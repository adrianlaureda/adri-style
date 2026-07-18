# Style Presets — Visual Reference for Web Projects

27 ready-to-use visual presets. Each includes a complete `:root` CSS variables block, font pairing, and `<link>` tags. Designed for copy-paste by AI subagents building web pages, dashboards, and educational tools.

**v5.2 (2026-04-14):** 10 new presets added after the moodboard pre-selection workflow (#18–#27). Animation rules relaxed in `SKILL.md` — physical-property animations and longer durations are now allowed when the preset explicitly documents them. A **Modifiers** section at the end of this file documents overlays that can be applied on top of any preset.

**v5.4 (2026-05-08):** auditados los 27 presets uno a uno tras audit Impeccable + Codex (24 anti-patterns en 5 sites reales). Cada preset declara ahora: pareja display/body explícita, weights máximos permitidos para body y para display, justificación si single-font o si weight>500 default, estado (`activo` / `revisión-30d` candidato a eliminar si no aparece en outputs reales). Ver tabla "Audit v5.4 — Reglas de fuentes y pesos por preset" abajo. Bootstrap canónico en `templates/bootstrap-adri.html` parte de Bold Signal y carga directamente todos los tokens.

**v5.6 (2026-05-08 noche):** mirror programático en `references/presets.json` (schema 1.0). Esta tabla sigue siendo la fuente humana canónica; el JSON es derivado para que `audit-adri.sh` y futuras herramientas (slider `Font variation`, validadores externos) lo consuman sin parsear markdown. **Si modificas un preset, edita primero esta tabla y replica en el JSON inmediatamente.** Las dos fuentes deben mantenerse sincronizadas hasta que en v6 (breaking) el JSON se vuelva canónico obligatorio.

---

## Quick Reference Table

| # | Name | Mood | Background | Accent | Display Font | Body Font |
|---|------|------|------------|--------|-------------|-----------|
| 1 | Bold Signal ★ | **Default Adri** — marca personal | `#f8f8f8` (light default) | `#0a0a0a` | Satoshi 900 | Inter 300 |
| 2 | Electric Studio | Professional tech | `#0a1628` | `#3b82f6` | Geist 800 | Inter |
| 3 | Creative Voltage | Retro-modern | `#1a0a2e` | `#f59e0b` | Clash Display | Satoshi |
| 4 | Dark Botanical | Elegant organic | `#0a0f0a` | `#4ade80` | Cormorant Garamond | DM Sans |
| 5 | Notebook Tabs | Editorial paper | `#f5f0e8` | `#2563eb` | Newsreader | Source Serif 4 |
| 6 | Pastel Geometry | Friendly pastel | `#fef7f4` | `#e07850` | Satoshi 700 | Inter |
| 7 | Split Pastel | Juicy bicolor | `#fff1f2` | `#e11d48` | Space Grotesk | Inter |
| 8 | Vintage Editorial | Literary cálido | `#faf8f5` | `#8B2E1F` | Playfair Display | Public Sans |
| 9 | Neon Cyber | Futuristic neon | `#030712` | `#06ffa5` | Orbitron | Inter |
| 10 | Terminal Green | Developer | `#0a0a0a` | `#22c55e` | JetBrains Mono | JetBrains Mono |
| 11 | Swiss Modern | Corporate precise | `#ffffff` | `#000000` | Switzer 900 | Inter |
| 12 | Paper & Ink | Literary reflective | `#1c1917` | `#d4a574` | Instrument Serif | Inter |
| 13 | Minimalista Adri | Educational default | `#050505` | multi-section | Geist 700 | Inter |
| 14 | Soffia Warm | Warm premium | `hsl(220 15% 8%)` | `#c9a96e` | Satoshi 900 | Inter |
| 15 | Signal Hardware | Monochrome industrial | `#050505` | `#f04d23` | Space Grotesk | Space Mono |
| 16 | Magazine Editorial | Revista densa multi-col | `#fafaf9` | `#C1272D` | Fraunces | Source Serif 4 |
| 17 | Cinematic Story | Narrativa inmersiva | `hsl(220 30% 6%)` | `#F59E0B` | Bricolage Grotesque | Public Sans |
| 18 | Storytelling-Driven | Narrativa por capítulos | `#faf5ed` | `#D97706` | Literata | Inter |
| 19 | E-Ink Paper | Lectura calmada mate | `#fdfbf7` | `#1A1A1A` | Literata | Inter |
| 20 | Exaggerated Minimalism | Tipografía gigante + 1 acento | `#FFFFFF` | `#FF3B30` | Archivo Black | Inter |
| 21 | Bento Grids | Modular Apple-style | `#F5F5F7` | `#1D1D1F` | Inter 700 | Inter |
| 22 | Zero Interface | Minimal ambiental | `#FAFAFA` | `hsl(220 10% 40%)` | Inter Light 200 | Inter |
| 23 | Neumorphism | Soft UI playful | `#E0E5EC` | `#5E72E4` | Nunito 800 | Nunito |
| 24 | Motion-Driven | Animaciones coreografiadas | `#0A0A0A` | `#22C55E` | Inter 800 | Inter |
| 25 | Micro-interactions | Feedback sutil | `#FFFFFF` | `#22C55E` | Inter 700 | Inter |
| 26 | AI-Native UI | Chat-first conversacional | `#0A0A0F` | `#6366F1` | Inter 700 | Inter |
| 27 | Interactive Cursor | Cursor-centric portfolio | `#FAFAFA` | `#5E6AD2` | Inter 800 | Inter |

---

## Audit v5.4 — Reglas de fuentes y pesos por preset

Tabla canónica generada el 2026-05-08 tras la auditoría manual de los 27 presets. Resuelve la queja v5.3: cada preset DEBE declarar explícitamente qué fuentes acepta, en qué rango de peso y por qué se desvía de los defaults `300-500`.

**Columnas:**
- **Display / Body**: las fuentes oficiales del preset. Si dice "—" en body es porque comparte familia con display (single-font justificado).
- **Display weights** y **Body weights**: rango permitido para esa familia en ese preset. Cualquier output que use un peso fuera de este rango incumple el preset.
- **Single-font**: ¿display y body son la misma familia? Si `SÍ → justificado`, está documentado y permitido. Si `NO`, va contra `typography.md` v5.3 y bloquea audit.
- **Body default >500**: ¿el body por defecto excede el límite v5.3 (300-500)? Si `SÍ`, debe haber justificación; si no, hay que rebajar.
- **Modo default**: light o dark según el preset; el otro está disponible vía `[data-theme]`.
- **Caso aula real**: ¿Adri lo ha usado en un output verificado? Vacío o `revisión-30d` → candidato a eliminar si no aparece en 30 días.
- **Estado**: `activo` (ok), `activo-frágil` (acepta uso pero requiere observación), `revisión-30d` (candidato a eliminar tras Codex B1).

| # | Preset | Display | Body | Display weights | Body weights | Single-font? | Body >500 default? | Modo default | Caso aula real | Estado |
|---|--------|---------|------|-----------------|--------------|---------------|---------------------|---------------|------------------|--------|
| 1 | Bold Signal ★ | Satoshi | Inter | 500 (.t-overline) · 900 (display+section+h2) | 300 (body) · 400 (utility) | NO | NO — body 300 | light | brandbook live, formacion-xograr, planificacion-4eso, adri-react | activo |
| 2 | Electric Studio | Geist | Inter | 300-800 (display) | 400-600 | NO | NO — body 400 | dark | parcial (formacion-xograr v0) | activo |
| 3 | Creative Voltage | Clash Display | Satoshi | 500-700 | 400-700 (default 400) | NO | NO — body 400 | dark | (sin uso real verificado) | revisión-30d |
| 4 | Dark Botanical | Cormorant Garamond | DM Sans | 400 · 600 · 700 (display) | 100-1000 var (default 400) | NO | NO — body 400 | dark | (sin uso real verificado) | revisión-30d |
| 5 | Notebook Tabs | Newsreader | Source Serif 4 | 400 · 600 · 700 (italic 400) | 400 · 600 (italic 400) | NO (dos serif distintas) | NO — body 400 | light | (lectura prolongada, casos hipotéticos) | activo-frágil |
| 6 | Pastel Geometry | Satoshi | Inter | 300-700 | 400-600 (default 400) | NO | NO — body 400 | light | quizzes/forms alumnos | activo |
| 7 | Split Pastel | Space Grotesk | Inter | 400-700 | 400-600 | NO | NO — body 400 | light | (eventos/workshops, sin uso verificado) | revisión-30d |
| 8 | Vintage Editorial | Playfair Display | Public Sans | 400-900 var | 100-900 var (default 400) | NO (display serif + body sans humanist) | NO — body 400 | light | Día das Letras 2026 (ámbito objetivo) | activo |
| 9 | Neon Cyber | Orbitron | Inter | 400 · 600 · 700 · 800 | 400-600 | NO | NO — body 400 | dark | (programación/cyber, sin uso verificado) | revisión-30d |
| 10 | Terminal Green | JetBrains Mono | JetBrains Mono | 400-700 | 400-700 (default 400) | **SÍ — JUSTIFICADO** (autenticidad terminal: la fuente *es* el lenguaje) | NO — body 400 | dark | (docs CLI, sin uso aula verificado) | activo-frágil |
| 11 | Swiss Modern | Switzer | Inter | 700-900 (display típico swiss) | 400-700 | NO | NO — body 400 | light | (reports densos, sin uso verificado) | revisión-30d |
| 12 | Paper & Ink | Instrument Serif | Inter | 400 (italic 400) — *única weight disponible en la fuente* | 100-900 var (default 400) | NO (serif + sans) | NO — body 400 | dark | reading log/journal (uso personal) | activo |
| 13 | Minimalista Adri | Geist | Inter | 300-700 | 400-800 (default 400) | NO | NO — body 400 | dark | dashboards calificaciones, materiales clase | activo |
| 14 | Soffia Warm | Satoshi | Inter | 300-900 | 400-600 (default 400) | NO | NO — body 400 | dark | (premium edu, casos hipotéticos) | activo-frágil |
| 15 | Signal Hardware | Space Grotesk | Space Mono | 400-700 | 400-700 (default 400) | NO (sans + mono) | NO — body 400 | dark | dashboards agentes (cora), tooling | activo |
| 16 | Magazine Editorial | Fraunces | Source Serif 4 | 100-900 var (drop-cap usa 900) | 200-900 var (default 400) | NO (dos serifs con registros distintos) | NO — body 400 | light | dossiers literarios (Día das Letras, longreads) | activo |
| 17 | Cinematic Story | Bricolage Grotesque | Public Sans | 200-800 var (chapter-num usa 200 italic) | 100-900 var (default 400) | NO | NO — body 400 | dark | unidades narrativas (Odisea, Quijote — uso planificado) | activo |
| 18 | Storytelling-Driven | Literata | Inter | 200-900 var (chapter-num 300 italic) | 100-900 var (default 400) | NO (serif + sans) | NO — body 400 | light | unidades arco narrativo (Generación 27, planificadas) | activo |
| 19 | E-Ink Paper | Literata | Inter | 200-900 var (h2/h3 italic 700) | 100-900 var (default 400) | NO (serif + sans) | NO — body 400 | light | guías de lectura, antologías, B/N imprimible | activo |
| 20 | Exaggerated Minimalism | Archivo Black | Inter | 400 (única weight disponible — Archivo Black ya es black) | 100-900 var (eyebrow 300) | NO | NO — body 400 | light | portadas/intro slides | activo |
| 21 | Bento Grids | Inter | Inter | 700 (display) | 400-500 (default 400) | **SÍ — JUSTIFICADO** (sistema Apple-style usa una sola family — Inter sustituye a SF Pro) | NO — body 400 | light | dashboards educativos (KPI hero + métricas) | activo |
| 22 | Zero Interface | Inter | Inter | 200 (display Light) | 200-400 (default 400) | **SÍ — JUSTIFICADO** (interfaz invisible: la fuente desaparece) | NO — body 200-400 | light | splash/pausas pedagógicas (uso planificado) | activo-frágil |
| 23 | Neumorphism | Nunito | Nunito | 800 (display) | 600-700 forced para contraste WCAG | **SÍ — JUSTIFICADO** (rounded sans coherente con vibe blando) | **SÍ — JUSTIFICADO** (peso 600+ obligatorio para legibilidad sobre fondo plomizo `#E0E5EC`; documentado en components.md) | light | material primaria/calculadoras (hipotético) | revisión-30d |
| 24 | Motion-Driven | Inter | Inter | 800 (display Black) | 400-500 | **SÍ — JUSTIFICADO** (el wow es la animación, no la tipografía) | NO — body 400 | dark | trailers unidades (sin uso verificado) | revisión-30d |
| 25 | Micro-interactions | Inter | Inter | 700 (display) | 400-600 (default 600 en btn) | **SÍ — JUSTIFICADO** (Linear/Notion-style, sistema único) | NO — body 400 default | light | quizzes con feedback inmediato | activo |
| 26 | AI-Native UI | Inter | Inter | 700 (display) | 400-500 | **SÍ — JUSTIFICADO** (Claude/ChatGPT/Perplexity usan Inter Display + Inter Text; coherente con producto chat) | NO — body 400 | dark | tutor IA (uso planificado) | activo-frágil |
| 27 | Interactive Cursor | Inter | Inter | 800 (display Black) | 400-500 | **SÍ — JUSTIFICADO** (portfolio premium tipo Linear/Vercel) | NO — body 400 | light | (portfolios, sin uso verificado) | revisión-30d |

**Lectura de la tabla:**

- 7 presets `activo` con uso verificado: 1 ★, 2 (parcial), 6, 8, 12, 13, 15, 16, 17, 18, 19, 20, 21, 25.
- 6 presets `activo-frágil` (admitidos pero sin pruebas): 5, 10, 14, 22, 26 — observar 30 días tras v5.4.
- 8 presets `revisión-30d` candidatos a eliminar si no aparecen en outputs reales tras 2026-06-08: 3, 4, 7, 9, 11, 23, 24, 27.

**Reglas operativas (post-audit):**

- Cualquier output nuevo DEBE arrancar de `templates/bootstrap-adri.html` (Bold Signal por defecto) y declarar el preset elegido en un comentario `<!-- preset: NN-name -->` al inicio.
- Si un output usa pesos fuera del rango declarado para su preset, `audit-adri.sh` debe detectarlo (todo > 500 en body, single-font sin "JUSTIFICADO" en `style-presets.md`).
- Los 8 presets `revisión-30d` no se eliminan ahora; se vuelve a auditar el 2026-06-08. Si no han aparecido en `~/Proyectos/Claude/`, se mueven a `references/_archive/style-presets-deprecated.md` y se rebaja a 19 el catálogo activo.

---

## Layout Patterns por Preset (OBLIGATORIO)

Cada preset tiene layouts prescritos para evitar el patrón genérico "todo centrado en columna estrecha". Usar al menos 2 de los patrones indicados.

| Preset | Layout primario | Layout secundario | Evitar |
|--------|----------------|-------------------|--------|
| Bold Signal | Full-width hero + asymmetric split (60/40) | Spotlight card (1 grande + 2 pequeñas) | Grid simétrico 3 columnas |
| Electric Studio | Sidebar nav + main content area | Bento grid (2x2 irregular) | Todo centrado sin sidebar |
| Creative Voltage | Overlapping sections + diagonal breaks | Masonry grid | Columna única lineal |
| Dark Botanical | Wide image + text wrap | Alternating left/right split sections | Cards uniformes en grid |
| Notebook Tabs | Tabbed content + prose column | Side-by-side comparison | Full-width sections |
| Pastel Geometry | Bento grid (mixed sizes) + floated callouts | Zigzag (text-left/image-right alternating) | 3 cards iguales en fila |
| Split Pastel | 50/50 split hero + stacked cards | Offset grid (items desplazados) | Todo alineado a izquierda |
| Vintage Editorial | 2-column editorial (main + margin notes) | Pull quotes + dropcaps | Grid moderno |
| Neon Cyber | Terminal-style stacked panels + sidebar stats | Full-width data dashboard | Layouts suaves/redondeados |
| Terminal Green | Single-column monospace + code blocks | Horizontal stat bar + log output | Grids visuales elaborados |
| Swiss Modern | Strict grid (12-col) + generous whitespace | Horizontal rules as section dividers | Decoración visual excesiva |
| Paper & Ink | Prose column (65ch) + marginal annotations | Blockquotes + horizontal dividers | Layouts anchos/dashboard |
| Minimalista Adri | Dashboard grid (sidebar + cards) | Spotlight KPI (1 big + 3 small) | Todo flotante sin estructura |
| Soffia Warm | Asymmetric hero (70/30) + warm card grid | Feature section with icon-left + text-right | Grid frío/mecánico |
| Signal Hardware | Dashboard instrumental + panel lateral | Tarjetas técnicas apiladas + métricas segmentadas | Composición editorial cálida |
| Magazine Editorial | Multi-columna (2-3 cols) con drop cap inicial + pull quotes full-width | Hero a sangre + article body en 2 cols + margen de notas | Dashboard, grids de cards uniformes |
| Cinematic Story | Capítulos full-viewport con número decorativo gigante + parallax sticky | Hero full-bleed + scroll narrativo + pinned nav | Grid de cards sin arco narrativo |
| Storytelling-Driven | Capítulos secuenciales con acento variable por sección + hero ilustrado | Timeline vertical con marcadores de capítulo + eyebrow romano | Grid uniforme sin narrativa, dashboards |
| E-Ink Paper | Prose de 1 columna (65ch) + textura de papel sutil + dot grid opcional | Reading view con table of contents lateral | Colores vibrantes, gradientes, sombras fuertes |
| Exaggerated Minimalism | Hero con palabra gigante (>20vw) + 1 acento puntual | Split 70/30 con tipografía invadiendo el espacio | Grids 3-col uniformes, densidad de información |
| Bento Grids | Grid asimétrico modular (3-4 cards de tamaños mixtos) + spotlight 2x1 | Card-grande + 3 pequeñas con jerarquía Apple-style | Full-width sections sin modularidad |
| Zero Interface | Contenido centrado + ambient gradient muy sutil + 1-2 elementos max por vista | Voice-visual con waveform y listening cues | Densidad de información, grids complejos |
| Neumorphism | Cards flotantes con doble sombra + botones extruidos + contraste alto controlado | Dashboard soft UI con widgets redondeados | Contraste bajo WCAG fallido, texto sin borde |
| Motion-Driven | Hero con animación de entrada coreografiada + scroll-triggered keyframes + transiciones sección-a-sección | Parallax vertical con elementos que entran desde diferentes lados | Todo estático, grids sin vida |
| Micro-interactions | Grid compacto con feedback sutil (hover, pulse, ripple) + respuestas animadas | Form/quiz con validación visual inmediata | Feedback tardío, sin estados visibles |
| AI-Native UI | Chat layout con sidebar de historial + mensajes alternados user/assistant + shimmer on stream | Split content-main + panel lateral de contexto | Grids frios sin conversación, dashboards tradicionales |
| Interactive Cursor | Hero centrado + cursor custom que reacciona al hover + magnetic elements | Portfolio asimétrico donde el cursor revela info | Todo con cursor default, sin punteros custom |

---

## 1. Bold Signal ★ (Default Adri)

**Marca personal de Adri por antonomasia.** Cuerpo Inter 300 (fina), Satoshi 900 para display, ángulos rectos (`--radius: 0`), paleta neutra blanco/negro/grises con 6 acentos opcionales por dominio. Light por defecto, dark via `[data-theme="dark"]`. Validado en producción en `formacion-xograr`, `planificacion-4eso`, `adri-react` y el brandbook live (https://branding-adri.adrianlaureda.workers.dev/).

**Cuándo usarlo (default por antonomasia):**
- Cualquier comunicación firmada por Adri (presentaciones, charlas, portfolio, landing)
- Material educativo donde la marca personal debe ser visible
- Contexto ambiguo / no claramente educativo-funcional → usar este por defecto
- Como tokens compartidos en proyectos React/HTML del ecosistema Adri

**Cuándo NO** (presets contextuales mantienen prioridad):
- Dashboard de calificaciones → **Minimalista Adri** (colores semánticos verde/amarillo/rojo)
- Quiz interactivo para alumnos → **Pastel Geometry** o **Split Pastel**
- Documento largo de lectura → **Paper & Ink** o **Notebook Tabs**

**Font loading:**
```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

> Alternativa: importar `tokens.css` directo del repo brandbook (Inter self-hosted variable + Satoshi via Fontshare). Ver `references/identity-adri.md`.

**CSS variables (light default):**
```css
:root {
  /* Fonts */
  --font-display: 'Satoshi', system-ui, -apple-system, sans-serif;
  --font-body:    'Inter', system-ui, -apple-system, sans-serif;
  --font-mono:    'JetBrains Mono', 'SF Mono', Menlo, monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds (light por defecto) */
  --bg:          #f8f8f8;
  --bg-surface:  #ffffff;
  --bg-elevated: #efefef;

  /* Borders */
  --border: hsl(0 0% 0% / 0.10);

  /* Text */
  --text:           #0a0a0a;
  --text-secondary: hsl(0 0% 0% / 0.60);
  --text-muted:     hsl(0 0% 0% / 0.35);

  /* Accent — negro como acento neutro por defecto */
  --accent:         #0a0a0a;
  --accent-surface: hsl(0 0% 0% / 0.06);

  /* Semánticos */
  --success: #16a34a;
  --warning: #ca8a04;
  --danger:  #dc2626;
  --info:    #2563eb;

  /* Geometría */
  --radius:      0px;
  --radius-pill: 999px;
  --maxw:        1200px;

  /* Movimiento */
  --transition:      200ms;
  --transition-slow: 400ms;
  --ease-out:        cubic-bezier(0.16, 1, 0.3, 1);    /* expo out */
  --ease-out-back:   cubic-bezier(0.34, 1.56, 0.64, 1);/* overshoot suave */
  --ease-in-out:     cubic-bezier(0.65, 0, 0.35, 1);
}

[data-theme="dark"] {
  --bg:             #050505;
  --bg-surface:     #0e0e0e;
  --bg-elevated:    #161616;
  --border:         hsl(0 0% 100% / 0.10);
  --text:           #ffffff;
  --text-secondary: hsl(0 0% 100% / 0.70);
  --text-muted:     hsl(0 0% 100% / 0.40);
  --accent:         #ffffff;
  --accent-surface: hsl(0 0% 100% / 0.06);
  --success: #22c55e;
  --warning: #eab308;
  --danger:  #f87171;
  --info:    #60a5fa;
}
```

**Body styles obligatorios** (cuerpo fino — discrepancia explícita con Inter default):
```css
body {
  font-family: var(--font-body);
  font-size: 1rem;
  font-weight: 300;          /* CRÍTICO — Inter Light, no 400 */
  line-height: var(--lh-body);
  color: var(--text);
  background: var(--bg);
}
```

**6 acentos opcionales por dominio** (toggle vía `<body class="accent-X">`):
```css
.accent-azul    { --accent: #3b82f6; --accent-surface: hsl(217 91% 60% / 0.10); }
.accent-violeta { --accent: #a78bfa; --accent-surface: hsl(258 90% 76% / 0.12); }
.accent-verde   { --accent: #22c55e; --accent-surface: hsl(142 71% 45% / 0.10); }
.accent-naranja { --accent: #f97316; --accent-surface: hsl(24 95% 53% / 0.10);  }
.accent-cyan    { --accent: #06b6d4; --accent-surface: hsl(189 94% 43% / 0.10); }
.accent-rosa    { --accent: #f43f5e; --accent-surface: hsl(349 89% 60% / 0.10); }
```

**5 utilidades tipográficas reutilizables:**
```css
.t-overline {
  font-family: var(--font-display); font-weight: 500;
  font-size: 0.7rem; letter-spacing: 0.25em; text-transform: uppercase;
  color: var(--text-muted);
}
.t-section {
  font-family: var(--font-display); font-weight: 900;
  font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--text-secondary);
}
.t-display {
  font-family: var(--font-display); font-weight: 900;
  font-size: clamp(2.5rem, 6vw, 5rem); line-height: 0.95;
  letter-spacing: -0.03em;
}
.t-h2 {
  font-family: var(--font-display); font-weight: 900;
  font-size: clamp(1.5rem, 3vw, 2.25rem); line-height: 1.1;
  letter-spacing: -0.02em;
}
.t-mono { font-family: var(--font-mono); font-size: 0.85rem; }
```

---

## 2. Electric Studio

Azul nocturno profesional con acento azul eléctrico. Transmite competencia técnica sin agresividad. La opción segura para proyectos de tecnología, SaaS o herramientas educativas digitales.

**Ideal for:**
- Tech product landing pages
- SaaS dashboards
- Educational tools and platforms
- Developer documentation sites

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;700;800&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Geist', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #0a1628;
  --bg-surface:  #101e35;
  --bg-elevated: #162540;

  /* Borders */
  --border: hsl(215 50% 50% / 0.15);

  /* Text */
  --text:           #e8edf5;
  --text-secondary: hsl(215 20% 75%);
  --text-muted:     hsl(215 15% 50%);

  /* Accent */
  --accent:         #3b82f6;
  --accent-surface: hsl(217 91% 60% / 0.12);

  /* Utilities */
  --radius:     8px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f0f5ff;
  --bg-surface:  #ffffff;
  --bg-elevated: #e8f0fe;
  --border:      hsl(217 50% 60% / 0.2);
  --text:           #1a1a2e;
  --text-secondary: hsl(220 15% 40%);
  --text-muted:     hsl(220 10% 60%);
  --accent:         #2563eb;
  --accent-surface: hsl(221 83% 53% / 0.08);
}
```

---

## 3. Creative Voltage

Púrpura profundo con ámbar dorado. Energía retro-futurista, entre póster de concierto y estudio creativo de los 90. Para proyectos que necesitan personalidad sin perder legibilidad.

**Ideal for:**
- Creative portfolios
- Music or arts projects
- Workshop or event landing pages
- Youth-oriented educational content

**Font loading:**
```html
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&f[]=satoshi@400,500,700&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Clash Display', 'Helvetica Neue', sans-serif;
  --font-body:    'Satoshi', 'Inter', sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #1a0a2e;
  --bg-surface:  #22103a;
  --bg-elevated: #2a1645;

  /* Borders */
  --border: hsl(270 50% 60% / 0.15);

  /* Text */
  --text:           #f0eaf8;
  --text-secondary: hsl(270 20% 70%);
  --text-muted:     hsl(270 15% 50%);

  /* Accent */
  --accent:         #f59e0b;
  --accent-surface: hsl(38 92% 50% / 0.12);

  /* Utilities */
  --radius:     4px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #fdfaf0;
  --bg-surface:  #ffffff;
  --bg-elevated: #fef9e7;
  --border:      hsl(38 50% 50% / 0.2);
  --text:           #1a1005;
  --text-secondary: hsl(35 15% 40%);
  --text-muted:     hsl(35 10% 60%);
  --accent:         #d97706;
  --accent-surface: hsl(38 92% 50% / 0.08);
}
```

---

## 4. Dark Botanical

Verde mineral sobre negro orgánico. Sobriedad editorial con un toque de naturaleza. La tipografía serif Cormorant le da altura literaria; el verde jade lo ancla en lo natural.

**Ideal for:**
- Nature or science educational content
- Literary or essay-style web pages
- Environmental project microsites
- Long-form reading experiences

**Font loading (self-host vía Fontsource — descargar woff2 a `fonts/`):**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/cormorant-garamond@latest/files/cormorant-garamond-latin-400-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/cormorant-garamond@latest/files/cormorant-garamond-latin-600-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/cormorant-garamond@latest/files/cormorant-garamond-latin-700-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/cormorant-garamond@latest/files/cormorant-garamond-latin-400-italic.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/dm-sans@latest/files/dm-sans-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/dm-sans@latest/files/dm-sans-latin-ext-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Cormorant Garamond'; font-style: normal; font-weight: 400; font-display: swap; src: url('fonts/cormorant-garamond-latin-400-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Cormorant Garamond'; font-style: normal; font-weight: 600; font-display: swap; src: url('fonts/cormorant-garamond-latin-600-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Cormorant Garamond'; font-style: normal; font-weight: 700; font-display: swap; src: url('fonts/cormorant-garamond-latin-700-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Cormorant Garamond'; font-style: italic; font-weight: 400; font-display: swap; src: url('fonts/cormorant-garamond-latin-400-italic.woff2') format('woff2'); }
  @font-face {
    font-family: 'DM Sans';
    font-style: normal;
    font-display: swap;
    font-weight: 100 1000;
    src: url('fonts/dm-sans-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  @font-face {
    font-family: 'DM Sans';
    font-style: normal;
    font-display: swap;
    font-weight: 100 1000;
    src: url('fonts/dm-sans-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
</style>
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Cormorant Garamond', 'Georgia', serif;
  --font-body:    'DM Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #0a0f0a;
  --bg-surface:  #101610;
  --bg-elevated: #161e16;

  /* Borders */
  --border: hsl(130 20% 40% / 0.15);

  /* Text */
  --text:           #e8f0e8;
  --text-secondary: hsl(130 10% 65%);
  --text-muted:     hsl(130 8% 45%);

  /* Accent */
  --accent:         #4ade80;
  --accent-surface: hsl(142 69% 58% / 0.1);

  /* Utilities */
  --radius:     6px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f0f5f0;
  --bg-surface:  #ffffff;
  --bg-elevated: #e8f0e8;
  --border:      hsl(130 20% 40% / 0.15);
  --text:           #0f1a0f;
  --text-secondary: hsl(130 10% 35%);
  --text-muted:     hsl(130 8% 55%);
  --accent:         #16a34a;
  --accent-surface: hsl(142 72% 29% / 0.08);
}
```

---

## 5. Notebook Tabs

Crema de papel con tinta azul. Evoca el cuaderno académico, la anotación a mano, el material de estudio bien impreso. El preset más cómodo para lectura prolongada.

**Ideal for:**
- Educational handouts and study materials
- Reading comprehension exercises
- Literary analysis pages
- Any content meant to be read, not skimmed

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Newsreader', 'Georgia', serif;
  --font-body:    'Source Serif 4', 'Georgia', serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #f5f0e8;
  --bg-surface:  #faf7f2;
  --bg-elevated: #ffffff;

  /* Borders */
  --border: hsl(35 30% 60% / 0.3);

  /* Text */
  --text:           #1a1a1a;
  --text-secondary: hsl(35 10% 35%);
  --text-muted:     hsl(35 8% 55%);

  /* Accent */
  --accent:         #2563eb;
  --accent-surface: hsl(221 83% 53% / 0.08);

  /* Utilities */
  --radius:     4px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="dark"] {
  --bg:          #1a1710;
  --bg-surface:  #211e16;
  --bg-elevated: #28241c;
  --border:      hsl(40 15% 50% / 0.15);
  --text:           #e8e2d4;
  --text-secondary: hsl(40 10% 60%);
  --text-muted:     hsl(40 8% 45%);
  --accent:         #60a5fa;
  --accent-surface: hsl(213 94% 68% / 0.1);
}
```

---

## 6. Pastel Geometry

Melocotón claro con coral cálido. Amigable, moderno y ligeramente lúdico sin caer en infantil. Funciona muy bien para herramientas interactivas y formularios.

**Ideal for:**
- Interactive educational tools and quizzes
- Student-facing web apps
- Friendly forms and surveys
- Project management boards

**Font loading:**
```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Satoshi', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #fef7f4;
  --bg-surface:  #ffffff;
  --bg-elevated: #fef0ea;

  /* Borders */
  --border: hsl(15 50% 60% / 0.2);

  /* Text */
  --text:           #1a1a1a;
  --text-secondary: hsl(15 10% 40%);
  --text-muted:     hsl(15 8% 60%);

  /* Accent */
  --accent:         #e07850;
  --accent-surface: hsl(15 70% 60% / 0.08);

  /* Utilities */
  --radius:     10px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="dark"] {
  --bg:          #1a0f0a;
  --bg-surface:  #251610;
  --bg-elevated: #2e1c14;
  --border:      hsl(15 40% 50% / 0.15);
  --text:           #f5ece8;
  --text-secondary: hsl(15 15% 68%);
  --text-muted:     hsl(15 10% 50%);
  --accent:         #f09070;
  --accent-surface: hsl(15 74% 68% / 0.12);
}
```

---

## 7. Split Pastel

Rosa muy claro con rojo carmesí intenso. Contraste llamativo dentro de una paleta luminosa. La tensión entre lo suave y lo vibrante genera energía visual inmediata.

**Ideal for:**
- Event or workshop pages
- Attention-grabbing announcements
- Youth content or campaigns
- Headers and hero sections that need to pop

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Space Grotesk', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #fff1f2;
  --bg-surface:  #ffffff;
  --bg-elevated: #ffe4e6;

  /* Borders */
  --border: hsl(351 80% 60% / 0.2);

  /* Text */
  --text:           #1a1a1a;
  --text-secondary: hsl(350 10% 40%);
  --text-muted:     hsl(350 8% 60%);

  /* Accent */
  --accent:         #e11d48;
  --accent-surface: hsl(347 77% 50% / 0.08);

  /* Utilities */
  --radius:     8px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="dark"] {
  --bg:          #200a10;
  --bg-surface:  #2a1018;
  --bg-elevated: #33151f;
  --border:      hsl(347 40% 50% / 0.15);
  --text:           #fce8ec;
  --text-secondary: hsl(347 15% 65%);
  --text-muted:     hsl(347 10% 48%);
  --accent:         #fb7185;
  --accent-surface: hsl(351 95% 71% / 0.1);
}
```

---

## 8. Vintage Editorial

Crema cálido con granate editorial. Playfair Display variable como display + Public Sans humanista como body — el contraste serif/sans hace la página más legible que el "todo serif" clásico, sin perder el aire de revista cultural. Para webs de autor literario, recursos de literatura/lengua, contextos culturales con peso.

**Ideal for:**
- Author landing pages and literary tributes (Día das Letras, homenajes)
- Book club, reading list and book project pages
- Cultural or historical educational materials
- Long-form essays where readability matters

**Font loading (self-host vía Fontsource — descargar woff2 a `fonts/`):**
```bash
# desde la raíz del proyecto
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/playfair-display@latest/files/playfair-display-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/playfair-display@latest/files/playfair-display-latin-ext-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/playfair-display@latest/files/playfair-display-latin-wght-italic.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/public-sans@latest/files/public-sans-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/public-sans@latest/files/public-sans-latin-ext-wght-normal.woff2
```

```html
<style>
  @font-face {
    font-family: 'Playfair Display';
    font-style: normal;
    font-display: swap;
    font-weight: 400 900;
    src: url('fonts/playfair-display-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  @font-face {
    font-family: 'Playfair Display';
    font-style: normal;
    font-display: swap;
    font-weight: 400 900;
    src: url('fonts/playfair-display-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
  @font-face {
    font-family: 'Playfair Display';
    font-style: italic;
    font-display: swap;
    font-weight: 400 900;
    src: url('fonts/playfair-display-latin-wght-italic.woff2') format('woff2');
  }
  @font-face {
    font-family: 'Public Sans';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/public-sans-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  @font-face {
    font-family: 'Public Sans';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/public-sans-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
</style>
```

**Body alternativo (serif clásico Lora):** si el proyecto pide vibe "libro impreso" puro (no homenaje contemporáneo), sustituye el `@font-face` de Public Sans por Lora desde `@fontsource-variable/lora` y cambia `--font-body` a `'Lora', 'Georgia', serif`. Útil en logs de lectura, journals, materiales históricos.

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Playfair Display', 'Georgia', serif;
  --font-body:    'Public Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.65;

  /* Backgrounds */
  --bg:          #faf8f5;
  --bg-surface:  #ffffff;
  --bg-elevated: #f3ede3;

  /* Borders */
  --border: hsl(30 30% 60% / 0.25);

  /* Text */
  --text:           #1a1a1a;
  --text-secondary: hsl(30 10% 35%);
  --text-muted:     hsl(30 8% 55%);

  /* Accent — granate editorial vivo */
  --accent:         #8B2E1F;
  --accent-soft:    #C9986A;
  --accent-surface: hsl(10 65% 33% / 0.08);

  /* Utilities */
  --radius:     3px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="dark"] {
  --bg:          #1a1510;
  --bg-surface:  #221c15;
  --bg-elevated: #2a231c;
  --border:      hsl(30 15% 45% / 0.2);
  --text:           #e8e0d0;
  --text-secondary: hsl(35 12% 60%);
  --text-muted:     hsl(35 8% 45%);
  --accent:         #C44A38;
  --accent-soft:    #D4B08C;
  --accent-surface: hsl(10 55% 50% / 0.1);
}
```

---

## 9. Neon Cyber

Negro casi puro con verde neón fosforescente. Cyberpunk funcional — no decorativo. La luminosidad del acento garantiza legibilidad incluso sobre fondos muy oscuros.

**Ideal for:**
- Programming and technology content
- Cybersecurity or digital literacy topics
- Gamified learning interfaces
- Night-mode default tools

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Orbitron', 'Courier New', monospace;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #030712;
  --bg-surface:  #0a0f1a;
  --bg-elevated: #111827;

  /* Borders */
  --border: hsl(160 90% 50% / 0.15);

  /* Text */
  --text:           #e8f4e8;
  --text-secondary: hsl(160 15% 60%);
  --text-muted:     hsl(160 10% 40%);

  /* Accent */
  --accent:         #06ffa5;
  --accent-surface: hsl(160 100% 51% / 0.08);

  /* Utilities */
  --radius:     4px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f0faf5;
  --bg-surface:  #ffffff;
  --bg-elevated: #e0f7ee;
  --border:      hsl(160 40% 40% / 0.2);
  --text:           #0a1a12;
  --text-secondary: hsl(160 10% 35%);
  --text-muted:     hsl(160 8% 55%);
  --accent:         #059669;
  --accent-surface: hsl(161 94% 30% / 0.08);
}
```

---

## 10. Terminal Green

Monocromo de terminal. Todo en JetBrains Mono — el código y el texto son el mismo gesto. Para herramientas de desarrollador, logs y cualquier cosa que viva en la CLI.

**Ideal for:**
- Developer tools and CLI documentation
- Code-heavy educational content
- Terminal emulators or log viewers
- Programming exercises and challenges

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts — same family for everything, intentional */
  --font-display: 'JetBrains Mono', 'Courier New', monospace;
  --font-body:    'JetBrains Mono', 'Courier New', monospace;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #0a0a0a;
  --bg-surface:  #121212;
  --bg-elevated: #1a1a1a;

  /* Borders */
  --border: hsl(120 60% 40% / 0.2);

  /* Text */
  --text:           #e8e8e8;
  --text-secondary: hsl(120 10% 60%);
  --text-muted:     hsl(120 8% 40%);

  /* Accent */
  --accent:         #22c55e;
  --accent-surface: hsl(142 71% 45% / 0.1);

  /* Utilities */
  --radius:     2px;
  --transition: 150ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f5faf5;
  --bg-surface:  #ffffff;
  --bg-elevated: #edf7ed;
  --border:      hsl(120 30% 50% / 0.25);
  --text:           #0a1a0a;
  --text-secondary: hsl(120 10% 35%);
  --text-muted:     hsl(120 8% 55%);
  --accent:         #16a34a;
  --accent-surface: hsl(142 76% 36% / 0.08);
}
```

---

## 11. Swiss Modern

Blanco absoluto con negro absoluto. La única excepción a la regla anti-negro: aquí el contraste máximo es la intención. Grid preciso, sin ornamento, tipografía como estructura.

**Ideal for:**
- Corporate or institutional presentations
- Data-dense reports and tables
- Print-first layouts converted to web
- When the client demands "clean and professional"

**Font loading:**
```html
<link href="https://api.fontshare.com/v2/css?f[]=switzer@100,300,400,500,700,900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Switzer', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #ffffff;
  --bg-surface:  #f8f8f8;
  --bg-elevated: #f0f0f0;

  /* Borders — very subtle tinted gray, not pure */
  --border: hsl(220 5% 85%);

  /* Text */
  --text:           #1a1a1a;
  --text-secondary: hsl(220 5% 40%);
  --text-muted:     hsl(220 4% 60%);

  /* Accent — black, by design */
  --accent:         #0a0a0a;
  --accent-surface: hsl(220 5% 5% / 0.06);

  /* Utilities */
  --radius:     0px;
  --transition: 150ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="dark"] {
  --bg:          #111214;
  --bg-surface:  #18191c;
  --bg-elevated: #1f2023;
  --border:      hsl(220 5% 100% / 0.1);
  --text:           #e8e8e8;
  --text-secondary: hsl(220 5% 65%);
  --text-muted:     hsl(220 4% 45%);
  --accent:         #ffffff;
  --accent-surface: hsl(0 0% 100% / 0.06);
}
```

---

## 12. Paper & Ink

Tostado oscuro como papel craft con oro envejecido. Calidez literaria sin cursilería. La Instrument Serif tiene una elegancia contemporánea que diferencia este preset del editorial clásico.

**Ideal for:**
- Personal writing and reflection tools
- Literary journals and book projects
- Reading logs and annotation interfaces
- Any context where warmth matters more than precision

**Font loading (self-host vía Fontsource — descargar woff2 a `fonts/`):**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/instrument-serif@latest/files/instrument-serif-latin-400-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/instrument-serif@latest/files/instrument-serif-latin-400-italic.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-ext-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Instrument Serif'; font-style: normal; font-weight: 400; font-display: swap; src: url('fonts/instrument-serif-latin-400-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Instrument Serif'; font-style: italic; font-weight: 400; font-display: swap; src: url('fonts/instrument-serif-latin-400-italic.woff2') format('woff2'); }
  @font-face {
    font-family: 'Inter';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  }
  @font-face {
    font-family: 'Inter';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/inter-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  }
</style>
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Instrument Serif', 'Georgia', serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #1c1917;
  --bg-surface:  #252220;
  --bg-elevated: #2e2b28;

  /* Borders */
  --border: hsl(25 15% 50% / 0.15);

  /* Text */
  --text:           #e8e0d4;
  --text-secondary: hsl(30 12% 62%);
  --text-muted:     hsl(30 8% 45%);

  /* Accent */
  --accent:         #d4a574;
  --accent-surface: hsl(30 52% 65% / 0.1);

  /* Utilities */
  --radius:     6px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #faf7f2;
  --bg-surface:  #ffffff;
  --bg-elevated: #f3ede3;
  --border:      hsl(30 25% 60% / 0.25);
  --text:           #1a1a1a;
  --text-secondary: hsl(30 10% 38%);
  --text-muted:     hsl(30 8% 58%);
  --accent:         #b5793a;
  --accent-surface: hsl(30 52% 47% / 0.08);
}
```

---

## 13. Minimalista Adri

Negro profundo con acentos cambiantes por sección. El preset por defecto para material educativo de Adri: Inter limpio, espaciado generoso, y un acento diferente por bloque temático para orientar visualmente al estudiante.

**Ideal for:**
- Educational handouts and class materials
- Multi-topic lesson pages
- Student-facing study tools
- Any Adri project where no other preset fits

**Color palette per section:**
- `#3b82f6` — blue (introduction, theory)
- `#10b981` — green (practice, exercises)
- `#f59e0b` — amber (warnings, important notes)
- `#ef4444` — red (errors, common mistakes)
- `#8b5cf6` — purple (extension, advanced content)

**Usage:** Set `--accent` to the section color on each `<section>` element:
```css
section.practica { --accent: #10b981; }
section.importante { --accent: #f59e0b; }
```

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Geist', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #050505;
  --bg-surface:  #0e0e0e;
  --bg-elevated: #161616;

  /* Borders */
  --border: hsl(220 10% 50% / 0.12);

  /* Text */
  --text:           #e8e8e8;
  --text-secondary: hsl(220 5% 65%);
  --text-muted:     hsl(220 5% 45%);

  /* Accent — default blue; override per section */
  --accent:         #3b82f6;
  --accent-surface: hsl(217 91% 60% / 0.1);

  /* Section accent palette (apply via data attributes or class overrides) */
  --accent-blue:    #3b82f6;
  --accent-green:   #10b981;
  --accent-amber:   #f59e0b;
  --accent-red:     #ef4444;
  --accent-purple:  #8b5cf6;

  /* Utilities */
  --radius:     6px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f8f9fa;
  --bg-surface:  #ffffff;
  --bg-elevated: #f0f2f5;
  --border:      hsl(220 10% 50% / 0.15);
  --text:           #1a1a1a;
  --text-secondary: hsl(220 5% 38%);
  --text-muted:     hsl(220 5% 58%);
  --accent:         #2563eb;
  --accent-surface: hsl(221 83% 53% / 0.08);
}
```

---

## 14. Soffia Warm

Azul marino oscuro y cálido — no frío — con dorado bronce. Equilibrio entre profesional y acogedor. El nombre y la paleta evocan una noche de verano con buena compañía.

**Ideal for:**
- Premium educational platforms
- Personal brand pages
- Portfolio and professional bio sites
- Any project that needs warmth without losing credibility

**Font loading:**
```html
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Satoshi', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds — warm blue-tinted darks */
  --bg:          hsl(220 15% 8%);
  --bg-surface:  hsl(220 14% 11%);
  --bg-elevated: hsl(220 13% 14%);

  /* Borders */
  --border: hsl(220 15% 50% / 0.14);

  /* Text */
  --text:           hsl(40 20% 92%);
  --text-secondary: hsl(35 10% 65%);
  --text-muted:     hsl(35 8% 45%);

  /* Accent */
  --accent:         #c9a96e;
  --accent-surface: hsl(38 48% 61% / 0.1);

  /* Utilities */
  --radius:     8px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          hsl(40 30% 97%);
  --bg-surface:  #ffffff;
  --bg-elevated: hsl(40 25% 93%);
  --border:      hsl(35 20% 60% / 0.25);
  --text:           #1a1a1a;
  --text-secondary: hsl(35 10% 38%);
  --text-muted:     hsl(35 8% 58%);
  --accent:         #a07840;
  --accent-surface: hsl(32 45% 44% / 0.08);
}
```

---

## 15. Signal Hardware

Monocromo industrial con un único acento naranja de sistema. Inspirado en interfaces tipo Nothing: jerarquía agresiva, paneles instrumentales y detalles mecánicos. No es un preset generalista; funciona mejor en tooling, dashboards de agentes y UIs de monitorización.

**Ideal for:**
- Agent dashboards
- Internal tools and control panels
- Monitoring interfaces
- Experimental CLI/web hybrids

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Space Grotesk', system-ui, sans-serif;
  --font-body:    'Space Mono', 'JetBrains Mono', monospace;
  --font-mono:    'Space Mono', 'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 0.98;
  --lh-body:    1.6;

  /* Backgrounds */
  --bg:          #050505;
  --bg-surface:  #0d0d0d;
  --bg-elevated: #141414;

  /* Borders */
  --border: hsl(0 0% 100% / 0.12);

  /* Text */
  --text:           #f5f5f0;
  --text-secondary: hsl(48 7% 70%);
  --text-muted:     hsl(48 5% 50%);

  /* Accent */
  --accent:         #f04d23;
  --accent-surface: hsl(12 87% 54% / 0.12);

  /* Utilities */
  --radius:     0px;
  --transition: 180ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f2f1ec;
  --bg-surface:  #ffffff;
  --bg-elevated: #e9e7e0;
  --border:      hsl(0 0% 0% / 0.1);
  --text:           #111111;
  --text-secondary: hsl(30 6% 34%);
  --text-muted:     hsl(30 5% 54%);
  --accent:         #cc3d18;
  --accent-surface: hsl(13 79% 45% / 0.08);
}
```

---

## 16. Magazine Editorial

Rejilla multi-columna con drop caps, pull quotes y peso tipográfico fuerte. Fraunces Variable como display + Source Serif 4 como body — los dos son serif pero con registro distinto (display cinematográfico vs body de lectura densa). Vibe The New Yorker / Pitchfork / Granta. Para dossiers literarios, longreads, materiales curriculares largos donde Vintage Editorial (1 columna) se queda corto.

**Ideal for:**
- Dossiers literarios y unidades didácticas de lectura larga
- Artículos académicos y ensayos educativos
- Revista digital de departamento o de centro
- Homenajes culturales densos (biografía + análisis + timeline)

**Font loading (self-host vía Fontsource — descargar woff2 a `fonts/`):**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/fraunces@latest/files/fraunces-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/fraunces@latest/files/fraunces-latin-ext-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/fraunces@latest/files/fraunces-latin-wght-italic.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/source-serif-4@latest/files/source-serif-4-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/source-serif-4@latest/files/source-serif-4-latin-ext-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono@latest/files/jetbrains-mono-latin-wght-normal.woff2
```

```html
<style>
  @font-face {
    font-family: 'Fraunces';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/fraunces-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122;
  }
  @font-face {
    font-family: 'Fraunces';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/fraunces-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+2C60-2C7F, U+A720-A7FF;
  }
  @font-face {
    font-family: 'Fraunces';
    font-style: italic;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/fraunces-latin-wght-italic.woff2') format('woff2');
  }
  @font-face {
    font-family: 'Source Serif 4';
    font-style: normal;
    font-display: swap;
    font-weight: 200 900;
    src: url('fonts/source-serif-4-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122;
  }
  @font-face {
    font-family: 'Source Serif 4';
    font-style: normal;
    font-display: swap;
    font-weight: 200 900;
    src: url('fonts/source-serif-4-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+2C60-2C7F, U+A720-A7FF;
  }
  @font-face {
    font-family: 'JetBrains Mono';
    font-style: normal;
    font-display: swap;
    font-weight: 100 800;
    src: url('fonts/jetbrains-mono-latin-wght-normal.woff2') format('woff2');
  }
</style>
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Fraunces', 'Georgia', serif;
  --font-body:    'Source Serif 4', 'Georgia', serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.0;
  --lh-body:    1.7;

  /* Backgrounds */
  --bg:          #fafaf9;
  --bg-surface:  #ffffff;
  --bg-elevated: #f5f5f4;

  /* Borders */
  --border: hsl(0 0% 20% / 0.15);

  /* Text */
  --text:           #0c0a09;
  --text-secondary: hsl(20 10% 30%);
  --text-muted:     hsl(20 8% 50%);

  /* Accent — rojo editorial magazine */
  --accent:         #C1272D;
  --accent-soft:    #78716C;
  --accent-surface: hsl(358 65% 46% / 0.08);

  /* Editorial specifics (característica del preset) */
  --col-count:      2;
  --col-gap:        2.5rem;
  --drop-cap-size:  4.5em;
  --pull-quote-size: 1.8em;

  /* Utilities */
  --radius:     2px;
  --transition: 250ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="dark"] {
  --bg:          #1a1917;
  --bg-surface:  #242321;
  --bg-elevated: #2d2c2a;
  --border:      hsl(30 10% 60% / 0.18);
  --text:           #f5f5f4;
  --text-secondary: hsl(30 8% 72%);
  --text-muted:     hsl(30 6% 52%);
  --accent:         #E11D48;
  --accent-soft:    #A8A29E;
  --accent-surface: hsl(347 77% 50% / 0.12);
}
```

**Editorial patterns (técnicas de firma del preset):**
```css
.article-body {
  column-count: var(--col-count);
  column-gap: var(--col-gap);
  font-family: var(--font-body);
  font-size: var(--step-0);
  line-height: var(--lh-body);
}
.article-body > p:first-of-type::first-letter {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: var(--drop-cap-size);
  float: left;
  line-height: 0.85;
  padding: 0.1em 0.1em 0 0;
  color: var(--accent);
}
.pull-quote {
  font-family: var(--font-display);
  font-style: italic;
  font-weight: 300;
  font-size: var(--pull-quote-size);
  line-height: 1.25;
  color: var(--text);
  border-left: 3px solid var(--accent);
  padding-left: 1.5rem;
  margin: 2rem 0;
  column-span: all;
}
@media (max-width: 768px) {
  .article-body { column-count: 1; }
}
```

---

## 17. Cinematic Story

Full-bleed hero + capítulos numerados gigantes (scroll narrativo) + parallax vertical suave. Bricolage Grotesque Variable como display moderno + Public Sans como body legible. Paleta cinemática deep blue con acento dorado. Vibe Apple Event pages / The Verge feature / longreads de Pitchfork. Para cursos con narrativa fuerte, unidades didácticas que quieres "contar" no solo "listar".

**Ideal for:**
- Unidades didácticas narrativas (Odisea, Quijote, guerra civil, etc.)
- Cursos inmersivos con arco narrativo (hero → acto 1 → acto 2 → cierre)
- Landings de charla/conferencia con storytelling
- Case studies educativos y reportajes

**Font loading (self-host vía Fontsource — descargar woff2 a `fonts/`):**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/bricolage-grotesque@latest/files/bricolage-grotesque-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/bricolage-grotesque@latest/files/bricolage-grotesque-latin-ext-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/public-sans@latest/files/public-sans-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/public-sans@latest/files/public-sans-latin-ext-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono@latest/files/jetbrains-mono-latin-wght-normal.woff2
```

```html
<style>
  @font-face {
    font-family: 'Bricolage Grotesque';
    font-style: normal;
    font-display: swap;
    font-weight: 200 800;
    src: url('fonts/bricolage-grotesque-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122;
  }
  @font-face {
    font-family: 'Bricolage Grotesque';
    font-style: normal;
    font-display: swap;
    font-weight: 200 800;
    src: url('fonts/bricolage-grotesque-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+2C60-2C7F, U+A720-A7FF;
  }
  @font-face {
    font-family: 'Public Sans';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/public-sans-latin-wght-normal.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122;
  }
  @font-face {
    font-family: 'Public Sans';
    font-style: normal;
    font-display: swap;
    font-weight: 100 900;
    src: url('fonts/public-sans-latin-ext-wght-normal.woff2') format('woff2');
    unicode-range: U+0100-02AF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+2C60-2C7F, U+A720-A7FF;
  }
  @font-face {
    font-family: 'JetBrains Mono';
    font-style: normal;
    font-display: swap;
    font-weight: 100 800;
    src: url('fonts/jetbrains-mono-latin-wght-normal.woff2') format('woff2');
  }
</style>
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-body:    'Public Sans', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 0.95;
  --lh-body:    1.65;

  /* Backgrounds — deep cinematic blue/black */
  --bg:          hsl(220 30% 6%);
  --bg-surface:  hsl(220 28% 10%);
  --bg-elevated: hsl(220 25% 14%);

  /* Borders */
  --border: hsl(220 30% 50% / 0.18);

  /* Text */
  --text:           #f5f3ea;
  --text-secondary: hsl(220 15% 72%);
  --text-muted:     hsl(220 10% 52%);

  /* Accent — amber gold cinemático */
  --accent:         #F59E0B;
  --accent-soft:    #FCD34D;
  --accent-surface: hsl(38 92% 50% / 0.1);

  /* Parallax / storytelling specifics */
  --section-height:    100vh;
  --chapter-num-size:  clamp(120px, 22vw, 320px);
  --parallax-speed-bg: 0.3;
  --parallax-speed-mid: 0.6;

  /* Utilities */
  --radius:     8px;
  --transition: 300ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f8f6f0;
  --bg-surface:  #ffffff;
  --bg-elevated: #efebdf;
  --border:      hsl(40 20% 50% / 0.18);
  --text:           #1a1812;
  --text-secondary: hsl(40 12% 28%);
  --text-muted:     hsl(40 8% 50%);
  --accent:         #B45309;
  --accent-soft:    #D97706;
  --accent-surface: hsl(30 80% 45% / 0.08);
}
```

**Storytelling patterns:**
```css
.chapter {
  min-height: var(--section-height);
  display: grid;
  place-items: center;
  position: relative;
  padding: clamp(60px, 10vw, 160px) clamp(24px, 5vw, 80px);
}
.chapter-number {
  font-family: var(--font-display);
  font-weight: 200;
  font-size: var(--chapter-num-size);
  line-height: 0.85;
  color: var(--accent);
  opacity: 0.15;
  position: absolute;
  top: 8%;
  right: 5%;
  pointer-events: none;
  user-select: none;
}
.chapter-content {
  max-width: 65ch;
  position: relative;
  z-index: 1;
}
.parallax-bg {
  position: sticky;
  top: 0;
  transform: translateY(calc(var(--scroll) * var(--parallax-speed-bg)));
  will-change: transform;
}
```

**Nota de implementación:** el parallax real requiere JS mínimo (IntersectionObserver + CSS custom property `--scroll`). No uses librerías externas — la técnica cabe en 20 líneas.

---

## 18. Storytelling-Driven

Capítulos secuenciales con acento variable por sección — cada sección tiene su propio `--accent` dentro del mismo sistema de tinted warm creams, así el lector percibe progresión emocional. Literata Variable (serif literaria recién salida de Google Fonts) como display + Inter como body. Vibe: New York Times Magazine / Longreads / Aeon essays. Ideal cuando quieres que la unidad didáctica *se sienta* como un relato, no como una ficha.

**Ideal for:**
- Unidades didácticas con arco narrativo por capítulos (Odisea, Quijote, 98, Generación del 27)
- Biografías y semblanzas de autores
- Dossiers temáticos con secciones emocionalmente distintas
- Charlas largas con progresión dramática

**Font loading (self-host vía Fontsource):**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/literata@latest/files/literata-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono@latest/files/jetbrains-mono-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Literata'; font-style: normal; font-display: swap; font-weight: 200 900;
    src: url('fonts/literata-latin-wght-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
  @font-face { font-family: 'JetBrains Mono'; font-style: normal; font-display: swap; font-weight: 100 800;
    src: url('fonts/jetbrains-mono-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Literata', 'Georgia', serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.65;

  /* Backgrounds — warm creams */
  --bg:          #faf5ed;
  --bg-surface:  #fffaf0;
  --bg-elevated: #f1ead9;

  /* Borders */
  --border: hsl(30 20% 30% / 0.18);

  /* Text */
  --text:           #1a1410;
  --text-secondary: hsl(25 12% 28%);
  --text-muted:     hsl(25 10% 50%);

  /* Accent base — ámbar cálido */
  --accent:         #D97706;
  --accent-soft:    #F59E0B;
  --accent-surface: hsl(32 95% 44% / 0.09);

  /* Acentos por sección (cambian el tono emocional) */
  --accent-ch-1:    #78350F;  /* apertura · barro seco */
  --accent-ch-2:    #D97706;  /* desarrollo · ámbar */
  --accent-ch-3:    #9F1239;  /* clímax · granate */
  --accent-ch-4:    #1E3A5F;  /* reflexión · azul nocturno */
  --accent-ch-5:    #14532D;  /* cierre · verde profundo */

  /* Storytelling specifics */
  --chapter-num-size: clamp(72px, 10vw, 160px);
  --timeline-gap:     clamp(80px, 12vw, 160px);

  /* Utilities */
  --radius:     6px;
  --transition: 450ms;
  --ease-story: cubic-bezier(0.22, 1, 0.36, 1);
}

[data-theme="dark"] {
  --bg:          #1a150f;
  --bg-surface:  #22180f;
  --bg-elevated: #2b1f13;
  --border:      hsl(35 20% 55% / 0.18);
  --text:           #f5e9d6;
  --text-secondary: hsl(35 15% 72%);
  --text-muted:     hsl(35 10% 50%);
  --accent:         #F59E0B;
  --accent-soft:    #FBBF24;
  --accent-surface: hsl(38 92% 55% / 0.12);
}
```

**Storytelling patterns:**
```css
.chapter {
  padding-block: var(--timeline-gap);
  position: relative;
}
.chapter[data-ch="1"] { --accent: var(--accent-ch-1); }
.chapter[data-ch="2"] { --accent: var(--accent-ch-2); }
.chapter[data-ch="3"] { --accent: var(--accent-ch-3); }
.chapter[data-ch="4"] { --accent: var(--accent-ch-4); }
.chapter[data-ch="5"] { --accent: var(--accent-ch-5); }
.chapter-number {
  font-family: var(--font-display);
  font-weight: 300;
  font-style: italic;
  font-size: var(--chapter-num-size);
  color: var(--accent);
  line-height: 0.85;
  letter-spacing: -0.03em;
}
.chapter-eyebrow {
  font-family: var(--font-mono);
  font-size: var(--step--1);
  text-transform: uppercase;
  letter-spacing: 0.22em;
  color: var(--accent);
  border-left: 2px solid var(--accent);
  padding-left: 0.8rem;
  margin-bottom: 0.8rem;
}
.chapter-body { max-width: 65ch; font-family: var(--font-body); }
.chapter-entry {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity var(--transition) var(--ease-story),
              transform var(--transition) var(--ease-story);
}
.chapter-entry.visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  .chapter-entry { opacity: 1; transform: none; transition: none; }
}
```

**Animation policy (excepción documentada):** este preset usa transitions de 450ms para las entradas scroll-triggered — superior a los 300ms por defecto — porque el ritmo narrativo pide más lentitud. El JS mínimo es un `IntersectionObserver` que añade `.visible` a los `.chapter-entry` al entrar en viewport.

---

## 19. E-Ink / Paper

Papel electrónico literario. Off-white mate con dot grid muy sutil, Literata Italic como display (serif de lectura moderna), Inter como body. Cero color, cero sombras, cero gradientes — solo contraste de peso y jerarquía. Vibe: Kindle Paperwhite / Instapaper / The Browser. Para documentos largos donde lo que importa es que el lector no note la interfaz.

**Ideal for:**
- Guías de lectura y comentarios de texto largos
- Antologías y colecciones de poemas
- Apuntes editables densos en prose
- Dossiers para imprimir (el diseño aguanta la impresión en B/N)

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/literata@latest/files/literata-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Literata'; font-style: normal; font-display: swap; font-weight: 200 900;
    src: url('fonts/literata-latin-wght-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Literata', 'Georgia', serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 1.15;
  --lh-body:    1.7;

  --bg:          #fdfbf7;
  --bg-surface:  #ffffff;
  --bg-elevated: #f5f3ed;

  --border: hsl(30 10% 20% / 0.16);

  --text:           #1a1a1a;
  --text-secondary: hsl(20 5% 28%);
  --text-muted:     hsl(20 5% 48%);

  --accent:         #1a1a1a;
  --accent-soft:    hsl(20 5% 35%);
  --accent-surface: hsl(20 5% 20% / 0.05);

  /* Paper specifics */
  --prose-width: 65ch;
  --dot-size:    14px;

  --radius:     2px;
  --transition: 200ms;
}

[data-theme="dark"] {
  --bg:          #15130f;
  --bg-surface:  #1c1a16;
  --bg-elevated: #23211d;
  --border:      hsl(30 8% 60% / 0.2);
  --text:           #e8e4d8;
  --text-secondary: hsl(35 8% 72%);
  --text-muted:     hsl(35 6% 48%);
  --accent:         #e8e4d8;
}
```

**Paper patterns:**
```css
body {
  background-color: var(--bg);
  background-image: radial-gradient(circle at 1px 1px, hsl(20 5% 20% / 0.06) 1px, transparent 0);
  background-size: var(--dot-size) var(--dot-size);
}
.prose {
  max-width: var(--prose-width);
  margin-inline: auto;
  font-family: var(--font-body);
  font-size: var(--step-0);
  line-height: var(--lh-body);
  padding-block: clamp(60px, 10vw, 120px);
}
.prose h1, .prose h2, .prose h3 {
  font-family: var(--font-display);
  font-style: italic;
  font-weight: 700;
  line-height: var(--lh-display);
  text-wrap: balance;
}
.prose h2 { margin-top: 2.2em; margin-bottom: 0.6em; }
.prose blockquote {
  border-left: 2px solid var(--text);
  padding-left: 1.2rem;
  margin-block: 1.6em;
  font-style: italic;
  color: var(--text-secondary);
}
```

---

## 20. Exaggerated Minimalism

Tipografía gigante que invade el viewport + un único acento puntual vibrante. Archivo Black (grotesk condensado ultra-negro) como display + Inter como body minimal. Blanco casi total. Vibe: Loud minimal / agencias de diseño de portfolio / The Pudding / fashion editorial. Cuando quieres que una palabra *sea* el hero.

**Ideal for:**
- Landing de sección / título de unidad didáctica con una sola palabra clave
- Portadas de examen o dossier con impacto tipográfico
- Citas destacadas tamaño display
- Secciones intro de presentaciones HTML

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource/archivo-black@latest/files/archivo-black-latin-400-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Archivo Black'; font-style: normal; font-display: swap; font-weight: 400;
    src: url('fonts/archivo-black-latin-400-normal.woff2') format('woff2'); }
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Archivo Black', 'Helvetica Neue', sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 0.82;
  --lh-body:    1.5;

  --bg:          #ffffff;
  --bg-surface:  #fafafa;
  --bg-elevated: #f4f4f4;

  --border: hsl(0 0% 0% / 0.12);

  --text:           #000000;
  --text-secondary: hsl(0 0% 25%);
  --text-muted:     hsl(0 0% 50%);

  --accent:         #FF3B30;
  --accent-soft:    #FF6B60;
  --accent-surface: hsl(4 100% 59% / 0.08);

  /* Display specifics */
  --display-huge: clamp(72px, 20vw, 280px);

  --radius:     0;
  --transition: 180ms;
  --ease-snap:  cubic-bezier(0.34, 1.56, 0.64, 1);
}

[data-theme="dark"] {
  --bg:          #0a0a0a;
  --bg-surface:  #141414;
  --bg-elevated: #1c1c1c;
  --border:      hsl(0 0% 100% / 0.14);
  --text:           #ffffff;
  --text-secondary: hsl(0 0% 72%);
  --text-muted:     hsl(0 0% 50%);
  --accent:         #FF3B30;
}
```

**Exag patterns:**
```css
.hero-huge {
  font-family: var(--font-display);
  font-size: var(--display-huge);
  line-height: var(--lh-display);
  letter-spacing: -0.04em;
  text-transform: uppercase;
  color: var(--text);
  overflow: hidden;
  padding-inline: clamp(24px, 4vw, 80px);
}
.hero-huge .accent-word { color: var(--accent); }
.hero-huge-bleed {
  /* palabra que rebasa el viewport deliberadamente */
  white-space: nowrap;
  margin-inline: calc(-1 * clamp(24px, 4vw, 80px));
}
.eyebrow-min {
  font-family: var(--font-body);
  font-size: var(--step--1);
  font-weight: 300;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
}
```

---

## 21. Bento Grids

Grid modular asimétrico estilo Apple event — cards de tamaños mixtos con jerarquía clara (1 grande + 2–3 pequeñas). Inter 700 como display + Inter regular como body. Off-white `#f5f5f7` (el gris exacto de apple.com). Vibe: Apple Event / iPhone launch page / Linear changelog. Cuando quieres mostrar features con jerarquía visual sin caer en el grid 3-col clásico.

**Ideal for:**
- Landing de skill/herramienta con features destacadas
- Dashboards educativos con KPI hero + métricas secundarias
- Recap de unidad didáctica con spotlight + bullet points
- Portfolio de proyectos con jerarquía

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Inter', -apple-system, system-ui, sans-serif;
  --font-body:    'Inter', -apple-system, system-ui, sans-serif;
  --font-mono:    'SF Mono', 'JetBrains Mono', monospace;

  --lh-display: 1.05;
  --lh-body:    1.55;

  --bg:          #f5f5f7;
  --bg-surface:  #ffffff;
  --bg-elevated: #fafafa;

  --border: hsl(220 5% 20% / 0.08);

  --text:           #1d1d1f;
  --text-secondary: hsl(220 4% 28%);
  --text-muted:     hsl(220 4% 52%);

  --accent:         #1d1d1f;
  --accent-soft:    #515154;
  --accent-surface: hsl(220 5% 20% / 0.05);

  /* Bento specifics */
  --bento-gap:    clamp(14px, 1.5vw, 22px);
  --bento-radius: 22px;

  --radius:     var(--bento-radius);
  --transition: 220ms;
  --ease-apple: cubic-bezier(0.42, 0, 0.16, 1);
}

[data-theme="dark"] {
  --bg:          #0a0a0b;
  --bg-surface:  #17171a;
  --bg-elevated: #1f1f23;
  --border:      hsl(220 4% 72% / 0.12);
  --text:           #f5f5f7;
  --text-secondary: hsl(220 4% 78%);
  --text-muted:     hsl(220 4% 55%);
  --accent:         #f5f5f7;
}
```

**Bento patterns:**
```css
.bento {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  grid-template-rows: auto auto;
  gap: var(--bento-gap);
  max-width: 1100px;
  margin-inline: auto;
}
.bento-card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--bento-radius);
  padding: clamp(20px, 2.5vw, 36px);
  transition: transform var(--transition) var(--ease-apple),
              border-color var(--transition) var(--ease-apple);
}
.bento-card:hover {
  transform: translateY(-2px);
  border-color: hsl(220 5% 40% / 0.2);
}
.bento-card--hero {
  grid-column: 1 / 2;
  grid-row: 1 / 3;
  min-height: 420px;
}
.bento-card--wide {
  grid-column: 2 / 4;
}
@media (max-width: 900px) {
  .bento { grid-template-columns: 1fr 1fr; }
  .bento-card--hero { grid-column: 1 / 3; grid-row: auto; min-height: 280px; }
  .bento-card--wide { grid-column: 1 / 3; }
}
```

---

## 22. Zero Interface

UI invisible, ambient, voice-first / gesto-first. Inter 200 (light weight) como display — la tipografía desaparece en vez de declarar. Fondo cream `#FAFAFA` con gradient radial muy sutil, una única palabra o frase centrada, waveform decorativa como guiño al input de voz. Vibe: AirPods Pro launch / meditation apps / "interfaces invisibles" de Golden Krishna. Cuando menos *es* más.

**Ideal for:**
- Splash screens o intros de sesión interactiva
- Pantallas de "escuchando / procesando" en apps conversacionales
- Mensajes de bienvenida o despedida
- Pausas pedagógicas entre secciones densas

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 1.15;
  --lh-body:    1.65;

  --bg:          #FAFAFA;
  --bg-surface:  #ffffff;
  --bg-elevated: #f5f5f5;

  --border: hsl(220 8% 80% / 0.5);

  --text:           hsl(220 10% 18%);
  --text-secondary: hsl(220 8% 40%);
  --text-muted:     hsl(220 6% 60%);

  --accent:         hsl(220 10% 40%);
  --accent-soft:    hsl(220 8% 60%);
  --accent-surface: hsl(220 10% 40% / 0.06);

  /* Zero specifics */
  --ambient-gradient: radial-gradient(ellipse at 50% 50%, hsl(220 20% 95%) 0%, transparent 70%);

  --radius:     999px;
  --transition: 400ms;
  --ease-ambient: cubic-bezier(0.23, 1, 0.32, 1);
}

[data-theme="dark"] {
  --bg:          #0a0a0a;
  --bg-surface:  #131313;
  --bg-elevated: #1a1a1a;
  --border:      hsl(220 8% 30% / 0.5);
  --text:           hsl(220 10% 88%);
  --text-secondary: hsl(220 8% 68%);
  --text-muted:     hsl(220 6% 48%);
  --accent:         hsl(220 10% 75%);
  --ambient-gradient: radial-gradient(ellipse at 50% 50%, hsl(220 20% 12%) 0%, transparent 70%);
}
```

**Zero patterns:**
```css
.zero-screen {
  min-height: 100dvh;
  display: grid;
  place-items: center;
  background: var(--bg) var(--ambient-gradient);
  padding: clamp(32px, 6vw, 96px);
  text-align: center;
}
.zero-title {
  font-family: var(--font-display);
  font-weight: 200;
  font-size: clamp(32px, 5vw, 72px);
  letter-spacing: -0.03em;
  color: var(--text);
  max-width: 22ch;
  text-wrap: balance;
}
.zero-waveform {
  display: flex;
  align-items: center;
  gap: 4px;
  margin-top: 3rem;
  height: 40px;
}
.zero-waveform span {
  width: 4px;
  background: var(--accent);
  border-radius: 2px;
  opacity: 0.6;
  animation: zero-pulse 1.4s ease-in-out infinite;
}
.zero-waveform span:nth-child(1) { height: 40%; animation-delay: 0s; }
.zero-waveform span:nth-child(2) { height: 70%; animation-delay: 0.1s; }
.zero-waveform span:nth-child(3) { height: 100%; animation-delay: 0.2s; }
.zero-waveform span:nth-child(4) { height: 55%; animation-delay: 0.3s; }
.zero-waveform span:nth-child(5) { height: 85%; animation-delay: 0.4s; }
@keyframes zero-pulse {
  0%, 100% { transform: scaleY(0.5); }
  50%      { transform: scaleY(1); }
}
@media (prefers-reduced-motion: reduce) {
  .zero-waveform span { animation: none; transform: scaleY(0.7); }
}
```

**Animation policy (excepción documentada):** waveform decorativa con `animation` infinita — explicitamente permitida porque es *el* elemento de firma del preset. Respeta `prefers-reduced-motion`.

---

## 23. Neumorphism

Soft UI con doble sombra (light top-left, dark bottom-right) — el componente parece extruido del fondo. Nunito 800 (rounded sans bien alineado con el vibe blando) como display + Nunito regular como body. Fondo `#E0E5EC` (el neutral plomizo característico). **IMPORTANTE**: este preset es controvertido porque el contraste suele fallar WCAG. Esta versión se mantiene sólo en componentes gruesos (cards, botones, inputs chunky) y usa texto con contraste alto forzado; NO aplicar a body text small.

**Ideal for:**
- Material infantil/lúdico de primaria (textos cortos, botones grandes)
- Calculadoras didácticas y herramientas de operación
- Controles de audio (sliders, knobs) en apps musicales educativas
- Demos playful en talleres de programación

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/nunito@latest/files/nunito-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Nunito'; font-style: normal; font-display: swap; font-weight: 200 900;
    src: url('fonts/nunito-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Nunito', 'Avenir Next', system-ui, sans-serif;
  --font-body:    'Nunito', 'Avenir Next', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 1.1;
  --lh-body:    1.6;

  --bg:          #E0E5EC;
  --bg-surface:  #E0E5EC;
  --bg-elevated: #E8EDF5;

  --border: transparent; /* se sustituye por sombras */

  --text:           #2d3748;
  --text-secondary: hsl(220 10% 30%);
  --text-muted:     hsl(220 10% 45%);

  --accent:         #5E72E4;
  --accent-soft:    #7C8DEB;
  --accent-surface: hsl(230 72% 63% / 0.1);

  /* Neumorphism specifics */
  --neu-light:  #ffffff;
  --neu-dark:   #b8bfc9;
  --neu-shadow-out: 8px 8px 16px var(--neu-dark), -8px -8px 16px var(--neu-light);
  --neu-shadow-in:  inset 6px 6px 12px var(--neu-dark), inset -6px -6px 12px var(--neu-light);

  --radius:     20px;
  --transition: 250ms;
  --ease-soft:  cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="dark"] {
  --bg:          #2d3748;
  --bg-surface:  #2d3748;
  --bg-elevated: #353f52;
  --text:           #e8eaf0;
  --text-secondary: hsl(220 10% 80%);
  --text-muted:     hsl(220 10% 60%);
  --accent:         #7C8DEB;
  --neu-light:  #3c4862;
  --neu-dark:   #1e2430;
  --neu-shadow-out: 8px 8px 16px var(--neu-dark), -8px -8px 16px var(--neu-light);
  --neu-shadow-in:  inset 6px 6px 12px var(--neu-dark), inset -6px -6px 12px var(--neu-light);
}
```

**Neumorphism patterns:**
```css
.neu-card {
  background: var(--bg-surface);
  border-radius: var(--radius);
  box-shadow: var(--neu-shadow-out);
  padding: clamp(20px, 2.5vw, 36px);
  /* asegurar contraste del texto — el body debe tener peso 600+ para ser legible sobre el fondo plomizo */
}
.neu-card h2, .neu-card h3 { font-weight: 800; color: var(--text); }
.neu-card p { font-weight: 600; color: var(--text-secondary); }

.neu-button {
  background: var(--bg-surface);
  border: none;
  border-radius: var(--radius);
  padding: 14px 28px;
  font-family: var(--font-body);
  font-weight: 700;
  color: var(--text);
  box-shadow: var(--neu-shadow-out);
  cursor: pointer;
  transition: box-shadow var(--transition) var(--ease-soft);
}
.neu-button:active,
.neu-button[aria-pressed="true"] {
  box-shadow: var(--neu-shadow-in);
}
.neu-input {
  background: var(--bg-surface);
  border: none;
  border-radius: var(--radius);
  padding: 14px 20px;
  font-family: var(--font-body);
  font-weight: 600;
  color: var(--text);
  box-shadow: var(--neu-shadow-in);
}
.neu-input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}
```

**Excepción documentada:** este preset usa `box-shadow` multi-capa (normalmente prohibido fuera de `card-premium`) porque *es* el lenguaje del estilo. Compensado con border-only en todos los demás casos.

---

## 24. Motion-Driven

Animaciones coreografiadas — hero con secuencia de entrada staggered, transiciones sección-a-sección con scroll-triggered keyframes, elementos que entran desde lados diferentes. Inter 800 (black) como display + Inter como body. Fondo near-black `#0A0A0A` con acento verde `#22C55E`. Vibe: Stripe / Apple Sequoia launch / Framer landing. Cuando la animación *es* la mitad del mensaje.

**Ideal for:**
- Landings con alto grado de polish
- Trailers interactivos de unidades didácticas
- Presentaciones HTML tipo keynote con entrada coreografiada
- Showcases de proyectos donde el "wow" visual importa

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 0.95;
  --lh-body:    1.55;

  --bg:          #0A0A0A;
  --bg-surface:  #141414;
  --bg-elevated: #1c1c1c;

  --border: hsl(140 40% 60% / 0.16);

  --text:           #e8e8e8;
  --text-secondary: hsl(0 0% 72%);
  --text-muted:     hsl(0 0% 48%);

  --accent:         #22C55E;
  --accent-soft:    #4ADE80;
  --accent-surface: hsl(142 71% 45% / 0.12);

  /* Motion specifics */
  --stagger-delay: 80ms;
  --entrance-dur:  600ms;
  --ease-out-expo: cubic-bezier(0.19, 1, 0.22, 1);
  --ease-back:     cubic-bezier(0.34, 1.56, 0.64, 1);

  --radius:     12px;
  --transition: 300ms;
}

[data-theme="light"] {
  --bg:          #f7f7f7;
  --bg-surface:  #ffffff;
  --bg-elevated: #f0f0f0;
  --border:      hsl(140 40% 40% / 0.18);
  --text:           #0a0a0a;
  --text-secondary: hsl(0 0% 28%);
  --text-muted:     hsl(0 0% 52%);
  --accent:         #16A34A;
}
```

**Motion patterns:**
```css
/* Stagger entrance: hijos de .hero-stage entran en cascada */
.hero-stage > * {
  opacity: 0;
  transform: translateY(32px);
  animation: motion-in var(--entrance-dur) var(--ease-out-expo) forwards;
}
.hero-stage > *:nth-child(1) { animation-delay: calc(var(--stagger-delay) * 0); }
.hero-stage > *:nth-child(2) { animation-delay: calc(var(--stagger-delay) * 1); }
.hero-stage > *:nth-child(3) { animation-delay: calc(var(--stagger-delay) * 2); }
.hero-stage > *:nth-child(4) { animation-delay: calc(var(--stagger-delay) * 3); }
.hero-stage > *:nth-child(5) { animation-delay: calc(var(--stagger-delay) * 4); }
@keyframes motion-in {
  to { opacity: 1; transform: none; }
}

/* Scroll-triggered reveal */
.reveal {
  opacity: 0;
  transform: translateY(48px) scale(0.98);
  transition: opacity 700ms var(--ease-out-expo),
              transform 700ms var(--ease-out-expo);
}
.reveal.in-view {
  opacity: 1;
  transform: none;
}

/* Slide from sides */
.slide-left  { transform: translateX(-60px); }
.slide-right { transform: translateX( 60px); }
.slide-left.in-view, .slide-right.in-view { transform: none; }

@media (prefers-reduced-motion: reduce) {
  .hero-stage > *, .reveal, .slide-left, .slide-right {
    animation: none; transition: none;
    opacity: 1; transform: none;
  }
}
```

**JS de apoyo (≤15 líneas):**
```js
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => e.isIntersecting && e.target.classList.add('in-view'));
}, { threshold: 0.2 });
document.querySelectorAll('.reveal, .slide-left, .slide-right').forEach(el => io.observe(el));
```

**Animation policy (excepción documentada):** duración 600-700ms para entradas, staggered delays con `nth-child`. Escaparate frente al default 200ms. Siempre con fallback `prefers-reduced-motion`.

---

## 25. Micro-interactions

Feedback sutil en cada interacción — hover con pulse, click con ripple, focus con glow, formularios con validación visual inmediata. Inter 700 como display + Inter como body. Fondo `#ffffff` con acento verde `#22C55E` para éxito y rojo `#EF4444` para error. Vibe: Linear / Notion / Figma. Cuando la UX se siente "viva" pero sin chillar.

