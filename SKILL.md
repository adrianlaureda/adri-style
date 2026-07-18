---
name: adri-style
description: >
  Sistema de diseño inyectable (NO invocar directamente). Otros skills (presentacion-html,
  dashboard-educativo, frontend-design) lo importan automáticamente. Solo invocar si el
  usuario pide explícitamente cambiar preset, tema, paleta de colores, o consultar los
  27 presets disponibles.
---

<!-- PRESCRIPTIVE-PATTERN id=adri-style-preset-fonts version=1 date=2026-05-28 rationale=Modelos medios olvidan declarar data-preset y cargan single-font Inter (ai-slop), saltándose el catálogo canónico de 27 presets y la regla Bold Signal por defecto. -->

## Reglas duras: invariantes de salida adri-style

Cualquier HTML que use este sistema DEBE cumplir, sin excepción:

1. **`data-preset="NN-name"` en `<html>` o root container**. Sin esa marca, el HTML se considera fuera del sistema y `audit-adri.sh` lo marca FAIL.
2. **Cargar AMBAS fuentes del preset declarado** (display + body). Single-font solo si el preset lo justifica explícitamente (3 presets: Bold Signal, Swiss Modern, Exaggerated Minimalism). Para el resto, cargar pareja completa = no negociable.
3. **Default Bold Signal (`data-preset="01-bold-signal"`)** cuando:
   - La pieza lleva firma o presencia de Adri (presentación, charla, portfolio, comunicación pública).
   - El contexto es ambiguo o no claramente educativo-funcional.
4. **Iconos: Lucide SVG inline**. Nunca emojis para iconos de UI.
5. **Light/dark toggle: `lucide:moon` (modo oscuro activo) ↔ `lucide:sun` (modo claro activo)**. Inverso = bug visual.
6. **Test de la Caja (EAR)**: cada caja con `background+border+border-radius` debe ser **E**s accionable, **A**grupa heterogéneo o **R**epresenta dato discreto. Si no pasa ninguna prueba, va sin caja (espaciado + tipografía + separador). Heurística rápida: si en pantalla hay >8 elementos con `border-radius > 6px`, hay encajamiento excesivo.

Excepción / condición: si el output es interno (debug, tooling, no firmado) puede saltarse Bold Signal default, pero la regla 1 (data-preset) sigue.

Catálogo canónico de presets: `references/style-presets.md` + `references/presets.json` (machine-readable mirror).

<!-- /PRESCRIPTIVE-PATTERN -->

# Adri Style v5.8 - Sistema de Diseño Personal

