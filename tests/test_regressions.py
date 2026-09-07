"""Regresiones observadas durante la auditoría de septiembre de 2026."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import validate_contract as validator
import export


class ContractRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = validator.load_catalog()

    def validate(self, content, css=None):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'index.html'
            path.write_text(content)
            if css is not None:
                (Path(tmp) / 'fonts.css').write_text(css)
            return validator.validate_html(path, self.catalog)

    def test_no_acepta_menciones_sin_carga(self):
        for content in [
            '<!-- <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter"> -->',
            '<style>body{font-family:Inter}</style>',
            '<script>const s = \'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter">\'</script>',
            '<link rel="preconnect" href="https://fonts.googleapis.com/css2?family=Inter">',
            '<link rel="stylesheet" href="https://example.org/Inter.css">',
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Interloper">',
            '<style>/* @font-face{font-family:Inter;src:url(inter.woff2)} */</style>',
            '<style>@font-face{font-family:Inter}</style>',
        ]:
            with self.subTest(content=content):
                result = self.validate('<html data-preset="21-bento-grids"><head>' + content + '</head></html>')
                self.assertIn('MISSING_FONT', result.codes)

    def test_contenedor_y_alias_documentados(self):
        content = '''<html><head>
        <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,900">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400">
        </head><body><main data-preset=soffia-warm data-theme=dark>Panel</main></body></html>'''
        result = self.validate(content)
        self.assertTrue(result.ok, result)
        self.assertEqual(result.preset_id, '14-soffia-warm')

    def test_css_local_y_font_face(self):
        content = '<html data-preset="21-bento-grids"><head><link rel="stylesheet" href="fonts.css"></head></html>'
        self.assertTrue(self.validate(content, '@font-face{font-family:"Inter";src:url("inter.woff2")}').ok)

    def test_no_acepta_preset_dentro_de_script(self):
        result = self.validate('<script>const s = \'<html data-preset="21-bento-grids">\'</script>')
        self.assertIn('MISSING_PRESET', result.codes)

    def test_valida_todos_los_contenedores(self):
        content = '<html data-preset="21-bento-grids"><head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter"></head><body><main data-preset="99-fake"></main></body></html>'
        self.assertIn('UNKNOWN_PRESET', self.validate(content).codes)

    def test_config_invalida_es_error_controlado(self):
        raw = json.loads((ROOT/'references/presets.json').read_text())
        cases = [[], None, 1]
        for field, value in [('fonts', None), ('fonts', []), ('color', {'bg':'red','accent':'multi-section'}), ('id','wrong'), ('name','')]:
            data = copy.deepcopy(raw)
            data['presets'][0][field] = value
            cases.append(data)
        for data in cases:
            with self.subTest(data=str(data)[:80]), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp)/'catalog.json'
                path.write_text(json.dumps(data))
                with self.assertRaises(validator.ContractConfigError):
                    validator.load_catalog(path)


class ExportRegressions(unittest.TestCase):
    def test_pesos_y_colores_canonicos(self):
        content = export.PRESETS_FILE.read_text()
        meta = export.load_preset_metadata()
        for slug, weight in [('paper-and-ink',400), ('zero-interface',200), ('exaggerated-minimalism',400)]:
            with self.subTest(slug=slug):
                preset = export.extract_preset(content,slug)
                export.enrich_preset(preset,meta)
                self.assertIn('fontWeight: '+str(weight), export.build_frontmatter(preset).split('  body:')[0])


if __name__ == '__main__':
    unittest.main()