**Ideal for:**
- Ejercicios interactivos con feedback inmediato (quiz, arrastrar, ordenar)
- Formularios de recogida de datos (encuestas, rúbricas)
- Dashboards con interacción frecuente
- Apps educativas donde cada clic tiene respuesta visible

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 1.1;
  --lh-body:    1.55;

  --bg:          #ffffff;
  --bg-surface:  #fafafa;
  --bg-elevated: #f5f5f5;

  --border: hsl(220 10% 82%);

  --text:           #1a1a1a;
  --text-secondary: hsl(220 5% 30%);
  --text-muted:     hsl(220 5% 52%);

  --accent:         #22C55E;
  --accent-soft:    #4ADE80;
  --accent-surface: hsl(142 71% 45% / 0.1);

  --danger:         #EF4444;
  --danger-surface: hsl(0 84% 60% / 0.1);

  /* Micro specifics */
  --pulse-ring: 0 0 0 0 hsl(142 71% 45% / 0.5);
  --glow-ring:  0 0 0 3px hsl(142 71% 45% / 0.25);

  --radius:     10px;
  --transition: 180ms;
  --ease-micro: cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="dark"] {
  --bg:          #0a0a0a;
  --bg-surface:  #141414;
  --bg-elevated: #1c1c1c;
  --border:      hsl(220 10% 25%);
  --text:           #e8e8e8;
  --text-secondary: hsl(220 5% 72%);
  --text-muted:     hsl(220 5% 48%);
  --accent:         #4ADE80;
}
```

**Micro patterns:**
```css
.btn-micro {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 10px 20px;
  font-family: var(--font-body);
  font-weight: 600;
  color: var(--text);
  cursor: pointer;
  transition: transform var(--transition) var(--ease-micro),
              border-color var(--transition) var(--ease-micro),
              box-shadow var(--transition) var(--ease-micro);
}
.btn-micro:hover {
  transform: translateY(-1px);
  border-color: var(--accent);
  box-shadow: var(--glow-ring);
}
.btn-micro:active { transform: translateY(0) scale(0.98); }
.btn-micro:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.pulse-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--accent);
  position: relative;
}
.pulse-dot::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  box-shadow: var(--pulse-ring);
  animation: pulse-out 1.8s ease-out infinite;
}
@keyframes pulse-out {
  0%   { box-shadow: 0 0 0 0 hsl(142 71% 45% / 0.5); }
  100% { box-shadow: 0 0 0 14px hsl(142 71% 45% / 0); }
}

