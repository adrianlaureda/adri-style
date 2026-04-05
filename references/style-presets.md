# Style Presets — Visual Reference for Web Projects

15 ready-to-use visual presets. Each includes a complete `:root` CSS variables block, font pairing, and `<link>` tags. Designed for copy-paste by AI subagents building web pages, dashboards, and educational tools.

---

## Quick Reference Table

| # | Name | Mood | Background | Accent | Display Font | Body Font |
|---|------|------|------------|--------|-------------|-----------|
| 1 | Bold Signal | High impact, keynote | `#050505` | `#ffffff` | Satoshi 900 | Inter |
| 2 | Electric Studio | Professional tech | `#0a1628` | `#3b82f6` | Geist 800 | Inter |
| 3 | Creative Voltage | Retro-modern | `#1a0a2e` | `#f59e0b` | Clash Display | Satoshi |
| 4 | Dark Botanical | Elegant organic | `#0a0f0a` | `#4ade80` | Cormorant Garamond | DM Sans |
| 5 | Notebook Tabs | Editorial paper | `#f5f0e8` | `#2563eb` | Newsreader | Source Serif 4 |
| 6 | Pastel Geometry | Friendly pastel | `#fef7f4` | `#e07850` | Satoshi 700 | Inter |
| 7 | Split Pastel | Juicy bicolor | `#fff1f2` | `#e11d48` | Space Grotesk | Inter |
| 8 | Vintage Editorial | Literary classic | `#faf8f5` | `#92400e` | Playfair Display | Lora |
| 9 | Neon Cyber | Futuristic neon | `#030712` | `#06ffa5` | Orbitron | Inter |
| 10 | Terminal Green | Developer | `#0a0a0a` | `#22c55e` | JetBrains Mono | JetBrains Mono |
| 11 | Swiss Modern | Corporate precise | `#ffffff` | `#000000` | Switzer 900 | Inter |
| 12 | Paper & Ink | Literary reflective | `#1c1917` | `#d4a574` | Instrument Serif | Inter |
| 13 | Minimalista Adri | Educational default | `#050505` | multi-section | Geist 700 | Inter |
| 14 | Soffia Warm | Warm premium | `hsl(220 15% 8%)` | `#c9a96e` | Satoshi 900 | Inter |
| 15 | Signal Hardware | Monochrome industrial | `#050505` | `#f04d23` | Space Grotesk | Space Mono |

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

---

## 1. Bold Signal

Máximo contraste tipográfico — negro profundo con blanco como único acento. Para landings de impacto, portadas de proyectos o cualquier pieza donde la tipografía ES el diseño.

**Ideal for:**
- Project landing pages
- Portfolio hero sections
- Keynote-style single-page presentations
- Dark-mode dashboards with dramatic headers

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
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

  /* Backgrounds */
  --bg:          #050505;
  --bg-surface:  #0e0e0e;
  --bg-elevated: #161616;

  /* Borders */
  --border: hsl(0 0% 100% / 0.1);

  /* Text */
  --text:           #ffffff;
  --text-secondary: hsl(0 0% 100% / 0.7);
  --text-muted:     hsl(0 0% 100% / 0.4);

  /* Accent — white IS the accent here */
  --accent:         #ffffff;
  --accent-surface: hsl(0 0% 100% / 0.06);

  /* Utilities */
  --radius:     0px;
  --transition: 200ms;
  --ease-out:   cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  --bg:          #f8f8f8;
  --bg-surface:  #ffffff;
  --bg-elevated: #efefef;
  --border:      hsl(0 0% 0% / 0.1);
  --text:           #0a0a0a;
  --text-secondary: hsl(0 0% 0% / 0.6);
  --text-muted:     hsl(0 0% 0% / 0.35);
  --accent:         #0a0a0a;
  --accent-surface: hsl(0 0% 0% / 0.06);
}
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

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
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

Marfil antiguo con tinta sepia. La combinación Playfair + Lora evoca libros bien impresos, revistas culturales y el cuidado tipográfico de otro tiempo. Sin nostalgia barata.

**Ideal for:**
- Literary analysis and language arts content
- Book club or reading list pages
- Cultural or historical educational materials
- Long-form articles and essays

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
```

**CSS variables:**
```css
:root {
  /* Fonts */
  --font-display: 'Playfair Display', 'Georgia', serif;
  --font-body:    'Lora', 'Georgia', serif;
  --font-mono:    'JetBrains Mono', monospace;

  /* Line heights */
  --lh-display: 1.05;
  --lh-body:    1.55;

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

  /* Accent */
  --accent:         #92400e;
  --accent-surface: hsl(25 75% 31% / 0.08);

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
  --accent:         #d4935a;
  --accent-surface: hsl(30 60% 60% / 0.1);
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

**Font loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
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
