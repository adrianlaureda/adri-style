import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_contract.py"
FIXTURES = ROOT / "tests" / "fixtures" / "contracts"


def load_validator():
    spec = importlib.util.spec_from_file_location("adri_contract", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("No se pudo cargar validate_contract.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ContractValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.catalog = cls.validator.load_catalog(
            ROOT / "references" / "presets.json"
        )

    def validate_fixture(self, name: str):
        return self.validator.validate_html(FIXTURES / name, self.catalog)

    def test_rechaza_html_sin_preset(self) -> None:
        result = self.validate_fixture("missing-preset.html")
        self.assertFalse(result.ok)
        self.assertIn("MISSING_PRESET", result.codes)

    def test_rechaza_preset_desconocido(self) -> None:
        result = self.validate_fixture("unknown-preset.html")
        self.assertFalse(result.ok)
        self.assertIn("UNKNOWN_PRESET", result.codes)

    def test_rechaza_fuentes_incoherentes(self) -> None:
        result = self.validate_fixture("incoherent-fonts.html")
        self.assertFalse(result.ok)
        self.assertIn("MISSING_FONT", result.codes)

    def test_acepta_pareja_tipografica_canonica(self) -> None:
        self.assertTrue(self.validate_fixture("valid-bold-signal.html").ok)

    def test_acepta_single_font_justificado(self) -> None:
        self.assertTrue(self.validate_fixture("valid-terminal-green.html").ok)

    def test_json_tiene_27_ids_contiguos_y_version_58(self) -> None:
        raw = json.loads(
            (ROOT / "references" / "presets.json").read_text(encoding="utf-8")
        )
        presets = raw["presets"]
        self.assertEqual(raw["adri_style_version"], "5.8")
        self.assertEqual([item["n"] for item in presets], list(range(1, 28)))
        self.assertEqual(len({item["id"] for item in presets}), 27)
        for item in presets:
            self.assertEqual(
                item["fonts"]["single_font"],
                item["fonts"]["display"] == item["fonts"]["body"],
            )
            self.assertIn(item["mode_default"], {"light", "dark"})

    def test_audit_valida_contrato_antes_de_impeccable(self) -> None:
        env = os.environ.copy()
        env["IMPECCABLE_REPO"] = "/tmp/impeccable-no-existe"
        proc = subprocess.run(
            [str(ROOT / "scripts" / "audit-adri.sh"),
             str(FIXTURES / "missing-preset.html")],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("MISSING_PRESET", proc.stdout + proc.stderr)
        self.assertNotIn("Impeccable no clonado", proc.stdout + proc.stderr)

    def test_audit_distingue_fallo_de_infraestructura(self) -> None:
        env = os.environ.copy()
        env["IMPECCABLE_REPO"] = "/tmp/impeccable-no-existe"
        proc = subprocess.run(
            [str(ROOT / "scripts" / "audit-adri.sh"),
             str(FIXTURES / "valid-bold-signal.html")],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("INFRASTRUCTURE_ERROR", proc.stdout + proc.stderr)

    def test_reporte_metrico_usa_exit_y_no_critical(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metrics = Path(tmp)
            (metrics / "2026-07-18.jsonl").write_text(
                "\n".join(
                    [
                        '{"critical":0,"exit":1,"top_tag":"infra"}',
                        '{"critical":0,"exit":0,"top_tag":""}',
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            env = os.environ.copy()
            env["METRICS_DIR"] = str(metrics)
            proc = subprocess.run(
                [str(ROOT / "scripts" / "measure-adri.sh"), "--report"],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("| 2026-07-18 | 2 | 1 | 50% |", proc.stdout)

    def test_auditoria_completa_fija_versiones_npx(self) -> None:
        script = (ROOT / "scripts" / "audit-adri-full.sh").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("@latest", script)
        self.assertIn("html-validate@11.5.6", script)
        self.assertIn("pa11y@9.1.1", script)
        self.assertIn("broken-link-checker@0.7.8", script)

    def test_auditoria_completa_propaga_error_de_infraestructura(self) -> None:
        env = os.environ.copy()
        env["IMPECCABLE_REPO"] = "/tmp/impeccable-no-existe"
        proc = subprocess.run(
            [
                str(ROOT / "scripts" / "audit-adri-full.sh"),
                str(FIXTURES / "valid-bold-signal.html"),
                "--quick",
            ],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("INFRASTRUCTURE_ERROR", proc.stdout + proc.stderr)

    def test_audit_no_infiere_semantica_solo_por_contar_colores(self) -> None:
        script = (ROOT / "scripts" / "audit-adri.sh").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("≥3 colores distintos", script)
        self.assertNotIn("color_count=", script)
        self.assertNotIn("minijuego con preset — transición intencional", script)
        self.assertNotIn('"$file" == *"adri-react/public/"*', script)
        self.assertNotIn("token de design system, no aplicación directa", script)
        self.assertNotIn("UI affordance — scroll/attention/pulse", script)


class SurfaceFixtureTests(unittest.TestCase):
    def test_las_cuatro_superficies_son_estructuralmente_distintas(self) -> None:
        surface_dir = ROOT / "tests" / "fixtures" / "surfaces"
        expected = {
            "console": "console-shell",
            "gallery": "media-stream",
            "dashboard": "metric-grid",
            "presentation": "slide-stage",
        }
        contents = {}
        for surface, marker in expected.items():
            html = (surface_dir / f"{surface}.html").read_text(encoding="utf-8")
            contents[surface] = html
            self.assertIn(f'data-surface="{surface}"', html)
            self.assertIn(marker, html)
            self.assertIn('data-preset="01-bold-signal"', html)
        self.assertEqual(len(set(contents.values())), 4)

    def test_no_impone_decoracion_comun(self) -> None:
        surface_dir = ROOT / "tests" / "fixtures" / "surfaces"
        htmls = [
            (surface_dir / f"{surface}.html").read_text(encoding="utf-8")
            for surface in ("console", "gallery", "dashboard", "presentation")
        ]
        for forbidden in ("decorative-number", "eyebrow", "bento-grid"):
            self.assertFalse(all(forbidden in html for html in htmls))

    def test_ejes_del_fixture_dashboard_no_tienen_relleno(self) -> None:
        html = (
            ROOT / "tests" / "fixtures" / "surfaces" / "dashboard.html"
        ).read_text(encoding="utf-8")
        self.assertIn(".axis{fill:none;stroke:", html)


if __name__ == "__main__":
    unittest.main()
