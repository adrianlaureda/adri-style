#!/usr/bin/env python3
"""Exporta un preset de adri-style al formato DESIGN.md.

Spec de referencia: https://github.com/google-labs-code/design.md/blob/main/docs/spec.md

Uso:
    export.py --preset=bold-signal
    export.py --preset=paper-and-ink --output=/tmp/pink.design.md
    export.py --list

Formato de salida (`--format=design-md`, único soportado):
    - YAML frontmatter con version/name/description/colors/typography/spacing/rounded/components
    - 8 secciones markdown fijas (Overview, Colors, Typography, Layout, Elevation & Depth,
      Shapes, Components, Do's and Don'ts)

Mapeo CSS -> design.md:
    --font-display/body/mono   -> typography.{display,body,mono}.fontFamily
    --lh-display/body          -> typography.{display,body}.lineHeight
    --bg* / --text* / --accent -> colors.*
    --border (con alpha)       -> colors.border (hex base + nota opacity)
    --radius                   -> rounded.base
    --transition / --ease-out  -> documentados en notas (no son tokens design.md)

El parser tolera valores HSL con notación moderna (sin comas) y los convierte a hex sRGB.
Los valores con canal alpha se convierten a hex de color base; la opacidad se anota aparte.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from textwrap import dedent

SKILL_ROOT = Path(__file__).resolve().parent.parent
PRESETS_FILE = SKILL_ROOT / "references" / "style-presets.md"
PRESETS_JSON = SKILL_ROOT / "references" / "presets.json"
DEFAULT_OUTPUT_DIR = SKILL_ROOT / "exports"

SPACING_SCALE = {
    "3xs": "4px",
    "2xs": "8px",
    "xs":  "12px",
    "s":   "16px",
    "m":   "24px",
    "l":   "32px",
    "xl":  "48px",
    "2xl": "72px",
    "3xl": "112px",
}

PRESET_HEADING_RE = re.compile(r"^## (\d+)\. (.+)$", re.MULTILINE)
ROOT_BLOCK_RE = re.compile(r":root\s*\{(.*?)\}", re.DOTALL)
VAR_LINE_RE = re.compile(r"--([a-z0-9-]+)\s*:\s*([^;]+?)\s*;")
IDEAL_FOR_RE = re.compile(r"\*\*Ideal for:\*\*\s*\n((?:-[^\n]*\n)+)", re.MULTILINE)


def slugify(name: str) -> str:
    # La estrella y el descriptor editorial no forman parte del ID canónico.
    name = re.sub(r"\s*★.*$", "", name).strip()
    name = name.lower()
    name = name.replace("&", " and ")
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return name.strip("-")


# ---------- Conversión de color -------------------------------------------------

def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def _hue_to_rgb(p: float, q: float, t: float) -> float:
    if t < 0:
        t += 1
    if t > 1:
        t -= 1
    if t < 1 / 6:
        return p + (q - p) * 6 * t
    if t < 1 / 2:
        return q
    if t < 2 / 3:
        return p + (q - p) * (2 / 3 - t) * 6
    return p


def hsl_to_hex(h: float, s: float, l: float) -> str:
    """h grados [0,360), s y l en [0,1]. Devuelve #rrggbb."""
    h = (h % 360) / 360
    s = _clamp01(s)
    l = _clamp01(l)
    if s == 0:
        v = round(l * 255)
        return f"#{v:02x}{v:02x}{v:02x}"
    q = l * (1 + s) if l < 0.5 else l + s - l * s
    p = 2 * l - q
    r = _hue_to_rgb(p, q, h + 1 / 3)
    g = _hue_to_rgb(p, q, h)
    b = _hue_to_rgb(p, q, h - 1 / 3)
    return f"#{round(r*255):02x}{round(g*255):02x}{round(b*255):02x}"


HSL_RE = re.compile(
    r"hsl\(\s*([\d.]+)\s+([\d.]+)%\s+([\d.]+)%\s*(?:/\s*([\d.]+))?\s*\)",
    re.IGNORECASE,
)
HEX_RE = re.compile(r"^#([0-9a-f]{3}|[0-9a-f]{6})$", re.IGNORECASE)


@dataclass
class ColorValue:
    hex: str
    alpha: float | None = None
    raw: str = ""

    def to_yaml(self) -> str:
        return f'"{self.hex}"'


