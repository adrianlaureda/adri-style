import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "export.py"
SPEC = importlib.util.spec_from_file_location("adri_export", MODULE_PATH)
assert SPEC and SPEC.loader
EXPORT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = EXPORT
SPEC.loader.exec_module(EXPORT)


class ExportTests(unittest.TestCase):
    def test_bold_signal_usa_slug_canonico(self) -> None:
        self.assertEqual(
            EXPORT.slugify("Bold Signal ★ (Default Adri)"),
            "bold-signal",
        )

    def test_extrae_los_27_presets(self) -> None:
        content = (ROOT / "references" / "style-presets.md").read_text(
            encoding="utf-8"
        )
        presets = EXPORT.list_presets(content)

        self.assertEqual(len(presets), 27)
        self.assertIn((1, "Bold Signal ★ (Default Adri)", "bold-signal"), presets)
        self.assertIsNotNone(EXPORT.extract_preset(content, "bold-signal"))

    def test_export_respeta_modo_y_politica_tipografica_del_json(self) -> None:
        content = (ROOT / "references" / "style-presets.md").read_text(
            encoding="utf-8"
        )
        metadata = EXPORT.load_preset_metadata()

        bold = EXPORT.extract_preset(content, "bold-signal")
        terminal = EXPORT.extract_preset(content, "terminal-green")
        assert bold is not None and terminal is not None
        EXPORT.enrich_preset(bold, metadata)
        EXPORT.enrich_preset(terminal, metadata)

        bold_output = EXPORT.build_design_md(bold)
        terminal_output = EXPORT.build_design_md(terminal)
        self.assertIn('default: "light"', bold_output)
        self.assertNotIn("Dark mode primero", bold_output)
        self.assertIn("pareja display/body canónica", bold_output)
        self.assertIn("single-font justificado", terminal_output)
        self.assertNotIn("\n  card:\n", bold_output)


if __name__ == "__main__":
    unittest.main()
