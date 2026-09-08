---
version: "alpha"
name: "Adri Console"
description: "Sistema visual de consola personal inspirado en Oura × WHOOP: escala gris oscura, gradiente ambiental muy sutil y azul acero como acento. Barlow local comparte familia entre display y body; display usa 500 y body 400 por defecto. El preset define tokens y tipografía, sin imponer layout."
mode:
  default: "dark"
colors:
  bg: "#111315"
  bg-surface: "#191c1f"
  text: "#f2f1ee"
  text-muted: "#aaaead"
  accent: "#8aaec3"
  on-accent: "#101014"
  accent-ink: "#8aaec3"
typography:
  display:
    fontFamily: "'Barlow', system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 2rem + 2.5vw, 4rem)"
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  body:
    fontFamily: "'Barlow', system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  mono:
    fontFamily: "monospace"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
    fontFeature: "tnum"
spacing:
  "3xs": "4px"
  "2xs": "8px"
  "xs": "12px"
  "s": "16px"
  "m": "24px"
  "l": "32px"
  "xl": "48px"
  "2xl": "72px"
  "3xl": "112px"
rounded:
  base: "8px"
  pill: "9999px"
components:
  button-primary:
    background: "token(colors.accent)"
    color: "token(colors.on-accent)"
    borderRadius: "token(rounded.base)"
    paddingX: "token(spacing.m)"
    paddingY: "token(spacing.2xs)"
    fontWeight: 500
---

## Overview

**Adri Console** — Sistema visual de consola personal inspirado en Oura × WHOOP: escala gris oscura, gradiente ambiental muy sutil y azul acero como acento. Barlow local comparte familia entre display y body; display usa 500 y body 400 por defecto. El preset define tokens y tipografía, sin imponer layout.

### Ideal for

- Consolas personales y dashboards de hábitos, salud o actividad
- Herramientas locales con modo oscuro y modo claro
- Interfaces densas que necesitan jerarquía tipográfica sobria

### Notes

- Modo inicial: `dark`; un toggle es opcional según la superficie.
- Política tipográfica: single-font justificado por el preset.
- Fondo base nunca `#000000` puro (ver `references/color-and-theme.md`).
- Escala tipográfica fluida Utopia (`--step-*`), no px fijos.

## Colors

| Token | Hex | Fuente CSS |
|-------|-----|-----------|
| `bg` | `#111315` | `#111315` |
| `bg-surface` | `#191c1f` | `#191c1f` |
| `border` | `rgba(235, 239, 242, .20)` | `rgba(235, 239, 242, .20)` |
| `text` | `#f2f1ee` | `#f2f1ee` |
| `text-muted` | `#aaaead` | `#aaaead` |
| `accent` | `#8aaec3` | `#8aaec3` |
| `on-accent` | `#101014` | `#101014` |
| `accent-ink` | `#8aaec3` | `#8aaec3` |

Los valores con canal alpha se preservan en el CSS original (ver columna *Fuente CSS*). El hex listado es el color base sRGB sin opacidad, tal y como exige el spec.

## Typography

| Rol | Font family | Weight | Line height | Letter spacing |
|-----|-------------|--------|-------------|----------------|
| Display | `'Barlow', system-ui, sans-serif` | 500 | 1.05 | -0.04em |
| Body | `'Barlow', system-ui, sans-serif` | 400,500,600 | 1.55 | 0 |
| Mono | `monospace` | 400 | 1.5 | 0 (tabular-nums) |

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
- Fondo contextual: `radial-gradient(110% 55% at 20% -8%, rgba(255,255,255,.075), transparent 58%), radial-gradient(70% 42% at 78% 28%, rgba(255,255,255,.025), transparent 64%), linear-gradient(180deg, #2a2e31 0%, #191c1f 34%, #0e1012 100%)`.


## Shapes

- Radius base: `8px`.
- Pills: `100px` / `9999px` (badges, botones pill).
- Consistencia: todos los componentes (cards, inputs, buttons) usan `token(rounded.base)` salvo pills explícitas.

## Components

Tokens accionables disponibles en `components:`:

- `button-primary` — fondo `--accent`, texto `--on-accent`, radius base.

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

- Pesos fuera del rango canónico del preset (también en fuentes de peso único).
- Cajas, sombras o gradientes sin función ni permiso del preset.
- Emojis en la interfaz (usar Lucide SVG).
- Fondo `#000000` puro.
- `bg-indigo-500` ni purple gradients Tailwind default.
- 3 cards idénticas con icono en grid como layout principal (anti-AI-slop).
- Grises puros `hsl(0, 0%, N%)` — siempre tinted.
- Single-font no declarado por el preset.
- Accent solid plano sin variante `--accent-surface` para backgrounds tintados.

Accent base: `#8aaec3`.
