---
version: "alpha"
name: "Bold Signal ★ (Default Adri)"
description: "**Marca personal de Adri por antonomasia.** Cuerpo Inter 300 (fina), Satoshi 900 para display, ángulos rectos (`--radius: 0`), paleta neutra blanco/negro/grises con 6 acentos opcionales por dominio. Light por defecto, dark via `[data-theme=\"dark\"]`. Validado en producción en `formacion-xograr`, `planificacion-4eso`, `adri-react` y el brandbook live (https://branding-adri.adrianlaureda.workers.dev/)."
mode:
  default: "light"
colors:
  bg: "#f8f8f8"
  bg-surface: "#ffffff"
  bg-elevated: "#efefef"
  border: "#000000"
  text: "#0a0a0a"
  text-secondary: "#000000"
  text-muted: "#000000"
  accent: "#0a0a0a"
  accent-surface: "#000000"
typography:
  display:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: "clamp(2.5rem, 2rem + 2.5vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  body:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  mono:
    fontFamily: "'JetBrains Mono', 'SF Mono', Menlo, monospace"
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
  base: "0px"
  pill: "9999px"
components:
  button-primary:
    background: "token(colors.accent)"
    color: "token(colors.bg)"
    borderRadius: "token(rounded.base)"
    paddingX: "token(spacing.m)"
    paddingY: "token(spacing.2xs)"
    fontWeight: 500
# color alpha conservado en CSS original: border (α=0.1), text-secondary (α=0.6), text-muted (α=0.35), accent-surface (α=0.06)
---

## Overview

**Bold Signal ★ (Default Adri)** — **Marca personal de Adri por antonomasia.** Cuerpo Inter 300 (fina), Satoshi 900 para display, ángulos rectos (`--radius: 0`), paleta neutra blanco/negro/grises con 6 acentos opcionales por dominio. Light por defecto, dark via `[data-theme="dark"]`. Validado en producción en `formacion-xograr`, `planificacion-4eso`, `adri-react` y el brandbook live (https://branding-adri.adrianlaureda.workers.dev/).

### Ideal for

- General-purpose.

### Notes

- Modo inicial: `light`; un toggle es opcional según la superficie.
- Política tipográfica: pareja display/body canónica.
- Fondo base nunca `#000000` puro (ver `references/color-and-theme.md`).
- Escala tipográfica fluida Utopia (`--step-*`), no px fijos.

## Colors

| Token | Hex | Fuente CSS |
|-------|-----|-----------|
| `bg` | `#f8f8f8` | `#f8f8f8` |
| `bg-surface` | `#ffffff` | `#ffffff` |
| `bg-elevated` | `#efefef` | `#efefef` |
| `border` | `#000000` (α=0.1) | `hsl(0 0% 0% / 0.10)` |
| `text` | `#0a0a0a` | `#0a0a0a` |
| `text-secondary` | `#000000` (α=0.6) | `hsl(0 0% 0% / 0.60)` |
| `text-muted` | `#000000` (α=0.35) | `hsl(0 0% 0% / 0.35)` |
| `accent` | `#0a0a0a` | `#0a0a0a` |
| `accent-surface` | `#000000` (α=0.06) | `hsl(0 0% 0% / 0.06)` |

Los valores con canal alpha se preservan en el CSS original (ver columna *Fuente CSS*). El hex listado es el color base sRGB sin opacidad, tal y como exige el spec.

## Typography

| Rol | Font family | Weight | Line height | Letter spacing |
|-----|-------------|--------|-------------|----------------|
| Display | `'Satoshi', system-ui, -apple-system, sans-serif` | 500-900 | 1.05 | -0.04em |
| Body | `'Inter', system-ui, -apple-system, sans-serif` | 300-400 | 1.55 | 0 |
| Mono | `'JetBrains Mono', 'SF Mono', Menlo, monospace` | 400 | 1.5 | 0 (tabular-nums) |

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

- Radius base: `0px`.
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

Accent base: `#0a0a0a`.
