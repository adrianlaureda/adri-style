#!/usr/bin/env python3
"""Contrato de catálogo e inyección HTML; solo biblioteca estándar, sin red."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = ROOT / 'references/presets.json'


class ContractConfigError(RuntimeError):
    """Entrada ilegible o catálogo estructuralmente inválido."""


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    preset_id: str | None = None
    preset_ids: tuple[str, ...] = ()

    @property
    def ok(self):
        return not self.findings

    @property
    def codes(self):
        return {finding.code for finding in self.findings}


def _check_schema(value, schema, document, location='$'):
    """Evalúa el subconjunto del schema del repo; rechaza keywords desconocidas."""
    supported = {'$schema','$id','title','description','$defs','$ref','type','const',
                 'enum','required','properties','additionalProperties','items',
                 'minItems','maxItems','minLength','minimum','maximum','pattern','format'}
    if set(schema) - supported:
        raise ContractConfigError(f'{location}: keyword de schema no soportada')
    if '$ref' in schema:
        ref = schema['$ref']
        if not ref.startswith('#/$defs/'):
            raise ContractConfigError(f'{location}: referencia de schema no local')
        return _check_schema(value, document['$defs'][ref.split('/')[-1]], document, location)
    types = schema.get('type', [])
    types = [types] if isinstance(types, str) else types
    checks = {'object':lambda: isinstance(value,dict), 'array':lambda: isinstance(value,list),
              'string':lambda: isinstance(value,str), 'integer':lambda: type(value) is int,
              'boolean':lambda: type(value) is bool, 'null':lambda: value is None}
    if types and not any(checks[t]() for t in types):
        raise ContractConfigError(f'{location}: tipo incorrecto')
    if 'const' in schema and value != schema['const']:
        raise ContractConfigError(f'{location}: valor incorrecto')
    if 'enum' in schema and value not in schema['enum']:
        raise ContractConfigError(f'{location}: valor fuera del enum')
    if isinstance(value,dict):
        props = schema.get('properties',{})
        if set(schema.get('required',[])) - value.keys():
            raise ContractConfigError(f'{location}: faltan campos obligatorios')
        if schema.get('additionalProperties') is False and value.keys() - props.keys():
            raise ContractConfigError(f'{location}: campos no reconocidos')
        for key,item in value.items():
            if key in props:
                _check_schema(item,props[key],document,f'{location}.{key}')
    if isinstance(value,list):
        if not schema.get('minItems',0) <= len(value) <= schema.get('maxItems',float('inf')):
            raise ContractConfigError(f'{location}: longitud incorrecta')
        for i,item in enumerate(value):
            _check_schema(item,schema.get('items',{}),document,f'{location}[{i}]')
    if isinstance(value,str):
        if len(value.strip()) < schema.get('minLength',0) or ('pattern' in schema and not re.search(schema['pattern'],value)):
            raise ContractConfigError(f'{location}: cadena inválida')
        if schema.get('format') == 'date':
            from datetime import date
            try:
                date.fromisoformat(value)
            except ValueError as exc:
                raise ContractConfigError(f'{location}: fecha inválida') from exc
    if type(value) is int and not schema.get('minimum',float('-inf')) <= value <= schema.get('maximum',float('inf')):
        raise ContractConfigError(f'{location}: número fuera de rango')


def load_catalog(path: Path = DEFAULT_CATALOG) -> dict[str,dict]:
    try:
        raw = json.loads(path.read_text(encoding='utf-8'))
        schema = json.loads((ROOT/'references/presets.schema.json').read_text(encoding='utf-8'))
        _check_schema(raw,schema,schema)
    except (OSError,UnicodeError,ValueError,KeyError,TypeError) as exc:
        raise ContractConfigError(f'No se pudo validar el catálogo {path}: {exc}') from exc
    catalog = {}
    for n,preset in enumerate(raw['presets'],1):
        pid,fonts = preset['id'],preset['fonts']
        if preset['n'] != n or not pid.startswith(f'{n:02d}-') or pid in catalog:
            raise ContractConfigError(f'{pid}: ID o numeración incoherente')
        if fonts['single_font'] != (fonts['display'] == fonts['body']):
            raise ContractConfigError(f'{pid}: single_font contradice display/body')
        if fonts['single_font'] and not fonts['single_font_justified']:
            raise ContractConfigError(f'{pid}: single_font sin justificación')
        for role in ('display','body'):
            font_weights(fonts[f'weights_{role}'])
        if 'local_stylesheet' in fonts:
            stylesheet = ROOT / fonts['local_stylesheet']
            if not stylesheet.is_file():
                raise ContractConfigError(f'{pid}: hoja tipográfica local ausente')
        catalog[pid] = preset
    if sum(p.get('default',False) for p in catalog.values()) != 1:
        raise ContractConfigError('Debe existir exactamente un preset default')
    return catalog


def font_weights(value):
    """Pesos discretos o rango CSS, con sufijo documental 'var'."""
    value = re.sub(r'\s*\([^)]*\)', '', value).strip().removesuffix(' var')
    if re.fullmatch(r'\d+\s*-\s*\d+',value):
        low,high = map(int,value.split('-'))
        weights = list(range(low,high+1,100))
    elif re.fullmatch(r'\d+(?:\s*,\s*\d+)*',value):
        weights = [int(w) for w in value.split(',')]
    else:
        raise ContractConfigError(f'Rango de pesos inválido: {value}')
    if not weights or min(weights)<100 or max(weights)>1000:
        raise ContractConfigError(f'Pesos fuera de rango: {value}')
    return weights


def normalize_preset(value,catalog):
    if value in catalog:
        return value
    # Alias derivado del ID, sin catálogo paralelo (consumidor soffia-warm).
    return next((pid for pid in catalog if pid.split('-',1)[1] == value),value)


class HtmlResources(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.scopes = []
        self.links = []
        self.styles = []
        self.style_depth = 0
        self.inert_depth = 0

    def handle_starttag(self,tag,attrs):
        if tag in {'template','noscript'}:
            self.inert_depth += 1
        if self.inert_depth:
            return
        attrs = dict(attrs)
        if 'data-preset' in attrs and tag in {'html','body','main','div','section','article','aside','header','footer','nav'}:
            self.scopes.append((attrs.get('data-preset'),attrs.get('data-theme')))
        if tag == 'link' and 'stylesheet' in (attrs.get('rel') or '').lower().split() and 'disabled' not in attrs:
            self.links.append(attrs.get('href') or '')
        if tag == 'style':
            self.style_depth += 1

    def handle_endtag(self,tag):
        if tag in {'template','noscript'} and self.inert_depth:
            self.inert_depth -= 1
        if tag == 'style' and self.style_depth:
            self.style_depth -= 1

    def handle_data(self,data):
        if self.style_depth and not self.inert_depth:
            self.styles.append(data)


def _family(value):
    return value.strip().strip('\"\'').casefold()


def _provider_fonts(url):
    parsed = urlsplit(url)
    query = parse_qs(parsed.query)
    if parsed.hostname == 'fonts.googleapis.com' and parsed.path in {'/css','/css2'}:
        return {f.split(':',1)[0].casefold() for group in query.get('family',[]) for f in group.split('|')}
    if parsed.hostname == 'api.fontshare.com' and parsed.path == '/v2/css':
        return {f.split('@',1)[0].replace('-',' ').casefold() for f in query.get('f[]',[])}
    return set()


def loaded_fonts(resources,base=None):
    fonts,seen = set(),set()

    def stylesheet(url,directory):
        fonts.update(_provider_fonts(url))
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or directory is None:
            return
        path = (directory/unquote(parsed.path)).resolve()
        if path in seen or len(seen) >= 64 or path.suffix.lower() != '.css':
            return
        seen.add(path)
        try:
            css(path.read_text(encoding='utf-8'),path.parent)
        except (OSError,UnicodeError):
            return  # La ausencia de evidencia termina en MISSING_FONT.

    def css(content,directory):
        content = re.sub(r'/\*.*?\*/','',content,flags=re.S)
        for face in re.findall(r'@font-face\s*\{([^}]+)\}',content,re.I):
            family = re.search(r'(?:^|;)\s*font-family\s*:\s*([^;]+)',face,re.I)
            source = re.search(r'(?:^|;)\s*src\s*:\s*(.+)',face,re.I)
            if family and source and re.search(r'(?:url|local)\(\s*[\"\']?[^\s)\"\']',source.group(1),re.I):
                fonts.add(_family(family.group(1)))
        for match in re.finditer(r'@import\s+(?:url\(\s*)?[\"\']([^\"\']+)[\"\']',content,re.I):
            stylesheet(match.group(1),directory)

    for url in resources.links:
        stylesheet(url,base)
    for content in resources.styles:
        css(content,base)
    return fonts


def html_loads_font(html,font):
    resources = HtmlResources()
    resources.feed(html)
    return _family(font) in loaded_fonts(resources)


def validate_html(path: Path,catalog: dict[str,dict]) -> ValidationResult:
    try:
        resources = HtmlResources()
        resources.feed(path.read_text(encoding='utf-8'))
    except (OSError,UnicodeError) as exc:
        raise ContractConfigError(f'No se pudo leer {path}: {exc}') from exc
    if not resources.scopes:
        return ValidationResult((Finding('MISSING_PRESET','Falta data-preset en html o contenedor raíz'),))
    findings,ids = [],[]
    fonts = loaded_fonts(resources,path.parent)
    for value,theme in resources.scopes:
        pid = normalize_preset(value,catalog)
        if pid not in catalog:
            findings.append(Finding('UNKNOWN_PRESET',f'Preset desconocido: {value}'))
            continue
        if pid not in ids:
            ids.append(pid)
        if theme is not None and theme not in {'light','dark'}:
            findings.append(Finding('INVALID_THEME','data-theme debe ser light o dark'))
        for font in dict.fromkeys(catalog[pid]['fonts'][r] for r in ('display','body')):
            if _family(font) not in fonts:
                findings.append(Finding('MISSING_FONT',f'{pid} requiere cargar la fuente {font}'))
    return ValidationResult(tuple(findings),ids[0] if ids else None,tuple(ids))


def format_result(path,result):
    if result.ok:
        return f'CONTRACT_OK: {path} · preset {", ".join(result.preset_ids)}'
    return '\n'.join([f'CONTRACT_FAIL: {path}',*(f'  [{f.code}] {f.message}' for f in result.findings)])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html',type=Path)
    parser.add_argument('--catalog',type=Path,default=DEFAULT_CATALOG)
    parser.add_argument('--json',action='store_true')
    args = parser.parse_args(argv)
    try:
        result = validate_html(args.html,load_catalog(args.catalog))
    except ContractConfigError as exc:
        print(f'INFRASTRUCTURE_ERROR: {exc}',file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({'ok':result.ok,'preset_ids':result.preset_ids,'findings':[vars(f) for f in result.findings]}))
    else:
        print(format_result(args.html,result))
    return 0 if result.ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
