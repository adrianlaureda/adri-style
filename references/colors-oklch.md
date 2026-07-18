# Colors OKLCH — referencia adicional (no-breaking, v5.7+)

Espacio de color perceptualmente uniforme. Soporte navegador estable desde Chrome 111 / Safari 15.4 / Firefox 113.

**Propósito**: cuando un preset adri-style necesite variantes de un accent (hover más claro, semántico más oscuro, paleta derivada), OKLCH garantiza diferencias perceptuales coherentes que HSL no garantiza.

**Esto es una capa adicional, no un reemplazo.** Los presets actuales en `style-presets.md` siguen usando HSL/HEX. OKLCH se añade como par opcional `--accent-oklch` cuando hace falta cálculo perceptual.

## Cuándo usar OKLCH (y cuándo no)

| Usar OKLCH | Mantener HSL/HEX |
|---|---|
| Generar variantes de luminance (hover, disabled, semantic) | Color base del preset (legibilidad humana en código) |
| Garantizar contraste WCAG 2.1 AA programáticamente | Diseño rápido / output one-shot |
| Pares de colores con mismo brillo percibido (semáforo neutralizado) | Cuando el lector del CSS prefiere `#f59e0b` antes que `oklch(75% 0.15 60)` |
| Animación de color sin pasar por gris (`oklch` interpolation) | Animaciones de opacidad simples |

## Sintaxis CSS

```css
/* Lightness % · Chroma 0-0.4 · Hue grados */
:root {
  --accent: #f59e0b;                       /* HSL/HEX canónico */
  --accent-oklch: oklch(75% 0.15 60);      /* equivalente perceptual */
  --accent-hover: oklch(from var(--accent-oklch) calc(l + 0.08) c h);
  --accent-muted: oklch(from var(--accent-oklch) l calc(c * 0.4) h);
}
```

`oklch(from … …)` permite derivar tokens sin recalcular manualmente.

## Tabla de conversión — 27 accents canónicos

Generado a partir de `presets.json` con conversión RGB→OKLCH (mediana de aproximación, valores redondeados):

| # | Preset | HEX | OKLCH equivalente |
|---|--------|-----|-------------------|
| 1 | Bold Signal ★ | `#0a0a0a` | `oklch(15% 0 0)` |
| 2 | Electric Studio | `#3b82f6` | `oklch(63% 0.19 258)` |
| 3 | Creative Voltage | `#f59e0b` | `oklch(75% 0.15 60)` |
| 4 | Dark Botanical | `#4ade80` | `oklch(78% 0.18 145)` |
| 5 | Notebook Tabs | `#2563eb` | `oklch(53% 0.22 263)` |
| 6 | Pastel Geometry | `#e07850` | `oklch(67% 0.13 41)` |
| 7 | Split Pastel | `#e11d48` | `oklch(58% 0.22 22)` |
| 8 | Vintage Editorial | `#8B2E1F` | `oklch(40% 0.13 28)` |
| 9 | Neon Cyber | `#06ffa5` | `oklch(89% 0.23 162)` |
| 10 | Terminal Green | `#22c55e` | `oklch(72% 0.17 145)` |
| 11 | Swiss Modern | `#000000` | `oklch(0% 0 0)` |
| 12 | Paper & Ink | `#d4a574` | `oklch(75% 0.07 71)` |
| 13 | Minimalista Adri | `multi-section` | (variable por sección — generar oklch al asignar) |
| 14 | Soffia Warm | `#c9a96e` | `oklch(74% 0.07 78)` |
| 15 | Signal Hardware | `#f04d23` | `oklch(63% 0.21 36)` |
| 16 | Magazine Editorial | `#C1272D` | `oklch(50% 0.20 24)` |
| 17 | Cinematic Story | `#F59E0B` | `oklch(75% 0.15 60)` |
| 18 | Storytelling-Driven | `#D97706` | `oklch(64% 0.16 48)` |
| 19 | E-Ink Paper | `#1A1A1A` | `oklch(20% 0 0)` |
| 20 | Exaggerated Min | `#FF3B30` | `oklch(63% 0.23 27)` |
| 21 | Bento Grids | `#1D1D1F` | `oklch(22% 0 0)` |
| 22 | Zero Interface | `hsl(220 10% 40%)` | `oklch(46% 0.02 257)` |
| 23 | Neumorphism | `#5E72E4` | `oklch(60% 0.16 268)` |
| 24 | Motion-Driven | `#22C55E` | `oklch(72% 0.17 145)` |
| 25 | Micro-interactions | `#22C55E` | `oklch(72% 0.17 145)` |
| 26 | AI-Native UI | `#6366F1` | `oklch(58% 0.20 277)` |
| 27 | Interactive Cursor | `#5E6AD2` | `oklch(58% 0.16 271)` |

## Patrones canónicos

### Variante hover (más clara, +8% L)

```css
.btn:hover {
  background: oklch(from var(--accent-oklch) calc(l + 0.08) c h);
}
```

### Variante muted (mismo hue, chroma 40%)

```css
.btn-secondary {
  color: oklch(from var(--accent-oklch) l calc(c * 0.4) h);
}
```

### Garantizar contraste AA sobre fondo

```css
/* Si --bg-oklch tiene L%, el texto necesita L diferencia ≥ 0.5 para AA. */
.text-on-accent {
  color: oklch(from var(--bg-oklch) clamp(0.05, calc(l > 0.5 ? l - 0.55 : l + 0.55), 0.95) 0 0);
}
```

(Implementación simplificada — para producción usa el cálculo APCA o la fórmula WCAG completa.)

### Animación entre dos colores sin pasar por gris

```css
@keyframes shift {
  from { background: oklch(60% 0.20 30); }
  to   { background: oklch(70% 0.20 200); }
}
/* En HSL/RGB esa animación pasa por gris hacia 50% lightness. En OKLCH mantiene saturación percibida. */
```

## Migración a v6 (futuro, breaking)

Si en algún momento el JSON canónico de presets se reescribe en v6:

1. `presets.json` añade campo `color.accent_oklch` por preset.
2. `bootstrap-adri.html` carga ambos (`--accent` HEX + `--accent-oklch` OKLCH).
3. Documentación obliga a usar OKLCH para variantes derivadas; HEX queda solo para el valor base canónico.
4. `audit-adri.sh` verifica coherencia (si declara `oklch()` pero no `--accent-oklch`, FAIL).

Hasta entonces (v5.7+), OKLCH es **opcional y no-breaking**. Esta referencia documenta el patrón para que cualquier output que lo necesite sepa cómo aplicarlo.

## Soporte navegador

- Chrome 111+ (marzo 2023) · Edge 111+ · Safari 15.4+ (marzo 2022) · Firefox 113+ (mayo 2023).
- Cobertura caniuse: ~96% global a 2026-05.
- Fallback: declarar par `--accent` (HEX) + `--accent-oklch` (OKLCH); si el navegador no soporta OKLCH, ignora la declaración y usa el HEX.

## Referencias externas

- [Spec CSS Color Module Level 4](https://www.w3.org/TR/css-color-4/#ok-lab) (W3C).
- [OKLCH playground](https://oklch.com) — picker visual.
- [Evil Martians OKLCH explainer](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl) — por qué OKLCH supera HSL/HSL.
