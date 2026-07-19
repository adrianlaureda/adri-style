#!/usr/bin/env python3
"""Valida el contrato mínimo de un HTML adri-style sin dependencias externas."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote_plus


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = ROOT / "references" / "presets.json"
PRESET_RE = re.compile(r"""data-preset\s*=\s*["']([^"']+)["']""", re.I)
THEME_RE = re.compile(r"""data-theme\s*=\s*["']([^"']+)["']""", re.I)


class ContractConfigError(RuntimeError):
    """El catálogo no existe o no cumple su contrato estructural."""


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    preset_id: str | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def codes(self) -> set[str]:
        return {finding.code for finding in self.findings}


def load_catalog(path: Path = DEFAULT_CATALOG) -> dict[str, dict]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContractConfigError(f"No existe el catálogo: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContractConfigError(f"JSON inválido en {path}: {exc}") from exc

    if raw.get("adri_style_version") != "5.8":
        raise ContractConfigError(
            "references/presets.json debe declarar adri_style_version 5.8"
        )
    presets = raw.get("presets")
    if not isinstance(presets, list) or len(presets) != 27:
        raise ContractConfigError("El catálogo debe contener exactamente 27 presets")

    catalog: dict[str, dict] = {}
    for expected_n, preset in enumerate(presets, start=1):
        if not isinstance(preset, dict):
            raise ContractConfigError(f"Preset {expected_n}: objeto inválido")
        preset_id = preset.get("id")
        if preset.get("n") != expected_n:
            raise ContractConfigError(
                f"Preset {preset_id or expected_n}: n no contiguo"
            )
        if not isinstance(preset_id, str) or preset_id in catalog:
            raise ContractConfigError(f"Preset {expected_n}: id ausente o duplicado")
        fonts = preset.get("fonts", {})
        display = fonts.get("display")
        body = fonts.get("body")
        if not isinstance(display, str) or not isinstance(body, str):
            raise ContractConfigError(f"Preset {preset_id}: fuentes incompletas")
        if fonts.get("single_font") != (display == body):
            raise ContractConfigError(
                f"Preset {preset_id}: single_font contradice display/body"
            )
        if preset.get("mode_default") not in {"light", "dark"}:
            raise ContractConfigError(f"Preset {preset_id}: mode_default inválido")
        catalog[preset_id] = preset
    return catalog


def _font_tokens(font: str) -> tuple[str, ...]:
    base = font.casefold()
    return (
        base,
        base.replace(" ", "+"),
        base.replace(" ", "-"),
        base.replace(" ", "%20"),
    )


def html_loads_font(html: str, font: str) -> bool:
    hrefs = re.findall(
        r"""<link\b[^>]*\bhref\s*=\s*["']([^"']+)["'][^>]*>""",
        html,
        re.I,
    )
    declarations = re.findall(
        r"""font-family\s*:\s*([^;}]+)""",
        html,
        re.I,
    )
    decoded = unquote_plus(" ".join([*hrefs, *declarations])).casefold()
    compact = re.sub(r"\s+", " ", decoded)
    return any(token in compact for token in _font_tokens(font))


def validate_html(path: Path, catalog: dict[str, dict]) -> ValidationResult:
    try:
        html = path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError) as exc:
        raise ContractConfigError(f"No se pudo leer {path}: {exc}") from exc

    findings: list[Finding] = []
    html_without_comments = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    root_match = re.search(r"<html\b([^>]*)>", html_without_comments, re.I)
    root_attributes = root_match.group(1) if root_match else ""
    preset_match = PRESET_RE.search(root_attributes)
    if preset_match is None:
        findings.append(
            Finding("MISSING_PRESET", "Falta data-preset en el elemento raíz")
        )
        return ValidationResult(tuple(findings))

    preset_id = preset_match.group(1)
    preset = catalog.get(preset_id)
    if preset is None:
        findings.append(
            Finding("UNKNOWN_PRESET", f"Preset desconocido: {preset_id}")
        )
        return ValidationResult(tuple(findings), preset_id)

    theme_match = THEME_RE.search(root_attributes)
    if theme_match is not None and theme_match.group(1) not in {"light", "dark"}:
        findings.append(
            Finding("INVALID_THEME", "data-theme debe ser light o dark")
        )

    fonts = preset["fonts"]
    expected_fonts = [fonts["display"]]
    if not fonts["single_font"]:
        expected_fonts.append(fonts["body"])
    for font in expected_fonts:
        if not html_loads_font(html, font):
            findings.append(
                Finding(
                    "MISSING_FONT",
                    f"{preset_id} requiere cargar la fuente {font}",
                )
            )

    return ValidationResult(tuple(findings), preset_id)


def format_result(path: Path, result: ValidationResult) -> str:
    if result.ok:
        return f"CONTRACT_OK: {path} · preset {result.preset_id}"
    lines = [f"CONTRACT_FAIL: {path}"]
    lines.extend(
        f"  [{finding.code}] {finding.message}" for finding in result.findings
    )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida data-preset, modo y fuentes de un HTML adri-style."
    )
    parser.add_argument("html", type=Path)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    args = parser.parse_args(argv)

    try:
        catalog = load_catalog(args.catalog)
        result = validate_html(args.html, catalog)
    except ContractConfigError as exc:
        print(f"INFRASTRUCTURE_ERROR: {exc}", file=sys.stderr)
        return 2

    print(format_result(args.html, result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