.input-micro {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 12px 16px;
  font-family: var(--font-body);
  background: var(--bg);
  transition: border-color var(--transition), box-shadow var(--transition);
}
.input-micro:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: var(--glow-ring);
}
.input-micro.valid   { border-color: var(--accent); background: var(--accent-surface); }
.input-micro.invalid { border-color: var(--danger); background: var(--danger-surface); }

@media (prefers-reduced-motion: reduce) {
  .btn-micro, .pulse-dot::after { animation: none; transition: none; }
}
```

---

## 26. AI-Native UI

Layout chat-first para herramientas conversacionales — mensajes alternados user/assistant, sidebar de historial, shimmer en stream, área de composición con atajos. Inter 700 como display + Inter como body. Fondo `#0A0A0F` con acento violeta `#6366F1`. Vibe: Claude / ChatGPT / Perplexity / Linear Agents. Cuando el producto *es* una conversación.

**Ideal for:**
- Asistentes educativos conversacionales (tutor IA, repaso de examen)
- Interfaces de búsqueda con respuesta generativa
- Logs de sesión con cora / agentes
- Herramientas didácticas chat-first

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono@latest/files/jetbrains-mono-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
  @font-face { font-family: 'JetBrains Mono'; font-style: normal; font-display: swap; font-weight: 100 800;
    src: url('fonts/jetbrains-mono-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 1.1;
  --lh-body:    1.6;

  --bg:          #0A0A0F;
  --bg-surface:  #13131A;
  --bg-elevated: #1C1C26;

  --border: hsl(240 30% 60% / 0.14);

  --text:           #E8E8F0;
  --text-secondary: hsl(240 10% 78%);
  --text-muted:     hsl(240 8% 52%);

  --accent:         #6366F1;
  --accent-soft:    #8B5CF6;
  --accent-surface: hsl(238 84% 67% / 0.15);

  /* AI specifics */
  --msg-user-bg:      linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%);
  --msg-assistant-bg: hsl(240 20% 12%);
  --shimmer-gradient: linear-gradient(90deg,
                      hsl(240 20% 12%) 0%,
                      hsl(240 20% 18%) 50%,
                      hsl(240 20% 12%) 100%);

  --radius:     14px;
  --transition: 220ms;
  --ease-ai:    cubic-bezier(0.4, 0, 0.2, 1);
}

