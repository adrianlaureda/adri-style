# Tipografia

Fuentes: Butterick (principios), Utopia (escala fluida), Vercel Geist (tokens compostos).
Principio: a tipografia e a base do deseño; se a tipografia falla, todo falla.

## Sistema de fontes (font pairing)

> **REGLA v5.3 (post-audit Impeccable 2026-05-08)**: NO existe "fuente por defecto" global de adri-style. **El preset activo dicta las fuentes y pesos**. Si NO hay preset activo, el output debe abortar y pedir uno antes de generar. Inter es UNA opción entre muchas — su uso por defecto fue un anti-pattern detectado en outputs reales (adri-app, estacion-clasificacion). Cada preset en `style-presets.md` declara su pareja display/body explícitamente.

Tres roles tipograficos. Cada preset elige fuentes y pesos:

| Rol | Función | Catalogo de fuentes recomendadas |
|-----|---------|----------------------------------|
| Display/Headings | Titulos, heroes, headings | Satoshi, Cabinet Grotesk, Clash Display, Excon, Alpino, Space Grotesk, Plus Jakarta Sans, Instrument Serif, Playfair Display, Cormorant Garamond, Orbitron, DM Sans, Newsreader, Inter |
| Body/Copy | Texto corrido, parrafos | Inter, DM Sans, Satoshi, Switzer, Alpino, Pally, Nunito, Lora, Source Serif 4, General Sans |
| Mono/Data | Dashboards, codigo, tabular-nums | Geist Mono, JetBrains Mono, Fira Code, IBM Plex Mono |

**Antipatterns detectados en producción que NO se deben repetir** (audit Impeccable 2026-05-08):
- Single-font accidental: usar una familia sin que el preset declare
  `single_font=true`.
- Inter como default sin pensar el preset: el output tira de Inter porque "es lo seguro" → señal IA-generada.
- Display sin pareja body diferenciada: jerarquía floja.

**Decision tree para elexir fuentes:**
1. Proxecto educativo/dashboard → Minimalista Adri o Swiss Modern (ver style-presets.md)
2. Portfolio/editorial → Bold Signal, Soffia Warm, o Paper & Ink
3. Landing page expresiva → Creative Voltage, Electric Studio, o Dark Botanical
4. Documentacion tecnica → Terminal Green o Swiss Modern
5. Ejercicio interactivo → Pastel Geometry, Split Pastel, o Electric Studio
6. Literario/cultural → Vintage Editorial o Paper & Ink
7. Futurista/gaming → Neon Cyber o Creative Voltage

### Cargar fontes

```html
<!-- Minimo: Inter + Geist Mono -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">

<!-- Con display alternativa (Space Grotesk para headings) -->
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Cargar fontes de Fontshare

```html
<!-- Cabinet Grotesk (display) -->
<link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,700,500&display=swap" rel="stylesheet">

<!-- Clash Display (display) -->
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&display=swap" rel="stylesheet">

<!-- Satoshi (body) -->
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap" rel="stylesheet">

<!-- General Sans (body) -->
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600&display=swap" rel="stylesheet">

<!-- Excon (display — geométrica bold, impacto visual) -->
<link href="https://api.fontshare.com/v2/css?f[]=excon@700,800,900&display=swap" rel="stylesheet">

<!-- Alpino (display o body — versátil, moderna) -->
<link href="https://api.fontshare.com/v2/css?f[]=alpino@400,500,700&display=swap" rel="stylesheet">