def parse_color(raw: str) -> ColorValue | None:
    raw = raw.strip()
    hex_match = HEX_RE.match(raw)
    if hex_match:
        body = hex_match.group(1)
        if len(body) == 3:
            body = "".join(c * 2 for c in body)
        return ColorValue(hex=f"#{body.lower()}", alpha=None, raw=raw)
    hsl_match = HSL_RE.match(raw)
    if hsl_match:
        h, s, l, a = hsl_match.groups()
        alpha = float(a) if a is not None else None
        return ColorValue(
            hex=hsl_to_hex(float(h), float(s) / 100, float(l) / 100),
            alpha=alpha,
            raw=raw,
        )
    return None


# ---------- Extracción del preset ----------------------------------------------

@dataclass
class Preset:
    number: int
    name: str
    slug: str
    description: str
    ideal_for: list[str] = field(default_factory=list)
    vars: dict[str, str] = field(default_factory=dict)
    raw_block: str = ""
    mode_default: str = "light"
    single_font: bool = False
    weights_display: str = ""
    weights_body: str = ""


def load_preset_metadata(path: Path = PRESETS_JSON) -> dict[int, dict]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise ValueError(f"No se pudo cargar metadata de presets: {exc}") from exc
    presets = raw.get("presets")
    if not isinstance(presets, list):
        raise ValueError("references/presets.json no contiene presets")
    return {int(item["n"]): item for item in presets}


def enrich_preset(preset: Preset, metadata: dict[int, dict]) -> Preset:
    item = metadata.get(preset.number)
    if item is None:
        raise ValueError(f"Falta metadata para preset {preset.number}")
    fonts = item["fonts"]
    preset.mode_default = item["mode_default"]
    preset.single_font = fonts["single_font"]
    preset.weights_display = fonts["weights_display"]
    preset.weights_body = fonts["weights_body"]
    return preset


def list_presets(content: str) -> list[tuple[int, str, str]]:
    out = []
    for m in PRESET_HEADING_RE.finditer(content):
        num = int(m.group(1))
        name = m.group(2).strip()
        out.append((num, name, slugify(name)))
    return out


def extract_preset(content: str, slug: str) -> Preset | None:
    matches = list(PRESET_HEADING_RE.finditer(content))
    for i, m in enumerate(matches):
        name = m.group(2).strip()
        if slugify(name) != slug:
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section = content[start:end]

        desc_match = re.match(r"\s*\n([^\n][^\n]+)\n", section)
        description = desc_match.group(1).strip() if desc_match else ""

        ideal_for = []
        ifor = IDEAL_FOR_RE.search(section)
        if ifor:
            for line in ifor.group(1).splitlines():
                line = line.strip()
                if line.startswith("-"):
                    ideal_for.append(line.lstrip("-").strip())

        root_match = ROOT_BLOCK_RE.search(section)
        raw_block = root_match.group(0) if root_match else ""
        vars_ = {}
        if root_match:
            for v in VAR_LINE_RE.finditer(root_match.group(1)):
                vars_[v.group(1)] = v.group(2).strip()

        return Preset(
            number=int(m.group(1)),
            name=name,
            slug=slug,
            description=description,
            ideal_for=ideal_for,
            vars=vars_,
            raw_block=raw_block,
        )
    return None


# ---------- Construcción del DESIGN.md -----------------------------------------

COLOR_KEYS_ORDER = [
    "bg",
    "bg-surface",
    "bg-elevated",
    "border",
    "text",
    "text-secondary",
    "text-muted",
    "accent",
    "accent-surface",
    "accent-blue",
    "accent-green",
    "accent-amber",
    "accent-red",
    "accent-purple",
]


def indent(block: str, spaces: int) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line else line for line in block.splitlines())


def yaml_quote(value: str) -> str:
    return '"' + value.replace('"', '\\"') + '"'