[data-theme="light"] {
  --bg:          #fafaff;
  --bg-surface:  #ffffff;
  --bg-elevated: #f5f5fc;
  --border:      hsl(240 20% 80%);
  --text:           #1a1a2e;
  --text-secondary: hsl(240 10% 30%);
  --text-muted:     hsl(240 8% 52%);
  --accent:         #6366F1;
  --msg-assistant-bg: hsl(240 30% 96%);
}
```

**AI patterns:**
```css
.chat-shell {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: 100dvh;
}
.chat-sidebar {
  background: var(--bg-surface);
  border-right: 1px solid var(--border);
  padding: 20px 16px;
}
.chat-main {
  display: flex;
  flex-direction: column;
  max-width: 820px;
  margin-inline: auto;
  padding: 24px;
  gap: 16px;
}
.msg {
  max-width: 78%;
  padding: 14px 18px;
  border-radius: var(--radius);
  font-family: var(--font-body);
  line-height: var(--lh-body);
}
.msg--user {
  align-self: flex-end;
  background: var(--msg-user-bg);
  color: #fff;
  border-bottom-right-radius: 4px;
}
.msg--assistant {
  align-self: flex-start;
  background: var(--msg-assistant-bg);
  color: var(--text);
  border: 1px solid var(--border);
  border-bottom-left-radius: 4px;
}