<!-- Pally (body — redondeada, informal, amigable) -->
<link href="https://api.fontshare.com/v2/css?f[]=pally@400,500,700&display=swap" rel="stylesheet">
```

### Variables CSS de fuentes (placeholders, debe rellenarlos el preset activo)

```css
:root {
  /* PLACEHOLDERS — el preset activo redefine estos valores */
  --font-display: 'Satoshi', system-ui, sans-serif;     /* ejemplo: Bold Signal */
  --font-body: 'Inter', system-ui, sans-serif;          /* ejemplo: Bold Signal */
  --font-mono: 'Geist Mono', 'JetBrains Mono', monospace;
}
```

Cada preset (`style-presets.md`) declara su propia pareja explícita. Por ejemplo:
- **Bold Signal**: display Satoshi 900 + body Inter 300.
- **Paper & Ink**: display Instrument Serif + body Inter.
- **Swiss Modern**: display Switzer + body Inter.
- **Vintage Editorial**: display Playfair Display + body Public Sans.

NUNCA dejar `--font-display === --font-body` (single-font), salvo que el preset lo declare como decisión consciente.

## Escala tipografica fluida (ratio 1.25 — Major Third)

Basada en Utopia. Escala de 16px (min, viewport 400px) a 20px (max, viewport 1280px).
Ratio: 1.25 (Major Third) — equilibrio entre jerarquia clara e eficiencia vertical.

```css
:root {
  /* Escala tipografica fluida */
  --step--2: clamp(0.64rem, 0.59rem + 0.24vw, 0.80rem);   /* 10-13px Caption */
  --step--1: clamp(0.80rem, 0.74rem + 0.30vw, 1.00rem);   /* 13-16px Small */
  --step-0:  clamp(1.00rem, 0.93rem + 0.37vw, 1.25rem);   /* 16-20px Body */
  --step-1:  clamp(1.25rem, 1.16rem + 0.47vw, 1.56rem);   /* 20-25px H4 */
  --step-2:  clamp(1.56rem, 1.44rem + 0.61vw, 1.95rem);   /* 25-31px H3 */
  --step-3:  clamp(1.95rem, 1.79rem + 0.82vw, 2.44rem);   /* 31-39px H2 */
  --step-4:  clamp(2.44rem, 2.22rem + 1.10vw, 3.05rem);   /* 39-49px H1 */
  --step-5:  clamp(3.05rem, 2.76rem + 1.46vw, 3.81rem);   /* 49-61px Hero */
}
```

### Ratios alternativos

| Contexto | Ratio | Steps recomendados |
|----------|-------|-------------------|
| Dashboard denso | 1.125 (Major Second) | step-0 a step-3 |
| General (default) | 1.25 (Major Third) | step--2 a step-5 |
| Editorial/portfolio | 1.333 (Perfect Fourth) | step--1 a step-5 |

## Xerarquia tipografica (defaults v5.3 — favorecen pesos finos)

> **Cambio v5.3**: defaults rebajados a 300/400/500. **Nunca** subir a 600+ salvo que el preset lo justifique en su sección de `style-presets.md`. Justificación: weights medios/bold por defecto son tell IA-generado (audit Adri 2026-05-08).

| Elemento | Font | Size | Weight | Letter-spacing | Line-height |
|----------|------|------|--------|----------------|-------------|
| Hero | --font-display | --step-5 | 400-500 | -0.03em | 1.05 |
| H1 | --font-display | --step-4 | 400-500 | -0.02em | 1.1 |
| H2 | --font-display | --step-3 | 400-500 | -0.02em | 1.15 |
| H3 | --font-display | --step-2 | 400 | -0.01em | 1.2 |
| H4 | --font-display | --step-1 | 400 | normal | 1.25 |
| Body | --font-body | --step-0 | 300-400 | normal | 1.5 |
| Small | --font-body | --step--1 | 300-400 | normal | 1.45 |
| Caption | --font-body | --step--2 | 400 | 0.02em | 1.3 |
| Labels | --font-body | --step--2 | 500 | 0.1em (uppercase) | 1.2 |
| Data | --font-mono | --step-0 | 400 | normal | 1.3 |
| Code | --font-mono | --step--1 | 400 | normal | 1.5 |

**Excepciones legítimas** (presets que justifican weights altos):
- **Bold Signal** ★: display Satoshi 900 (impacto visual identidad). Body Inter 300.
- **Swiss Modern**: display Inter 700 (típica identidad swiss).
- **Exaggerated Minimalism**: display Inter 800-900 (es su seña).
- **Motion-Driven** / **Interactive Cursor**: pesos altos justificados por preset.

## Espazado fluido (Utopia)

O espazado escala co mesmo sistema que a tipografia:

```css
:root {
  --space-3xs: clamp(0.25rem, 0.23rem + 0.12vw, 0.31rem);
  --space-2xs: clamp(0.50rem, 0.46rem + 0.19vw, 0.63rem);
  --space-xs:  clamp(0.75rem, 0.70rem + 0.25vw, 0.94rem);
  --space-s:   clamp(1.00rem, 0.93rem + 0.37vw, 1.25rem);
  --space-m:   clamp(1.50rem, 1.39rem + 0.56vw, 1.88rem);
  --space-l:   clamp(2.00rem, 1.85rem + 0.74vw, 2.50rem);
  --space-xl:  clamp(3.00rem, 2.78rem + 1.11vw, 3.75rem);
  --space-2xl: clamp(4.00rem, 3.70rem + 1.48vw, 5.00rem);
}
```

## Datos e dashboards

Para calificaciones, metricas e táboas:

```css
.data-value, .grade, .metric {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-feature-settings: "tnum" 1;
}
```

## Tipografia premium (dark mode)

Reglas adicionales para temas oscuros de calidad profesional:

| Propiedad | Valor dark | Valor light | Razon |
|-----------|-----------|-------------|-------|
| Body color | #E8E8E8 | #1a1a1a | Off-white reduce fatiga visual |
| Title color | #FFFFFF | #1a1a1a | Maximo contraste solo en headings |
| font-weight body | 400 (regular) | 400 | En dark, regular parece medium |
| font-weight display | 500-600 | 600-700 | Reducir un nivel en dark |
| letter-spacing titles | -0.04em | -0.03em | Tighter en dark por glow optico |
| letter-spacing uppercase | +0.08em | +0.08em | Igual en ambos |
| line-height display | 1.05 | 1.05 | Consistente |
| line-height body | 1.55 | 1.5 | Ligeramente mas en dark |

**Variables recomendadas:**
```css
:root {
  --lh-display: 1.05;
  --lh-body: 1.55;
  --ls-tight: -0.04em;   /* titulos grandes */
  --ls-normal: normal;    /* body text */
  --ls-wide: 0.08em;      /* uppercase labels */
}
```

## Regras

- **Always** usar a escala fluida (--step-*) para tamaños, non valores fixos
- **Always** usar los roles tipográficos que declara el preset; en single-font,
  display y body comparten familia intencionadamente.
- **Always** usar tabular-nums para datos numéricos comparables; una familia mono
  es opcional si el preset conserva legibilidad.
- **Always** manter lonxitude de liña entre 45-90 caracteres (optimo: 65ch)
- **Always** usar marxes asimetricos en headings: mais espazo arriba que abaixo
- **Always** usar font-display: swap ao cargar fontes web
- **Always** respetar `fonts.single_font` y las familias del preset canónico
- **Always** verificar que `--font-display` y `--font-body` provienen del preset activo, no del default IA-genérico
- **Never** usar Inter como única fuente salvo que el preset declare
  `single_font=true`
- **Never** usar font-weight > 500 por defecto. Solo > 500 si el preset activo lo justifica explícitamente (Bold Signal, Swiss Modern, Exaggerated Minimalism)
- **Never** usar cursiva para enfase con sans-serif — usar negrita
- **Never** combinar espazo entre parrafos E sangria — elexir un
- **Consider** letter-spacing negativo (-0.02em) solo en titulos grandes (>step-3)
- **Consider** letter-spacing positivo (0.1em) solo en labels uppercase
- **Consider** ratio 1.125 para dashboards densos, 1.333 para editorial
- **Consider** weight 300 en body para presets con énfasis editorial/literario (Paper & Ink, Vintage Editorial)

## Checklist

- [ ] Fontes cargadas con display=swap
- [ ] Escala fluida con --step-* (non px fixos)
- [ ] Line-length non supera 90ch en ningun bloque
- [ ] Body usa line-height 1.5
- [ ] Titulos usan line-height 1.05-1.25
- [ ] Datos numericos con font-mono + tabular-nums
- [ ] Pareja o single-font coincide con `references/presets.json`
- [ ] Fuentes provienen del preset activo (declarado en `style-presets.md`), NO del default Inter
- [ ] Font-weight default ≤ 500 salvo justificación documentada en preset (Bold Signal, Swiss Modern, etc.)
- [ ] Inter solo es fuente única si el preset declara `single_font=true`
