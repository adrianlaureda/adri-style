import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets" / "preset-catalog.html"
SCHEMA = ROOT / "references" / "presets.schema.json"


class CatalogTests(unittest.TestCase):
    def test_catalogo_se_genera_desde_los_27_presets(self) -> None:
        html = CATALOG.read_text(encoding="utf-8")
        self.assertIn("adri-style v5.8", html)
        self.assertEqual(html.count('class="preset-option"'), 27)
        self.assertIn('data-preset-id="06-pastel-geometry"', html)
        self.assertIn('data-preset-id="07-split-pastel"', html)
        for surface in ("console", "gallery", "dashboard", "presentation"):
            self.assertIn(f'data-surface-option="{surface}"', html)

    def test_solo_una_superficie_puede_quedar_visible(self) -> None:
        html = CATALOG.read_text(encoding="utf-8")
        self.assertIn(".surface:not(.is-active){display:none}", html)

    def test_catalogo_versionado_esta_sincronizado(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate_catalog.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_existe_schema_del_contrato(self) -> None:
        schema = SCHEMA.read_text(encoding="utf-8")
        self.assertIn('"const": "5.8"', schema)
        self.assertIn('"minItems": 27', schema)
        self.assertIn('"maxItems": 27', schema)
        self.assertIn('"single_font"', schema)


if __name__ == "__main__":
    unittest.main()