/* Shimmer para mensajes en streaming */
.msg--streaming {
  background: var(--shimmer-gradient);
  background-size: 200% 100%;
  animation: shimmer 1.4s linear infinite;
}
@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
@media (prefers-reduced-motion: reduce) {
  .msg--streaming { animation: none; background: var(--msg-assistant-bg); }
}
@media (max-width: 900px) {
  .chat-shell { grid-template-columns: 1fr; }
  .chat-sidebar { display: none; }
}
```

---

## 27. Interactive Cursor

Cursor custom que reacciona al hover — se agranda sobre enlaces, se transforma sobre botones, deja trail sobre imagenes. Inter 800 como display + Inter como body. Fondo `#FAFAFA` con acento violeta `#5E6AD2` (Linear-ish). Vibe: portfolios de diseñadores premium / agencias creativas / Awwwards. Cuando quieres que la experiencia puntero-centric sea parte del branding.

**Ideal for:**
- Portfolios premium y sitios personales de diseño
- Landings de proyectos creativos destacados
- Experiencias interactivas tipo museo digital
- Páginas de inicio de curso que quieren sentirse "especiales"

**Font loading:**
```bash
mkdir -p fonts && cd fonts
curl -fsSL -O https://cdn.jsdelivr.net/npm/@fontsource-variable/inter@latest/files/inter-latin-wght-normal.woff2
```