def build_frontmatter(preset: Preset) -> str:
    v = preset.vars

    # Colors
    color_lines = []
    alpha_notes: list[tuple[str, float]] = []
    for key in COLOR_KEYS_ORDER:
        if key not in v:
            continue
        parsed = parse_color(v[key])
        if parsed is None:
            continue
        color_lines.append(f'  {key}: {parsed.to_yaml()}')
        if parsed.alpha is not None:
            alpha_notes.append((key, parsed.alpha))

    # Typography
    display_family = v.get("font-display", "system-ui, sans-serif").strip()
    body_family = v.get("font-body", "system-ui, sans-serif").strip()
    mono_family = v.get("font-mono", "monospace").strip()
    lh_display = v.get("lh-display", "1.05").strip()
    lh_body = v.get("lh-body", "1.55").strip()

    typography_block = dedent(f"""\
      display:
        fontFamily: {yaml_quote(display_family)}
        fontSize: "clamp(2.5rem, 2rem + 2.5vw, 4rem)"
        fontWeight: 700
        lineHeight: {lh_display}
        letterSpacing: "-0.04em"
      body:
        fontFamily: {yaml_quote(body_family)}
        fontSize: "1rem"
        fontWeight: 400
        lineHeight: {lh_body}
        letterSpacing: "0"
      mono:
        fontFamily: {yaml_quote(mono_family)}
        fontSize: "0.9375rem"
        fontWeight: 400
        lineHeight: 1.5
        letterSpacing: "0"
        fontFeature: "tnum"
    """).rstrip()

    # Spacing (escala Utopia documentada en base.css/layout.md)
    spacing_lines = [f'  "{k}": "{val}"' for k, val in SPACING_SCALE.items()]

    # Rounded
    radius_raw = v.get("radius", "8px").strip()
    rounded_lines = [
        f'  base: "{radius_raw}"',
        f'  pill: "9999px"',
    ]

    # Componentes accionables disponibles; no obligan a usar cards o inputs.
    components_block = dedent(f"""\
      button-primary:
        background: "token(colors.accent)"
        color: "token(colors.bg)"
        borderRadius: "token(rounded.base)"
        paddingX: "token(spacing.m)"
        paddingY: "token(spacing.2xs)"
        fontWeight: 500
    """).rstrip()

    alpha_note = ""
    if alpha_notes:
        joined = ", ".join(f"{k} (α={a})" for k, a in alpha_notes)
        alpha_note = f"# color alpha conservado en CSS original: {joined}"

    fm_parts = [
        "---",
        'version: "alpha"',
        f"name: {yaml_quote(preset.name)}",
        f"description: {yaml_quote(preset.description)}",
        "mode:",
        f'  default: "{preset.mode_default}"',
        "colors:",
        *color_lines,
        "typography:",
        indent(typography_block, 2),
        "spacing:",
        *spacing_lines,
        "rounded:",
        *rounded_lines,
        "components:",
        indent(components_block, 2),
    ]
    if alpha_note:
        fm_parts.append(alpha_note)
    fm_parts.append("---")
    return "\n".join(fm_parts)


