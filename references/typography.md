# Tipografia

Fuentes: Butterick (principios), Utopia (escala fluida), Vercel Geist (tokens compostos).
Principio: a tipografia e a base do deseño; se a tipografia falla, todo falla.

## Sistema de fontes (font pairing)

Tres roles tipograficos, cada un con fallback:

| Rol | Fonte por defecto | Alternativas | Uso |
|-----|------------------|-------------|-----|
| Display/Headings | Inter 600 | Cabinet Grotesk, Clash Display, Excon, Alpino, Space Grotesk, Plus Jakarta Sans, Instrument Serif, Playfair Display, Cormorant Garamond, Orbitron, DM Sans, Newsreader | Titulos, heroes, headings |
| Body/Copy | Inter 400-500 | DM Sans, Satoshi, Switzer, Alpino, Pally, Lora, Source Serif 4, General Sans | Texto corrido, parrafos |
| Mono/Data | Geist Mono | JetBrains Mono, Fira Code | Dashboards, codigo, tabular-nums |

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

### Variables CSS de fuentes

```css
:root {
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'Geist Mono', 'JetBrains Mono', monospace;
}
```

Para cambiar a Space Grotesk en headings:
```css
:root {
  --font-display: 'Space Grotesk', system-ui, sans-serif;
}
```

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

## Xerarquia tipografica

| Elemento | Font | Size | Weight | Letter-spacing | Line-height |
|----------|------|------|--------|----------------|-------------|
| Hero | --font-display | --step-5 | 600 | -0.03em | 1.05 |
| H1 | --font-display | --step-4 | 600 | -0.02em | 1.1 |
| H2 | --font-display | --step-3 | 600 | -0.02em | 1.15 |
| H3 | --font-display | --step-2 | 500 | -0.01em | 1.2 |
| H4 | --font-display | --step-1 | 500 | normal | 1.25 |
| Body | --font-body | --step-0 | 400 | normal | 1.5 |
| Small | --font-body | --step--1 | 400 | normal | 1.45 |
| Caption | --font-body | --step--2 | 500 | 0.02em | 1.3 |
| Labels | --font-body | --step--2 | 500 | 0.1em (uppercase) | 1.2 |
| Data | --font-mono | --step-0 | 400 | normal | 1.3 |
| Code | --font-mono | --step--1 | 400 | normal | 1.5 |

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
- **Always** usar --font-display para headings e --font-body para corpo
- **Always** usar --font-mono con tabular-nums para datos numericos
- **Always** manter lonxitude de liña entre 45-90 caracteres (optimo: 65ch)
- **Always** usar marxes asimetricos en headings: mais espazo arriba que abaixo
- **Always** usar font-display: swap ao cargar fontes web
- **Never** usar font-weight > 600 (excepto se --font-display soporta 700)
- **Never** usar cursiva para enfase con sans-serif — usar negrita
- **Never** combinar espazo entre parrafos E sangria — elexir un
- **Consider** letter-spacing negativo (-0.02em) solo en titulos grandes (>step-3)
- **Consider** letter-spacing positivo (0.1em) solo en labels uppercase
- **Consider** ratio 1.125 para dashboards densos, 1.333 para editorial

## Checklist

- [ ] Fontes cargadas con display=swap
- [ ] Escala fluida con --step-* (non px fixos)
- [ ] Line-length non supera 90ch en ningun bloque
- [ ] Body usa line-height 1.5
- [ ] Titulos usan line-height 1.05-1.25
- [ ] Datos numericos con font-mono + tabular-nums
- [ ] Font-weight maximo 600 (ou 700 so para display alternativo)