```html
<style>
  @font-face { font-family: 'Inter'; font-style: normal; font-display: swap; font-weight: 100 900;
    src: url('fonts/inter-latin-wght-normal.woff2') format('woff2'); }
</style>
```

**CSS variables:**
```css
:root {
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;

  --lh-display: 1.0;
  --lh-body:    1.55;

  --bg:          #FAFAFA;
  --bg-surface:  #ffffff;
  --bg-elevated: #f2f2f2;

  --border: hsl(240 10% 85%);

  --text:           #0a0a0a;
  --text-secondary: hsl(240 5% 26%);
  --text-muted:     hsl(240 5% 48%);

  --accent:         #5E6AD2;
  --accent-soft:    #8B93E3;
  --accent-surface: hsl(234 54% 60% / 0.1);

  /* Cursor specifics */
  --cursor-size:       18px;
  --cursor-size-hover: 48px;

  --radius:     8px;
  --transition: 220ms;
  --ease-cursor: cubic-bezier(0.2, 0.9, 0.25, 1);
}

[data-theme="dark"] {
  --bg:          #0a0a0a;
  --bg-surface:  #141414;
  --bg-elevated: #1c1c1c;
  --border:      hsl(240 10% 22%);
  --text:           #fafafa;
  --text-secondary: hsl(240 5% 78%);
  --text-muted:     hsl(240 5% 52%);
  --accent:         #8B93E3;
}
```

