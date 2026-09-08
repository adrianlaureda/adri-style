#!/usr/bin/env python3
"""Sincroniza tablas humanas; verifica los bloques CSS contra el contrato."""
import argparse
import re
import sys
from pathlib import Path
from validate_contract import load_catalog
from export import list_presets, extract_preset, parse_color

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'references/style-presets.md'


def render(content,catalog):
    quick_start = content.index('| # | Name |')
    quick_end = content.index('\n\n---',quick_start)
    moods = {}
    for line in content[quick_start:quick_end].splitlines()[2:]:
        cols = [c.strip() for c in line.split('|')[1:-1]]
        moods[int(cols[0])] = cols[2]
    quick = ['| # | Name | Mood | Background | Accent | Display Font | Body Font |',
             '|---|------|------|------------|--------|-------------|-----------|']
    for p in catalog.values():
        quick.append(f"| {p['n']} | {p['name']} | {moods[p['n']]} | `{p['color']['bg']}` | `{p['color']['accent']}` | {p['fonts']['display']} | {p['fonts']['body']} |")
    content = content[:quick_start]+'\n'.join(quick)+content[quick_end:]
    start = content.index('| # | Preset | Display |')
    end = content.index('\n\n**Lectura de la tabla:**',start)
    rows = ['| # | Preset | Display | Body | Display weights | Body weights | Single-font? | Body >500 default? | Modo default | Caso aula real | Estado |',
            '|---|--------|---------|------|-----------------|--------------|--------------|--------------------|--------------|---------------|--------|']
    for p in catalog.values():
        f=p['fonts']
        values=[str(p['n']),p['name'],f['display'],f['body'],f['weights_display'],f['weights_body'],
                'Sí: '+f['single_font_justified'] if f['single_font'] else 'No',
                'Sí: '+f.get('body_over_500_justified','') if f['body_default_over_500'] else 'No',
                p['mode_default'],', '.join(p['uso_real']) or 'Sin uso verificado',p['estado']]
        rows.append('| '+' | '.join(v.replace('|','/') for v in values)+' |')
    return content[:start]+'\n'.join(rows)+content[end:]


def validate_css(content,catalog):
    errors=[]
    for n,name,slug in list_presets(content):
        preset=extract_preset(content,slug)
        p=next(item for item in catalog.values() if item['n']==n)
        for token in ('bg','accent'):
            actual=parse_color(preset.vars.get(token,''))
            expected=parse_color(p['color'][token])
            if not actual or not expected or actual.hex!=expected.hex:
                errors.append(f'{p["id"]}: CSS {token} no coincide con JSON')
        if 'background_image' in p['color']:
            actual=preset.vars.get('background-image','')
            actual=re.sub(r'var\(--([a-z-]+)\)',lambda match:preset.vars.get(match[1],''),actual)
            if re.sub(r'\s+','',actual)!=re.sub(r'\s+','',p['color']['background_image']):
                errors.append(f'{p["id"]}: gradiente CSS no coincide con JSON')
        for role in ('display','body'):
            actual=preset.vars.get('font-'+role,'').split(',')[0].strip(" '\"")
            if actual!=p['fonts'][role]:
                errors.append(f'{p["id"]}: font-{role} no coincide con JSON')
    if len(list_presets(content))!=len(catalog):
        errors.append('Número de bloques CSS distinto al catálogo')
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    try:
        content=SOURCE.read_text()
        catalog=load_catalog()
        generated=render(content,catalog)
        errors=validate_css(generated,catalog)
        if errors:
            print('\n'.join(errors)); return 1
        if args.check:
            if content!=generated:
                print('DOCS_OUT_OF_DATE'); return 1
            print('DOCS_OK'); return 0
        SOURCE.write_text(generated)
        print('DOCS_WRITTEN'); return 0
    except (OSError,ValueError,RuntimeError) as exc:
        print(f'DOCS_ERROR: {exc}',file=sys.stderr); return 2


if __name__=='__main__':
    raise SystemExit(main())