Sistema de diseño con 27 presets visuales, tipografia fluida y layouts expresivos.
Referencia: [adri-app.com](https://adri-app.com).
Fuentes: Butterick (tipografia), Utopia (escala fluida), Vercel Geist (tokens), Emil Kowalski (animaciones), Linear/Vercel (dark mode profundidad), Refactoring UI (tinted grays), Impeccable (anti-patterns AI-tell).

## Changelog v5.7 → v5.8 (2026-05-09, P4 entera ejecutada)

Cierre del backlog completo `impeccable-integration` (P1+P2+P3+P4). Cuatro items P4 originalmente "ideas no priorizadas" implementados como adiciones no-breaking:

- **`scripts/audit-adri-full.sh` (NUEVO)**: wrapper de quality-check unificado. Combina `audit-adri.sh` + `html-validate` (npx) + `pa11y` WCAG 2.1 AA (npx) + opcional `broken-link-checker`. Flags `--quick` (solo audit-adri, rápido) y `--links` (verificación enlaces, lento). Sin instalación global, todo vía npx.
- **`scripts/measure-adri.sh` (NUEVO) + LaunchAgent diario 06:30**: medición objetiva del % de outputs HTML que pasan audit-adri.sh sin críticos. Escanea `~/Proyectos/Claude/{apps/adri-react/public, educacion, personal}` y registra JSONL por día en `~/Library/Application Support/adri-style-metrics/`. Modo `--report` genera tabla markdown de tendencia 30d. Línea base 2026-05-09: 35 HTMLs escaneados, 4 OK (11%), 31 con críticos (mayormente single-font Inter en minijuegos pre-override). LaunchAgent `com.adri.style-metrics` cargado.
- **`references/colors-oklch.md` (NUEVO)**: documentación del espacio de color OKLCH como capa adicional no-breaking. Tabla de los 27 accents canónicos convertidos a OKLCH para usar en variantes derivadas (hover, muted, semantic). Migración a v6 donde el JSON canónico añadiría `color.accent_oklch` queda como camino opcional. Soporte navegador ~96% global a 2026-05.
- **Chrome ext Impeccable**: instalación manual desde Chrome Web Store (Adri completa el click). Permite auditoría visual ad-hoc en preview local sin tocar código. Complementa `audit-adri.sh` que es CLI estático.

Sin breaking changes. Backlog impeccable-integration cerrado entero.

## Changelog v5.6 → v5.7 (2026-05-08 noche, anti-cajas como requisito canónico)

Iteración sobre `estacion-clasificacion` (adri-react/public) reveló que el **AI-tell más persistente NO es la tipografía sino el encajamiento**: cuando todo va envuelto en `background + border + border-radius`, el resultado parece SaaS dashboard genérico aunque la tipografía esté impecable. Adri lo expresó así: «Veo cuadros, destaques sin necesidad. Me gusta el estilo minimalista, salvo que sea un botón que haya que clicar por algún motivo».

- **`references/components.md` §15 (NUEVO)**: regla canónica **Test de la Caja (EAR)** — cada caja debe justificar su existencia con AL MENOS UNA de tres pruebas: **E**s accionable / **A**grupa contenido heterogéneo / **R**epresenta un dato discreto. Si no pasa ninguna, va sin caja (espaciado + tipografía + separador horizontal). Documentados 6 patrones canónicos de sustitución con ejemplos before/after: selectores radio, inputs de texto, contenedor protagonista, feedback contextual, cards de equipo, listados/tablas. Lista cerrada de excepciones (botones de acción, modales, code blocks, quotes editoriales, cards de portfolio en grid). Heurística rápida: contar elementos con `border-radius > 6px` en pantalla visible — si supera 8, hay encajamiento excesivo.
- **Checklist de entrega** (`components.md` final) ampliada con la casilla v5.7.

## Changelog v5.5 → v5.6 (2026-05-08 noche, fuente única `presets.json`)

Eliminada la duplicación de catálogo entre `audit-adri.sh` (case bash con 27 entries) y `references/style-presets.md` (tabla canónica humana). Ahora hay un mirror programático autoritativo: `references/presets.json`.

- **`references/presets.json` (NUEVO)**: schema 1.0 con los 27 presets. Por cada uno: id, n, name, fonts (display/body/single_font/justifications/weights), color (bg/accent), mode_default, estado, uso_real. Generado a partir de la tabla v5.4. La fuente humana sigue siendo `references/style-presets.md`; el JSON es mirror que se actualiza después.
- **`scripts/audit-adri.sh` (v5.6)**: la función `preset_canonical_fonts()` ahora lee de `references/presets.json` con `jq`. El catálogo bash hardcoded se elimina. Si `presets.json` o `jq` no están disponibles, el filtro 2 desactiva limpiamente (treat as preset desconocido).
- **Compatibilidad**: el comportamiento del filtro 2 es idéntico (8/8 batch + test negativo). Solo cambia la fuente de datos. No es breaking — los outputs existentes que pasaban v5.5 siguen pasando v5.6.
- **Desbloquea**: futuras herramientas (slider `Font variation` en `tweak-adri`, integraciones externas, validador de pesos) ya pueden consumir el JSON sin parsear markdown.

## Changelog v5.4 → v5.5 (2026-05-08 noche, cierre agujero filtro 2)

El filtro 2 introducido en v5.4 era ingenuo: aprobaba cualquier HTML que declarara `data-preset="NN-name"` aunque el HTML cargara solo una fuente y el preset declarado pidiera pareja display+body. Resultado: ai-slop (single-font Inter) disfrazado por declaración. Detectado y corregido tras auditar 7 cinematic-modules cherry-picked.

- **`scripts/audit-adri.sh`** (v5.5): el filtro 2 ahora **verifica coherencia** preset↔fuentes. Mantiene un catálogo interno de los 27 presets con sus fuentes canónicas (display + body) y exige que TODAS aparezcan cargadas en el HTML (vía `<link>` Google Fonts/Fontshare o declaración `font-family:` directa). Si declaras `01-bold-signal` pero no cargas Satoshi → FAIL. El reporte muestra "Preset declarado: NN-name · fuentes coherentes ✓" o "INCOHERENTE — fuentes esperadas: …".
- **`references/cinematic-modules/`** (en `presentacion-html`): 7 módulos cherry-picked de `robonuggets/cinematic-site-components` adaptados con Satoshi 900 display + Inter 300 body coherente con Bold Signal. Estaban single-font Inter en v0.1.0 (regresión IA-slop); arreglados en v5.5.

## Changelog v5.3 → v5.4 (2026-05-08, cierre Top 3 audit Codex ABCD)

Cierre de los dos puntos críticos del audit Codex (`AUDIT-codex-ABCD-2026-05-08.md` bloques C2/E2/F2):

- **`references/style-presets.md`**: nueva sección **"Audit v5.4 — Reglas de fuentes y pesos por preset"** con tabla canónica de los 27 presets. Cada preset declara explícitamente: pareja display/body, weights permitidos, justificación si single-font, justificación si body>500 default, modo light/dark, estado (`activo` / `activo-frágil` / `revisión-30d`). 8 presets quedan marcados como candidatos a eliminar tras 2026-06-08 si no aparecen en outputs reales (3, 4, 7, 9, 11, 23, 24, 27).
- **`templates/bootstrap-adri.html` (NUEVO)**: plantilla canónica para outputs nuevos. Carga Bold Signal por defecto (Satoshi + Inter + JetBrains Mono), tokens completos del preset, toggle light/dark con iconos lucide:moon/lucide:sun inline, esqueleto header/main/footer con comentarios de extensión. Pasa `audit-adri.sh` con preset declarado vía `data-preset="01-bold-signal"`. Cualquier output nuevo DEBE arrancar de aquí — sustituyendo el bloque `<!-- preset: NN-name -->`, las `<link>` de fuentes y el `:root`.
- **`scripts/audit-adri.sh`**: añadido filtro 2 — `overused-font` se considera FILTRADO cuando el HTML declara `data-preset="NN-name"` (señal de que el uso de Inter/Geist/etc. es intencional del preset y no IA-genérico).

## Changelog v5.2 → v5.3 (2026-05-08, post-audit Impeccable de 5 sites reales)

Cambios disparados por evidencia objetiva: 24 anti-patterns detectados en `branding-adri`, `adri-app-react/estacion-clasificacion`, `planificacion-2eso`, `formacion-ia-xograr`, `adri-app.com`.

- **`typography.md`**: eliminado "Inter 600" como default global. Cada preset declara su pareja display+body. Defaults rebajados a 300/400/500. Excepciones documentadas (Bold Signal Satoshi 900, Swiss Modern Inter 700, Exaggerated Minimalism). Single-font prohibido salvo decisión consciente del preset.
- **`components.md`**: avisos sobre anti-patterns en barras de progreso legacy (5 ejemplos con `transition: width/height`). Nueva sección **§14 Modern Progress Bars** con `transform: scaleX/scaleY` + `transform-origin`. Aviso sobre `border-left` colorido grueso (válido si codifica datos, anti-pattern si decoración).
- **`animation.md`**: prohibición explícita de `cubic-bezier(...> 1.0...)` (overshoot/bounce/elastic) por defecto. Refuerzo de `prefers-reduced-motion`. Refuerzo de "no animar `width/height/padding/margin/border/top/left`".
- **Linter `audit-adri.sh`** disponible en `scripts/` (CLI Impeccable + filtro de excepciones educativas: semáforo `border-left` permitido, etc.).

## Workflow (Decision Tree)

### Paso 0: Elegir estilo visual (OBLIGATORIO)

Antes de escribir CSS, elegir un preset de `references/style-presets.md`.

#### Default por antonomasia: Bold Signal ★

**Bold Signal** es la marca personal de Adri (ver `references/identity-adri.md` para logo + 10 animaciones + tokens.css importable). Se usa **por defecto cuando**:

- La pieza lleva firma o presencia de Adri (presentación, charla, portfolio, comunicación pública).
- El contexto es ambiguo o no claramente educativo-funcional.
- Se necesita coherencia visual con el brandbook live (https://branding-adri.adrianlaureda.workers.dev/) y los proyectos del ecosistema (`adri-react`, `formacion-xograr`, `planificacion-4eso`).

**Los presets contextuales mantienen prioridad** cuando el contexto lo dicta inequívocamente (dashboard de calificaciones → Minimalista Adri por colores semánticos; quiz alumnos → Pastel Geometry; lectura larga → Paper & Ink).

#### Tabla contexto → preset

| Contexto | Presets recomendados |
|----------|---------------------|
| **Marca Adri visible / contexto ambiguo / firma personal** | **Bold Signal ★ (default Adri)** |
| Dashboard educativo | Minimalista Adri, Swiss Modern, Terminal Green |
| Landing page / Portfolio | Bold Signal ★, Soffia Warm, Creative Voltage |
| Docs / herramienta funcional | Electric Studio, Minimalista Adri |
| Ejercicio interactivo | Pastel Geometry, Split Pastel, Electric Studio |
| Editorial / literario 1-col | Vintage Editorial, Paper & Ink, Dark Botanical |
| Longread / revista multi-col | **Magazine Editorial** |
| Futurista / gaming | Neon Cyber, Creative Voltage |
| Presentacion HTML | Bold Signal ★, Notebook Tabs, Soffia Warm |
| Unidad didáctica narrativa / curso inmersivo | **Cinematic Story** |
| Narrativa por capítulos con acentos por sección | **Storytelling-Driven** |
| Minimal agresivo / tipografía gigante como protagonista | **Exaggerated Minimalism** |
| Modular Apple-style / cards asimétricas con jerarquía | **Bento Grids** |
| Lectura densa estilo papel electrónico / calma | **E-Ink Paper** |
| Soft UI playful / materiales infantiles con contraste controlado | **Neumorphism** |
| Animaciones coreografiadas / hero con motion | **Motion-Driven** |
| Feedback sutil / quiz con respuesta animada | **Micro-interactions** |
| Interfaz minimalista ambiental / voz/gesto | **Zero Interface** |
| Asistente IA / chat-first / workflow conversacional | **AI-Native UI** |
| Portfolio con cursor custom / experiencia puntero-centric | **Interactive Cursor** |

**Elegir preset (flujo canónico v5.4):**
1. Abrir catalogo visual: `open ~/.dotfiles/ai/skills/adri-style/assets/preset-catalog.html`
2. El usuario elige visualmente el preset que quiere
3. **Copiar `templates/bootstrap-adri.html` como punto de partida** (default Bold Signal):
   ```bash
   cp ~/.dotfiles/ai/skills/adri-style/templates/bootstrap-adri.html mi-output.html
   ```
4. Si el preset elegido NO es Bold Signal: sustituir en el bootstrap el bloque `<!-- preset: NN-name -->`, las `<link>` de fuentes y el `:root` completo por los del preset elegido en `references/style-presets.md` (sección "Audit v5.4" valida los pesos permitidos).
5. Actualizar `data-preset="NN-name"` en `<html>` para que `audit-adri.sh` reconozca el uso justificado de la fuente.
6. Antes de publicar: `~/.dotfiles/ai/skills/adri-style/scripts/audit-adri.sh mi-output.html` debe devolver exit 0.

### Nuevo proyecto web
1. **Elegir preset** → Paso 0 (arrancar de `templates/bootstrap-adri.html`)
2. Layout y container → `references/layout.md`
3. Componentes necesarios → `references/components.md`
4. Animaciones → `references/animation.md`
5. Verificar con checklist
6. Pasar `audit-adri.sh` antes de cerrar la entrega

### Dashboard educativo
1. **Elegir preset** → Minimalista Adri o Swiss Modern
2. Escala: ratio 1.125 (Major Second) para densidad
3. Cards y KPIs → `references/components.md`
4. Graficas: Chart.js con colores semanticos → `references/color-and-theme.md`
5. Tabular-nums obligatorio en todas las notas

### Presentacion HTML / Landing
1. **Elegir preset** → Bold Signal ★ (default Adri), Soffia Warm, Creative Voltage, etc.
2. Escala: ratio 1.333 (Perfect Fourth) para impacto visual
3. Layouts asimetricos: alternar left-heavy, right-heavy, centered
4. Patrones premium → `references/components.md` (glassmorphism, glow, bento grid)
5. Animaciones de entrada → `references/animation.md`
6. **Si el preset es Bold Signal**: consultar `references/identity-adri.md` para 10 animaciones HTML reutilizables (timeline, line/bar chart, comparativas A/B, procesos lineal/circular, causa-consecuencia, radial top-down, estructura literaria) + logo (relleno vs monoline) + opción de importar `tokens.css` directo del repo

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
- Activos reales primero cuando haya identidad reconocible: logo, producto, portada, foto, captura UI o documento original antes que gradientes, iconos genericos o siluetas CSS. Si no hay activos suficientes, usar placeholder honesto y pedirlos; no rellenar con decoracion.
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
- En piezas sobre marca/producto/lugar/obra concreta, verificar identidad visual antes de diseñar: logo si existe, imagen oficial o captura real, colores/fuentes solo como apoyo. No sustituir un producto real por una silueta dibujada ni una UI real por cajas abstractas.
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

**ANIMATIONS (guidance, no bloqueo — desde v5.2):**
- **Por defecto**: preferir `transform` y `opacity` (compositing layer, sin reflow), transitions 150-300ms para UI, respetar `prefers-reduced-motion`
- **Excepción documentada por preset**: presets como Motion-Driven, Kinetic Typography, Micro-interactions o Storytelling-Driven pueden animar propiedades físicas (`width`, `margin`, `clip-path`, `filter`), usar keyframes más largos (500ms–2s) o coreografías scroll-driven. Cada preset documenta su propia política en la sección del preset
- **Siempre**: envolver animaciones no esenciales en `@media (prefers-reduced-motion: reduce) { animation: none; transition: none; }`

**CONSIDER:**
- Clase .prose para bloques de lectura (max-width: 65ch)
- Breakpoints 900px y 600px para responsive
- Border-radius maximo 12px (excepto pills: 100px)
- Chart.js para graficas en dashboards y explicaciones visuales

## Quick Reference

| Propiedad | Valor |
|-----------|-------|
| Presets | 27 estilos en `references/style-presets.md` |
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

- `references/style-presets.md` — **27 presets visuales** con CSS variables completas (v5.2; 10 presets nuevos + sección Modifiers + reglas animation relajadas, 2026-04-14)
- `references/ux-guidelines.md` — **99 reglas UX transversales** importadas de UI UX Pro Max (2026-04-13). Consultar antes de finalizar una página
- `references/typography.md` — Sistema tipografico fluido, font pairing, escala Utopia, tipografia premium dark
- `references/composition.md` — Composicion dinamica: posicion de texto segun contenido visual
- `references/animation.md` — Easings, duracion, scale, blur, propiedades seguras (Emil Kowalski)
- `references/color-and-theme.md` — Variables tema dual, contraste, semaforo educativo (Butterick)
- `references/components.md` — Cards, botones, tags, header blur, **patrones premium dark mode, bento grid, anti-AI-slop** (NUEVO v5)
- `references/layout.md` — Grid, container, prose, responsive, breakpoints

## Assets

- `assets/global.css` — Template CSS base para copiar en nuevos proyectos (default: Minimalista Adri)
- `assets/base.css` — CSS base inyectable con reset, tipografia fluida, tema dual y componentes base (NUEVO v5)

## Export a DESIGN.md (interoperabilidad)

> **`DESIGN.md` es canal, no fuente.** `adri-style` sigue siendo la fuente canónica del sistema de diseño. Los `.design.md` exportados son artefactos portables para herramientas externas; no se reimportan automáticamente. Ver `references/design-md-spec.md` para el subset compatible Google/Stitch + extensiones Adri, la convención de tokens/hex en `components:` y el validador Python.

Sub-comando para emitir un preset como fichero `DESIGN.md` compatible con el spec canónico de [google-labs-code/design.md](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) — útil cuando otro agente (Stitch, Cursor, Copilot, Antigravity) necesita consumir el sistema de diseño sin conocer la sintaxis CSS del preset.

```bash
# Listar presets disponibles (slugs)
python3 ~/.dotfiles/ai/skills/adri-style/scripts/export.py --list

# Exportar un preset (default output: exports/<slug>.design.md)
python3 ~/.dotfiles/ai/skills/adri-style/scripts/export.py --preset=bold-signal
python3 ~/.dotfiles/ai/skills/adri-style/scripts/export.py --preset=paper-and-ink

# Override de output path o emitir a stdout
python3 .../scripts/export.py --preset=bold-signal --output=/tmp/bs.design.md
python3 .../scripts/export.py --preset=bold-signal --stdout
```

**Mapping CSS → DESIGN.md:**

| CSS variable | Campo frontmatter |
|--------------|-------------------|
| `--font-display/body/mono` | `typography.{display,body,mono}.fontFamily` |
| `--lh-display/body`        | `typography.{display,body}.lineHeight` |
| `--bg* / --text* / --accent*` | `colors.*` (HSL convertido a hex sRGB; alpha conservado en nota) |
| `--border` | `colors.border` |
| `--radius` | `rounded.base` |

Secciones markdown emitidas en el orden canónico del spec: Overview · Colors · Typography · Layout · Elevation & Depth · Shapes · Components · Do's and Don'ts.

**Presets validados como piloto**: `bold-signal` (sans máximo contraste) + `paper-and-ink` (serif editorial). Cualquier preset del catálogo funciona; estos dos se usaron para asegurar varianza estructural (fonts sans vs serif, radius 0 vs 6, paleta neutra vs cálida tostada).