**Cursor patterns:**
```css
/* Ocultar cursor default, mostrar custom */
html { cursor: none; }
a, button, [data-cursor="hover"] { cursor: none; }

.cursor-dot {
  position: fixed;
  top: 0; left: 0;
  width: var(--cursor-size);
  height: var(--cursor-size);
  border-radius: 50%;
  background: var(--accent);
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  transition: width var(--transition) var(--ease-cursor),
              height var(--transition) var(--ease-cursor),
              background var(--transition) var(--ease-cursor),
              mix-blend-mode 0ms;
  mix-blend-mode: difference;
}
.cursor-dot.is-hover {
  width: var(--cursor-size-hover);
  height: var(--cursor-size-hover);
  background: var(--accent-soft);
}
.cursor-trail {
  position: fixed;
  top: 0; left: 0;
  width: 40px;
  height: 40px;
  border: 1px solid var(--accent);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9998;
  transform: translate(-50%, -50%);
  transition: transform 400ms var(--ease-cursor);
  opacity: 0.5;
}

/* Fallback: si el usuario tiene touch o no puede ver cursor custom, revertir */
@media (hover: none), (prefers-reduced-motion: reduce) {
  html, a, button, [data-cursor="hover"] { cursor: auto; }
  .cursor-dot, .cursor-trail { display: none; }
}
```

