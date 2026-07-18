---
version: "alpha"
name: "Paper & Ink"
description: "Tostado oscuro como papel craft con oro envejecido. Calidez literaria sin cursilería. La Instrument Serif tiene una elegancia contemporánea que diferencia este preset del editorial clásico."
colors:
  bg: "#1c1917"
  bg-surface: "#252220"
  bg-elevated: "#2e2b28"
  border: "#937c6c"
  text: "#e8e0d4"
  text-secondary: "#aa9e92"
  text-muted: "#7c736a"
  accent: "#d4a574"
  accent-surface: "#d4a677"
typography:
  display:
    fontFamily: "'Instrument Serif', 'Georgia', serif"
    fontSize: "clamp(2.5rem, 2rem + 2.5vw, 4rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  body:
    fontFamily: "'Inter', system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  mono:
    fontFamily: "'JetBrains Mono', monospace"
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
  base: "6px"
  pill: "9999px"
components:
  card:
    background: "#252220"
    borderColor: "token(colors.border)"
    borderRadius: "token(rounded.base)"
    padding: "token(spacing.m)"
  button-primary:
    background: "token(colors.accent)"
    color: "token(colors.bg)"
    borderRadius: "token(rounded.base)"
    paddingX: "token(spacing.m)"
    paddingY: "token(spacing.2xs)"
    fontWeight: 500
  input:
    background: "token(colors.bg-surface)"
    borderColor: "token(colors.border)"
    borderRadius: "token(rounded.base)"
    paddingX: "token(spacing.xs)"
    paddingY: "token(spacing.2xs)"
# color alpha conservado en CSS original: border (α=0.15), accent-surface (α=0.1)
---

## Overview

**Paper & Ink** — Tostado oscuro como papel craft con oro envejecido. Calidez literaria sin cursilería. La Instrument Serif tiene una elegancia contemporánea que diferencia este preset del editorial clásico.

### Ideal for

- Personal writing and reflection tools
- Literary journals and book projects
- Reading logs and annotation interfaces
- Any context where warmth matters more than precision

### Notes

- Dark mode primero; tema claro disponible vía `[data-theme="light"]`.
- Fondo base nunca `#000000` puro (ver `references/color-and-theme.md`).
- Escala tipográfica fluida Utopia (`--step-*`), no px fijos.

## Colors

| Token | Hex | Fuente CSS |
|-------|-----|-----------|
| `bg` | `#1c1917` | `#1c1917` |
| `bg-surface` | `#252220` | `#252220` |
| `bg-elevated` | `#2e2b28` | `#2e2b28` |
| `border` | `#937c6c` (α=0.15) | `hsl(25 15% 50% / 0.15)` |
| `text` | `#e8e0d4` | `#e8e0d4` |
| `text-secondary` | `#aa9e92` | `hsl(30 12% 62%)` |
| `text-muted` | `#7c736a` | `hsl(30 8% 45%)` |
| `accent` | `#d4a574` | `#d4a574` |
| `accent-surface` | `#d4a677` (α=0.1) | `hsl(30 52% 65% / 0.1)` |

Los valores con canal alpha se preservan en el CSS original (ver columna *Fuente CSS*). El hex listado es el color base sRGB sin opacidad, tal y como exige el spec.

## Typography

| Rol | Font family | Weight | Line height | Letter spacing |
|-----|-------------|--------|-------------|----------------|
| Display | `'Instrument Serif', 'Georgia', serif` | 700–900 | 1.05 | -0.04em |
| Body | `'Inter', system-ui, sans-serif` | 400 | 1.55 | 0 |
| Mono | `'JetBrains Mono', monospace` | 400 | 1.5 | 0 (tabular-nums) |

Reglas transversales (desde `SKILL.md`):

- Font pairing real: `--font-display` distinto de `--font-body`.
- `text-wrap: balance` en todos los h1-h6.
- `font-variant-numeric: tabular-nums` en datos numéricos.

## Layout

- Container: `max-width: 1000px`.
- Prose (lectura): `max-width: 65ch`.
- Breakpoints responsive: `900px` y `600px`.
- Spacing escala Utopia (ver frontmatter `spacing`): xs→3xl con clamp fluido.
- Padding hero: `clamp(80px, 12vw, 160px)` vertical.
- Padding sección funcional: `clamp(48px, 6vw, 80px)` vertical.

Ver `references/layout.md` y `references/composition.md`.

## Elevation & Depth

- **No usar `box-shadow` decorativo**: solo bordes (`--border`) + multi-layer inset para `card-premium`.
- Profundidad con gradientes radiales: `radial-gradient(ellipse at 70% 30%, rgba(accent, 0.04), transparent 60%)`.
- Niveles: `--bg` → `--bg-surface` → `--bg-elevated` (3 planos jerárquicos).
- En modo claro: opacidad del gradiente radial ≤ 0.03 y saturación baja.

## Shapes

- Radius base: `6px`.
- Pills: `100px` / `9999px` (badges, botones pill).
- Consistencia: todos los componentes (cards, inputs, buttons) usan `token(rounded.base)` salvo pills explícitas.

## Components

Tokens declarados en `components:` del frontmatter:

- `card` — fondo `--bg-surface`, border `--border`, radius base.
- `button-primary` — fondo `--accent`, texto `--bg`, radius base.
- `input` — fondo `--bg-surface`, border `--border`.

Ver `references/components.md` para catálogo extendido (bento grid, patrones premium dark mode, anti-AI-slop).

## Do's and Don'ts

**Do**

- Usar escala tipográfica fluida con `clamp()` (variables `--step-*`).
- `text-wrap: balance` en headings.
- 3 roles tipográficos definidos (display, body, mono) con font pairing real.
- Tema dual (oscuro por defecto) + toggle con persistencia en `localStorage`.
- `font-variant-numeric: tabular-nums` en datos numéricos.
- Iconos Lucide SVG (`stroke-width: 1.5`).
- Near-black para fondo oscuro: `#0a0a0a` o `hsl(220 15% 8%)`.
- Hover states con `transform` o `border-color` (no solo color).
- `prefers-reduced-motion` envolviendo animaciones no esenciales.

**Don't**

- `font-weight > 900` (display 700–900 Black, body nunca > 600).
- `box-shadow` decorativo (solo bordes).
- Emojis en la interfaz (usar Lucide SVG).
- Fondo `#000000` puro.
- `bg-indigo-500` ni purple gradients Tailwind default.
- 3 cards idénticas con icono en grid como layout principal (anti-AI-slop).
- Grises puros `hsl(0, 0%, N%)` — siempre tinted.
- Inter como única fuente sin display font contrastante.
- Accent solid plano sin variante `--accent-surface` para backgrounds tintados.

Accent base: `#d4a574`.
