---
name: adri-style
description: >
  Sistema de diseño inyectable (NO invocar directamente). Otros skills (presentacion-html,
  dashboard-educativo, frontend-design) lo importan automáticamente. Solo invocar si el
  usuario pide explícitamente cambiar preset, tema, paleta de colores, o consultar los
  15 presets disponibles.
---

# Adri Style v5 - Sistema de Diseño Personal

Sistema de diseño con 15 presets visuales, tipografia fluida y layouts expresivos.
Referencia: [adri-app.com](https://adri-app.com).
Fuentes: Butterick (tipografia), Utopia (escala fluida), Vercel Geist (tokens), Emil Kowalski (animaciones), Linear/Vercel (dark mode profundidad), Refactoring UI (tinted grays).

## Workflow (Decision Tree)

### Paso 0: Elegir estilo visual (OBLIGATORIO)

Antes de escribir CSS, elegir un preset de `references/style-presets.md`:

| Contexto | Presets recomendados |
|----------|---------------------|
| Dashboard educativo | Minimalista Adri, Swiss Modern, Terminal Green |
| Landing page / Portfolio | Bold Signal, Soffia Warm, Creative Voltage |
| Docs / herramienta funcional | Electric Studio, Minimalista Adri |
| Ejercicio interactivo | Pastel Geometry, Split Pastel, Electric Studio |
| Editorial / literario | Vintage Editorial, Paper & Ink, Dark Botanical |
| Futurista / gaming | Neon Cyber, Creative Voltage |
| Presentacion HTML | Notebook Tabs, Bold Signal, Soffia Warm |

**Elegir preset:**
1. Abrir catalogo visual: `open ~/.dotfiles/ai/skills/adri-style/assets/preset-catalog.html`
2. El usuario elige visualmente el preset que quiere
3. Copiar el bloque `:root` completo del preset elegido de `references/style-presets.md`
4. Copiar los `<link>` de fuentes del preset
5. Copiar `assets/base.css` como punto de partida
6. Sobreescribir las variables de `base.css` con las del preset

### Nuevo proyecto web
1. **Elegir preset** → Paso 0
2. Copiar `assets/base.css` + variables del preset
3. Layout y container → `references/layout.md`
4. Componentes necesarios → `references/components.md`
5. Animaciones → `references/animation.md`
6. Verificar con checklist

### Dashboard educativo
1. **Elegir preset** → Minimalista Adri o Swiss Modern
2. Escala: ratio 1.125 (Major Second) para densidad
3. Cards y KPIs → `references/components.md`
4. Graficas: Chart.js con colores semanticos → `references/color-and-theme.md`
5. Tabular-nums obligatorio en todas las notas

### Presentacion HTML / Landing
1. **Elegir preset** → Bold Signal, Soffia Warm, Creative Voltage, etc.
2. Escala: ratio 1.333 (Perfect Fourth) para impacto visual
3. Layouts asimetricos: alternar left-heavy, right-heavy, centered
4. Patrones premium → `references/components.md` (glassmorphism, glow, bento grid)
5. Animaciones de entrada → `references/animation.md`

### Documento / contenido de lectura
1. **Elegir preset** → Paper & Ink o Notebook Tabs
2. Clase .prose → `references/typography.md` (65ch, line-height 1.5)
3. Colores suaves → `references/color-and-theme.md`

## Reglas core

**ALWAYS:**
- Usar escala tipografica fluida con clamp() (variables --step-*)
- Usar text-wrap: balance en todos los headings (h1-h6)
- Usar 3 roles tipograficos: --font-display, --font-body, --font-mono
- Font pairing real: --font-display DIFERENTE de --font-body (Space Grotesk, Instrument Serif, etc.)
- Implementar tema dual (oscuro por defecto) con toggle + localStorage
- Usar Lucide SVG para iconos (stroke-width: 1.5, nunca emojis)
- Usar font-variant-numeric: tabular-nums en datos numericos
- Composicion dinamica: posicionar texto segun el contenido visual → `references/composition.md`
- Usar al menos 3 tipos de componentes distintos por pagina → `references/components.md`
- Usar al menos 2 patrones de layout distintos (no todo grid uniforme) → `references/composition.md`
- Incluir al menos 1 visualizacion SVG inline (donut con stroke-dashoffset, sparkline con polyline points, barras con scaleX, o decorativa con path/circle) en TODOS los outputs — no solo cuando haya datos numéricos
- Usar prefers-reduced-motion para accesibilidad
- Escala dramatica: al menos un elemento con tamaño ≥ step-4 (heroes, KPIs, spotlight numbers)
- Usar color-mix() para superficies tintadas, hover states y borders con tinte del color de acento
- Hover states con transform o border-color (no solo cambio de color)
- Near-black para fondo oscuro: #0a0a0a o hsl(220 15% 8%), NUNCA #000000 puro
- Superficies tintadas: backgrounds con rgba() o color-mix() a baja opacidad para status, badges, hover
- Al menos 4 niveles de --step-* usados en la pagina (jerarquia visual rica)
- 2 breakpoints responsive minimo (900px + 600px)
- Alternar layouts entre secciones consecutivas (no repetir el mismo patron 3 veces seguidas)
- Margenes asimetricos en headings: margin-top > margin-bottom (ej: margin-top: --space-l, margin-bottom: --space-s)

**COMPOSITION (principios de composición visual — inspirados en Present/Faces, Linear, Vercel):**
- Cada seccion debe transmitir **1 idea principal** — no 4-5 elementos compitiendo por atencion
- El contenido debe ocupar ~50-70% del viewport, el resto es **espacio negativo intencional**
- Hero sections: padding generoso `clamp(80px, 12vw, 160px)` vertical — que respire
- Secciones funcionales: mas compactas `clamp(48px, 6vw, 80px)` — pero nunca agolpadas
- **Eyebrow labels** encima de titulos: peso 300, ALL-CAPS, letter-spacing +0.15em a +0.25em, color de acento
- **Numeros decorativos gigantes** (01, 02, 03) como textura de fondo: peso 200, opacity 0.04, position absolute
- **Splits asimetricos**: imagen/visual 60% + texto 40%, o viceversa — NUNCA 50/50 exacto salvo comparativas
- **Contraste de pesos extremo**: display 900 (Black) + labels 300 (Light) + body 300-400 (Regular gris al 45%)
- Body text en gris al 40-45% opacity (`rgba(255,255,255,0.45)` en dark) — nunca blanco puro para cuerpo
- **Profundidad con gradientes radiales**: `radial-gradient(ellipse at 70% 30%, rgba(accent, 0.04), transparent 60%)` en secciones alternas. En modo claro: opacidad ≤ 0.03 y saturación baja — nunca un tinte de color marcado
- Max 3 cards por fila, y con jerarquia spotlight (1 grande + 2 pequeñas), nunca 4 identicas

**VIEWPORT-FIT (contenido autocontenido por vista):**
- Cada pestaña/sección seleccionada debe caber COMPLETA en el viewport sin scroll
- Si el contenido no cabe, subdividir en más pestañas o subsecciones
- **Preferir navegación por PESTAÑAS sobre scroll** en dashboards, docs y contenido educativo — más práctico para el usuario
- En docs con sidebar: cada sección del sidebar = un panel que ocupa `calc(100dvh - header)`, sin scroll de página
- Header/título SIEMPRE clicable → scroll to top o volver a pestaña inicial (`onclick="scrollTo({top:0,behavior:'smooth'})"`)
- Números decorativos: NUNCA sobre fondos del mismo color, `right: clamp(40px, 6vw, 100px)` mínimo desde bordes
- Padding lateral mínimo en todo el contenido: `clamp(24px, 4vw, 80px)`
- **Fondos consistentes**: secciones consecutivas deben usar el MISMO fondo (`var(--bg)`). Solo alternar fondo cuando hay razón visual clara (hero destacado). Evitar huecos de color vacíos entre secciones
- **Centrado vertical**: el contenido de cada panel/sección debe estar centrado verticalmente en el viewport, no pegado arriba
- **Variedad de layouts**: cada sección debe usar un layout DIFERENTE (split 60/40, split inverso 40/60, bento grid, full-width, centrado). No repetir el mismo patrón visual en secciones consecutivas

**IMÁGENES PROTAGONISTAS (contenido visual educativo):**
- Usar imágenes reales cuando el contenido lo pida: fotos de autores, portadas de libros, ilustraciones de época
- Splits imagen+texto asimétricos: imagen 55-60% + texto 40-45%
- Imágenes con `object-fit: cover`, `border-radius: var(--radius)`, sombra sutil con border
- Placeholder si no hay imagen real: fondo tintado con icono Lucide SVG grande (no cuadrado gris vacío)
- En contenido literario/editorial: las imágenes aportan contexto visual — NO son decoración

**EJERCICIOS INTERACTIVOS (patrón texto-fuente + pestañas):**
- Texto fuente (fragmento a analizar) SIEMPRE visible arriba, posición sticky
- Actividades organizadas en PESTAÑAS debajo del texto fuente (no scroll entre actividades)
- Si una actividad no cabe en el viewport, solo esa actividad tiene scroll interno
- Cada pestaña = 1 actividad autocontenida con instrucciones + espacio de respuesta
- Feedback visual inmediato al comprobar (color-mix con verde/rojo semántico)

**RHYTHM (ritmo vertical):**
- PROHIBIDO double-spacing: si la sección tiene padding-top, el h2 hijo NO necesita margin-top grande
- Variar el padding entre secciones (hero generoso, contenido funcional compacto)
- Footer: margin-top de --space-m o --space-l (NO --space-xl ni --space-2xl)
- NO usar inline style="margin-top: 0" en headings para compensar reglas globales incorrectas — arreglar las reglas globales

**NEVER:**
- font-weight > 900 (display fonts pueden usar 700-900 Black, body nunca > 600)
- box-shadow (solo bordes, excepto card-premium con inset para specular highlights)
- Colores saturados o gradientes decorativos
- Emojis en la interfaz
- Animar padding, margin, width, height, left, top, right, bottom (solo transform y opacity)
- transition con duración > 0.3s (usar 0.2s para UI, max 0.3s)
- Progress bars con `transition: width` (usar transform: scaleX() con transform-origin: left)
- Tamaños fijos en px para tipografia (usar --step-*)
- Fondo #000000 puro (demasiado contraste, parece template)
- 4 cards identicas en fila sin jerarquia (spotlight: 1 grande + N pequeños)
- Chart.js con colores por defecto sin personalizar
- Mismo font-family para display y body (sin contraste tipografico)
- padding: var(--space-2xl) en 4+ secciones uniformemente (falta jerarquia de espaciado)
- h2 { margin-top: var(--space-xl) } global cuando las secciones ya tienen padding grande
- Footer margin-top: var(--space-xl) o mayor

**NEVER (anti-AI-slop — ver `references/components.md` § ANTI-AI-SLOP):**
- `bg-indigo-500` ni purple gradients genericos (Tailwind default, cada IA genera esto)
- 3 cards identicas con icono en grid como layout principal (el layout mas generico)
- Inter como unica fuente sin display font contrastante
- Grises puros `hsl(0, 0%, N%)` — siempre tinted grays: `hsl(210, 15%, N%)` o `hsl(30, 8%, N%)`
- Hero centrado + 3-column grid + CTA como unico layout (cliché "startup template")
- Single box-shadow para profundidad (usar multi-layer o border-only)

**WHEN INTERACTIVE (formularios, ejercicios, quizzes):**
- :focus-visible con outline visible en todos los inputs/buttons/selects
- label[for=] o aria-label en todos los inputs (accesibilidad)
- cursor: pointer en elementos clicables
- scroll-behavior: smooth cuando hay navegacion interna
- En ejercicios: feedback tintado con color-mix() para .correct/.incorrect (verde/rojo semántico)
- En ejercicios: estilo :disabled para bloquear respuestas tras comprobar

**CONSIDER:**
- Clase .prose para bloques de lectura (max-width: 65ch)
- Breakpoints 900px y 600px para responsive
- Border-radius maximo 12px (excepto pills: 100px)
- Chart.js para graficas en dashboards y explicaciones visuales

## Quick Reference

| Propiedad | Valor |
|-----------|-------|
| Presets | 15 estilos en `references/style-presets.md` |
| Font display | Segun preset (Cabinet Grotesk, Space Grotesk, Instrument Serif, etc.) |
| Font body | Segun preset (Inter, DM Sans, Satoshi, Lora, etc.) |
| Font mono | Geist Mono / JetBrains Mono |
| Escala | 1.25 (general), 1.125 (dashboard), 1.333 (editorial) |
| Container | max-width: 1000px |
| Prose | max-width: 65ch |
| Radio | 12px |
| Transicion | 0.2s ease |
| Line-height body | 1.55 (dark), 1.5 (light) |
| Line-height titles | 1.05 |
| Letter-spacing titles | -0.04em (dark), -0.03em (light) |
| Grays | Siempre tinted: hsl(210, 15%, N%) o hsl(30, 8%, N%) |
| Body text dark | #E8E8E8 off-white (no #FFFFFF puro) |

## Checklist de revision

- [ ] Escala fluida con --step-* (no px fijos)
- [ ] Fontes cargadas con display=swap
- [ ] 3 roles tipograficos definidos (display, body, mono)
- [ ] Variables CSS con tema dual configuradas
- [ ] Toggle de tema con persistencia localStorage
- [ ] Datos numericos con font-mono + tabular-nums
- [ ] Layouts variados (no todo centrado)
- [ ] Elementos visuales/graficas donde aportan
- [ ] Responsive: 3→2→1 columna en grids
- [ ] Solo transform/opacity animados
- [ ] prefers-reduced-motion
- [ ] Iconos Lucide SVG (no emojis)

## Referencias

- `references/style-presets.md` — **15 presets visuales** con CSS variables completas (NUEVO v5)
- `references/typography.md` — Sistema tipografico fluido, font pairing, escala Utopia, tipografia premium dark
- `references/composition.md` — Composicion dinamica: posicion de texto segun contenido visual
- `references/animation.md` — Easings, duracion, scale, blur, propiedades seguras (Emil Kowalski)
- `references/color-and-theme.md` — Variables tema dual, contraste, semaforo educativo (Butterick)
- `references/components.md` — Cards, botones, tags, header blur, **patrones premium dark mode, bento grid, anti-AI-slop** (NUEVO v5)
- `references/layout.md` — Grid, container, prose, responsive, breakpoints

## Assets

- `assets/global.css` — Template CSS base para copiar en nuevos proyectos (default: Minimalista Adri)
- `assets/base.css` — CSS base inyectable con reset, tipografia fluida, tema dual y componentes base (NUEVO v5)