**JS de apoyo (≤20 líneas):**
```js
const dot = document.querySelector('.cursor-dot');
const trail = document.querySelector('.cursor-trail');
let tx = 0, ty = 0, dx = 0, dy = 0;
window.addEventListener('mousemove', e => {
  dot.style.transform = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%, -50%)`;
  tx = e.clientX; ty = e.clientY;
});
document.querySelectorAll('a, button, [data-cursor="hover"]').forEach(el => {
  el.addEventListener('mouseenter', () => dot.classList.add('is-hover'));
  el.addEventListener('mouseleave', () => dot.classList.remove('is-hover'));
});
(function loop() {
  dx += (tx - dx) * 0.12; dy += (ty - dy) * 0.12;
  trail.style.transform = `translate(${dx}px, ${dy}px) translate(-50%, -50%)`;
  requestAnimationFrame(loop);
})();
```

**Animation policy (excepción documentada):** `requestAnimationFrame` loop de trail activo mientras el puntero se mueve. Fallback obligatorio en touch y reduced-motion. Nunca usar como único medio de interacción (el cursor es *enhance*, no replace).

---

## Modifiers

Los *modifiers* son overlays aplicables **encima de cualquier preset** para añadir una capa técnica sin cambiar la paleta ni la tipografía. Se concibieron en v5.2 para cubrir estilos que funcionan mejor como "plugin" que como preset completo (#22 Zero Interface y #27 Interactive Cursor existen *también* como presets independientes, pero estos bloques documentan cómo usarlos como capa encima de otro preset).

### M1. Ambient (derivado de Zero Interface)

Añade una capa de contenido minimal ambiental (gradient radial sutil + waveform decorativa) sobre cualquier preset. Ideal para splash screens, pausas entre secciones densas, o mensajes de estado ("escuchando…", "procesando…").

```css
/* Aplicar encima de CUALQUIER preset */
.with-ambient {
  background-image: radial-gradient(ellipse at 50% 50%,
                    color-mix(in oklch, var(--accent) 8%, transparent) 0%,
                    transparent 70%);
}
.with-ambient .ambient-copy {
  text-align: center;
  max-width: 22ch;
  margin-inline: auto;
  text-wrap: balance;
  font-weight: 200; /* override ligero */
}
.with-ambient .ambient-waveform {
  display: inline-flex;
  gap: 4px;
  height: 40px;
  align-items: center;
  margin-top: 2rem;
}
.with-ambient .ambient-waveform span {
  width: 4px;
  background: var(--accent);
  border-radius: 2px;
  opacity: 0.6;
  animation: ambient-pulse 1.4s ease-in-out infinite;
}
.with-ambient .ambient-waveform span:nth-child(2) { animation-delay: 0.1s; height: 70%; }
.with-ambient .ambient-waveform span:nth-child(3) { animation-delay: 0.2s; height: 100%; }
.with-ambient .ambient-waveform span:nth-child(4) { animation-delay: 0.3s; height: 55%; }
.with-ambient .ambient-waveform span:nth-child(5) { animation-delay: 0.4s; height: 85%; }
@keyframes ambient-pulse { 0%,100% { transform: scaleY(0.5); } 50% { transform: scaleY(1); } }
@media (prefers-reduced-motion: reduce) {
  .with-ambient .ambient-waveform span { animation: none; transform: scaleY(0.7); }
}
```

**Uso:** añade la clase `.with-ambient` al `<section>` o `<main>` de la vista que quieres transformar. No toca el `:root` del preset base.

### M2. Custom Cursor (derivado de Interactive Cursor)

Añade un cursor puntero custom + trail sobre cualquier preset. Útil para portfolios y páginas de inicio premium donde quieres que el hover se sienta especial sin redefinir toda la paleta.

```css
html.with-custom-cursor { cursor: none; }
html.with-custom-cursor a,
html.with-custom-cursor button,
html.with-custom-cursor [data-cursor="hover"] { cursor: none; }

.with-custom-cursor .cursor-dot {
  position: fixed; top: 0; left: 0;
  width: 18px; height: 18px; border-radius: 50%;
  background: var(--accent);
  pointer-events: none; z-index: 9999;
  transform: translate(-50%, -50%);
  transition: width 220ms cubic-bezier(0.2, 0.9, 0.25, 1),
              height 220ms cubic-bezier(0.2, 0.9, 0.25, 1);
  mix-blend-mode: difference;
}
.with-custom-cursor .cursor-dot.is-hover { width: 48px; height: 48px; }

.with-custom-cursor .cursor-trail {
  position: fixed; top: 0; left: 0;
  width: 40px; height: 40px;
  border: 1px solid var(--accent);
  border-radius: 50%;
  pointer-events: none; z-index: 9998;
  transform: translate(-50%, -50%);
  opacity: 0.5;
}

@media (hover: none), (prefers-reduced-motion: reduce) {
  html.with-custom-cursor, html.with-custom-cursor * { cursor: auto; }
  .with-custom-cursor .cursor-dot,
  .with-custom-cursor .cursor-trail { display: none; }
}
```

**Uso:** añade `class="with-custom-cursor"` al `<html>` y los elementos `.cursor-dot` + `.cursor-trail` al body. El JS del preset #27 Interactive Cursor se reutiliza tal cual. Respeta automáticamente touch y reduced-motion.

### Combinando modifiers

Los modifiers son apilables. Ejemplo: Magazine Editorial + `with-custom-cursor` → revista densa con cursor premium. Bento Grids + `with-ambient` → landing modular con aura ambiental. La única restricción: evitar combinar `with-ambient` con presets que ya tengan gradient radial en el body (Storytelling-Driven, Creative Voltage) — chocarían visualmente.

---

## Usage Notes for Subagents

### Selecting a preset
- Default for Adri's educational work → **#13 Minimalista Adri**
- Dark + tech content → **#2 Electric Studio** or **#9 Neon Cyber**
- Light + reading-heavy → **#5 Notebook Tabs** or **#8 Vintage Editorial**
- Maximum visual impact → **#1 Bold Signal**
- Warm and personal → **#14 Soffia Warm** or **#12 Paper & Ink**
- Industrial / tooling / agentes → **#15 Signal Hardware**

### Applying a preset
1. Copy the `<link>` tags into `<head>`
2. Copy the `:root` block into your CSS
3. Use CSS custom properties throughout: `color: var(--text)`, `background: var(--bg-surface)`, etc.
4. For the `[data-theme]` toggle, add `data-theme="dark"` or `data-theme="light"` to `<html>` and toggle via JS

### Variable reference
| Variable | Purpose |
|----------|---------|
| `--bg` | Page background |
| `--bg-surface` | Cards, panels, inputs |
| `--bg-elevated` | Dropdowns, modals, tooltips |
| `--border` | All dividers and outlines |
| `--text` | Primary text |
| `--text-secondary` | Labels, captions, less important text |
| `--text-muted` | Placeholders, disabled states |
| `--accent` | Primary action color (buttons, links, highlights) |
| `--accent-surface` | Tinted background for accent-colored areas |
| `--font-display` | Headings (h1–h3) |
| `--font-body` | Body text and UI |
| `--font-mono` | Code, data, terminal content |
| `--lh-display` | Line height for headings (1.05) |
| `--lh-body` | Line height for body text (1.55) |
| `--radius` | Border radius for components |
| `--transition` | Duration for hover/focus transitions |
| `--ease-out` | Easing curve for animations |