def build_sections(preset: Preset) -> str:
    v = preset.vars
    ideal_bullets = "\n".join(f"- {item}" for item in preset.ideal_for) or "- General-purpose."

    colors_rows = []
    for key in COLOR_KEYS_ORDER:
        if key not in v:
            continue
        parsed = parse_color(v[key])
        hex_val = parsed.hex if parsed else v[key]
        note = f" (α={parsed.alpha})" if parsed and parsed.alpha is not None else ""
        colors_rows.append(f"| `{key}` | `{hex_val}`{note} | `{v[key]}` |")
    colors_table = "\n".join(colors_rows)

    light_rows = []
    # Busca el bloque [data-theme="light"]
    light_block_re = re.compile(r"\[data-theme=\"light\"\]\s*\{(.*?)\}", re.DOTALL)
    lm = light_block_re.search(preset.raw_block) if False else None
    # raw_block solo contiene :root — no tiene light. Se referencia en sección.
    _ = light_rows, lm  # placeholder

    display_family = v.get("font-display", "system-ui, sans-serif").strip()
    body_family = v.get("font-body", "system-ui, sans-serif").strip()
    mono_family = v.get("font-mono", "monospace").strip()
    radius_raw = v.get("radius", "8px").strip()
    accent_raw = v.get("accent", "#ffffff").strip()
    font_policy = (
        "single-font justificado por el preset"
        if preset.single_font
        else "pareja display/body canónica"
    )

    sections = f"""\
## Overview

**{preset.name}** — {preset.description}

### Ideal for

{ideal_bullets}

### Notes

- Modo inicial: `{preset.mode_default}`; un toggle es opcional según la superficie.
- Política tipográfica: {font_policy}.
- Fondo base nunca `#000000` puro (ver `references/color-and-theme.md`).
- Escala tipográfica fluida Utopia (`--step-*`), no px fijos.

## Colors

| Token | Hex | Fuente CSS |
|-------|-----|-----------|
{colors_table}

Los valores con canal alpha se preservan en el CSS original (ver columna *Fuente CSS*). El hex listado es el color base sRGB sin opacidad, tal y como exige el spec.

## Typography

| Rol | Font family | Weight | Line height | Letter spacing |
|-----|-------------|--------|-------------|----------------|
| Display | `{display_family}` | {preset.weights_display or "según preset"} | {v.get('lh-display', '1.05')} | -0.04em |
| Body | `{body_family}` | {preset.weights_body or "según preset"} | {v.get('lh-body', '1.55')} | 0 |
| Mono | `{mono_family}` | 400 | 1.5 | 0 (tabular-nums) |

Reglas transversales (desde `SKILL.md`):

- Pareja o single-font según `references/presets.json`.
- `text-wrap: balance` en todos los h1-h6.
- `font-variant-numeric: tabular-nums` en datos numéricos.

## Layout

- La superficie define ancho, densidad, scroll y breakpoints.
- Prose de lectura: aproximadamente `65ch`.
- Spacing disponible en frontmatter: xs→3xl.
- No hay cuota universal de layouts, cards o visualizaciones.

Ver `references/layout.md` y `references/composition.md`.

## Elevation & Depth

- El preset y la superficie deciden si usan bordes, sombras o gradientes.
- EAR elimina contenedores sin función.
- Los tokens `--bg`, `--bg-surface` y `--bg-elevated` están disponibles sin
  obligar a crear tres planos.

## Shapes

- Radius base: `{radius_raw}`.
- Pills: `100px` / `9999px` (badges, botones pill).
- Consistencia: todos los componentes (cards, inputs, buttons) usan `token(rounded.base)` salvo pills explícitas.

## Components

Tokens accionables disponibles en `components:`:

- `button-primary` — fondo `--accent`, texto `--bg`, radius base.

No se exportan cards universales. Cada superficie crea solo los contenedores que
superan EAR.

Ver `references/components.md` para catálogo extendido (bento grid, patrones premium dark mode, anti-AI-slop).

## Do's and Don'ts

**Do**

- Usar escala tipográfica fluida con `clamp()` (variables `--step-*`).
- `text-wrap: balance` en headings.
- 3 roles tipográficos definidos; pareja o single-font según el preset.
- Modo inicial del preset; toggle solo si la superficie lo necesita.
- `font-variant-numeric: tabular-nums` en datos numéricos.
- Iconos Lucide SVG (`stroke-width: 1.5`).
- Near-black para fondo oscuro: `#0a0a0a` o `hsl(220 15% 8%)`.
- Hover states con `transform` o `border-color` (no solo color).
- `prefers-reduced-motion` envolviendo animaciones no esenciales.

**Don't**

- `font-weight > 900` (display 700–900 Black, body nunca > 600).
- Cajas, sombras o gradientes sin función ni permiso del preset.
- Emojis en la interfaz (usar Lucide SVG).
- Fondo `#000000` puro.
- `bg-indigo-500` ni purple gradients Tailwind default.
- 3 cards idénticas con icono en grid como layout principal (anti-AI-slop).
- Grises puros `hsl(0, 0%, N%)` — siempre tinted.
- Single-font no declarado por el preset.
- Accent solid plano sin variante `--accent-surface` para backgrounds tintados.

Accent base: `{accent_raw}`.
"""
    return sections.rstrip() + "\n"


def build_design_md(preset: Preset) -> str:
    return build_frontmatter(preset) + "\n\n" + build_sections(preset)


# ---------- CLI ----------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Exporta un preset de adri-style al formato DESIGN.md.",
    )
    ap.add_argument("--preset", help="Slug del preset (ej. bold-signal, paper-and-ink)")
    ap.add_argument("--format", default="design-md", help="Formato de salida (único: design-md)")
    ap.add_argument("--output", help="Path de salida. Default: exports/<slug>.design.md")
    ap.add_argument("--list", action="store_true", help="Lista los slugs de preset disponibles")
    ap.add_argument("--stdout", action="store_true", help="Emite a stdout en vez de fichero")
    args = ap.parse_args(argv)

    if args.format != "design-md":
        print(f"error: format {args.format!r} no soportado (único: design-md)", file=sys.stderr)
        return 2

    if not PRESETS_FILE.exists():
        print(f"error: no existe {PRESETS_FILE}", file=sys.stderr)
        return 1

    content = PRESETS_FILE.read_text(encoding="utf-8")
    try:
        metadata = load_preset_metadata()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.list:
        for num, name, slug in list_presets(content):
            print(f"{num:>3}. {slug}  ({name})")
        return 0

    if not args.preset:
        print("error: se requiere --preset (o usa --list)", file=sys.stderr)
        return 2

    preset = extract_preset(content, args.preset)
    if preset is None:
        print(f"error: preset {args.preset!r} no encontrado. Usa --list.", file=sys.stderr)
        return 1
    try:
        enrich_preset(preset, metadata)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    output = build_design_md(preset)

    if args.stdout:
        sys.stdout.write(output)
        return 0

    out_path = Path(args.output) if args.output else DEFAULT_OUTPUT_DIR / f"{preset.slug}.design.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
