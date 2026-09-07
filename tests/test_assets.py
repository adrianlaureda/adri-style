"""Coherencia del contenido generado y contraste de los tokens documentados."""
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_contract import load_catalog, validate_html
from preset_assets import contrast, rgb, font_stylesheets, preview_tokens
from export import list_presets, extract_preset, enrich_preset, build_design_md, parse_color, VAR_LINE_RE


class AssetsTests(unittest.TestCase):
    def test_contrastes_derivados_para_los_27_presets(self):
        self.assertAlmostEqual(contrast('#ffffff','#000000'),21)
        for p in load_catalog().values():
            with self.subTest(preset=p['id']):
                tokens=preview_tokens(p)
                for foreground,background in [(tokens['text'],p['color']['bg']),
                       (tokens['accent_ink'],p['color']['bg']),(tokens['on_accent'],p['color']['accent'])]:
                    self.assertGreaterEqual(contrast(foreground,background),4.5)
                self.assertTrue(font_stylesheets(p))

    def test_todas_las_muestras_cumplen_contrato(self):
        catalog=load_catalog()
        paths=[ROOT/'templates/bootstrap-adri.html',*list((ROOT/'tests/fixtures/surfaces').glob('*.html'))]
        for path in paths:
            with self.subTest(path=path):
                result=validate_html(path,catalog)
                self.assertTrue(result.ok,result.findings)

    def test_exports_versionados_sin_drift(self):
        content=(ROOT/'references/style-presets.md').read_text()
        metadata={p['n']:p for p in load_catalog().values()}
        for path in (ROOT/'exports').glob('*.design.md'):
            preset=extract_preset(content,path.name.removesuffix('.design.md'))
            enrich_preset(preset,metadata)
            self.assertEqual(path.read_text(),build_design_md(preset),path.name)

    def test_documentacion_y_css_coherentes(self):
        result=subprocess.run([sys.executable,'scripts/generate_docs.py','--check'],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)

    def test_tokens_textuales_aa_en_temas_documentados(self):
        content=(ROOT/'references/style-presets.md').read_text()
        blocks=re.findall(r':root\s*\{[^}]*\}|\[data-theme="(?:light|dark)"\]\s*\{[^}]*\}',content)
        checked=0
        for block in blocks:
            values=dict(VAR_LINE_RE.findall(block))
            bg=parse_color(values.get('bg',''))
            if not bg:continue
            backgrounds=[bg.hex]
            for key in ('bg-surface','bg-elevated'):
                color=parse_color(values.get(key,''))
                if color and color.alpha is None:backgrounds.append(color.hex)
            for key in ('text','text-secondary','text-muted'):
                color=parse_color(values.get(key,''))
                if not color:continue
                for background in backgrounds:
                    actual=color.hex
                    if color.alpha is not None:
                        actual='#'+''.join(f'{round((a*color.alpha+b*(1-color.alpha))*255):02x}' for a,b in zip(rgb(color.hex),rgb(background)))
                    with self.subTest(key=key,color=actual,bg=background):
                        self.assertGreaterEqual(contrast(actual,background),4.5)
                    checked+=1
        self.assertGreater(checked,300)


if __name__=='__main__':unittest.main()
