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
2. **Cargar las fuentes exactas del preset declarado** según
   `references/presets.json`. Si `single_font=true`, una familia es correcta;
   si es `false`, display y body deben estar cargadas.
3. **Accesibilidad y semántica**: contraste AA, foco visible, nombres
   accesibles, teclado y estructura HTML prevalecen sobre cualquier receta
   visual.
4. **Iconos UI: Lucide SVG inline**. Nunca emojis como sustituto de iconos;
   los emojis de contenido sí son válidos.
5. **Movimiento**: si existe animación no esencial, respetar
   `prefers-reduced-motion`.
6. **Test de la Caja (EAR)**: cada caja con
   `background+border+border-radius` debe ser **E**s accionable, **A**grupa
   contenido heterogéneo o **R**epresenta un dato discreto. Si no pasa ninguna
   prueba, va sin caja.

El preset, el tema, la densidad y la composición dependen de la superficie.
Bold Signal es el default de identidad para piezas públicas firmadas y una
heurística cuando el contexto es ambiguo; no es un invariante universal.

Si existe toggle de tema, el icono representa la **acción**: luna en light
(`Activar modo oscuro`) y sol en dark (`Activar modo claro`).

Fuente estructurada canónica: `references/presets.json`. La referencia humana
`references/style-presets.md`, el catálogo y los exports deben validarse o
generarse contra ella.

<!-- /PRESCRIPTIVE-PATTERN -->

# Adri Style v5.8 - Sistema de Diseño Personal

Sistema de diseño con 27 presets visuales, tipografia fluida y layouts expresivos.
Referencia: [adri-app.com](https://adri-app.com).
Fuentes: Butterick (tipografia), Utopia (escala fluida), Vercel Geist (tokens), Emil Kowalski (animaciones), Linear/Vercel (dark mode profundidad), Refactoring UI (tinted grays), Impeccable (anti-patterns AI-tell).

## Parche transversal PRO-211 (2026-07-18)

Precedencia obligatoria:

1. Accesibilidad y semántica.
2. Contrato de la superficie.
3. Identidad y tokens del preset.
4. Heurísticas.
5. Recetas decorativas opcionales.

“Less, but better” aplica como criterio de reducción: ninguna receta añade
componentes, visualizaciones, layouts o decoración que el contenido no
necesita.

## Changelog v5.7 → v5.8

**Consolidación PRO-211 (2026-07-18):** `presets.json` pasa a ser el
contrato estructurado canónico; `validate_contract.py` bloquea preset o fuentes
incoherentes antes de la auditoría opcional; el catálogo se genera desde ese
contrato; identidad, superficie y decoración quedan separados.

**Integración P4 (2026-05-09):**

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

Eliminada la duplicación de catálogo entre `audit-adri.sh` (case bash con 27 entries) y `references/style-presets.md` (tabla canónica humana). Desde PRO-211, `references/presets.json` es el contrato estructurado autoritativo.

- **`references/presets.json` (NUEVO)**: schema 1.0 con los 27 presets. Por cada uno: id, n, name, fonts (display/body/single_font/justifications/weights), color (bg/accent), mode_default, estado, uso_real. La referencia humana explica intención y CSS; no redefine el contrato.
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
3. En una página web general, copiar `templates/bootstrap-adri.html` como punto de partida (default Bold Signal). En Console, galería, dashboard o presentación, partir del fixture o skill propietario de esa superficie:
   ```bash
   cp ~/.dotfiles/ai/skills/adri-style/templates/bootstrap-adri.html mi-output.html
   ```
4. Si el preset elegido NO es Bold Signal: sustituir en el bootstrap el bloque `<!-- preset: NN-name -->`, las `<link>` de fuentes y el `:root` completo por los del preset elegido en `references/style-presets.md` (sección "Audit v5.4" valida los pesos permitidos).
5. Actualizar `data-preset="NN-name"` en `<html>` para que `audit-adri.sh` reconozca el uso justificado de la fuente.
6. Antes de publicar: `~/.dotfiles/ai/skills/adri-style/scripts/audit-adri.sh mi-output.html` debe devolver exit 0. Exit 2 significa infraestructura incompleta, nunca aprobación.

### Nuevo proyecto web
1. **Elegir preset** → Paso 0 (arrancar de `templates/bootstrap-adri.html`)
2. Layout y container → `references/layout.md`
3. Componentes necesarios → `references/components.md`
4. Animaciones → `references/animation.md`
5. Verificar con checklist
6. Pasar `audit-adri.sh` antes de cerrar la entrega

### Dashboard educativo
1. **Elegir preset** → el que fije `dashboard-educativo`; sin contrato propietario, considerar Soffia Warm, Minimalista Adri o Swiss Modern
2. Escala: ratio 1.125 (Major Second) para densidad
3. KPIs, tablas y gráficos necesarios → `references/components.md`; no convertir cada dato en card
4. Graficas: Chart.js con colores semanticos → `references/color-and-theme.md`
5. Tabular-nums obligatorio en todas las notas

### Presentacion HTML / Landing
1. **Elegir preset** → Bold Signal ★ (default Adri), Soffia Warm, Creative Voltage, etc.
2. Escala: ratio 1.333 (Perfect Fourth) para impacto visual
3. Cada slide presenta una idea y cabe en 100vw × 100vh; la landing usa scroll natural.
4. Variar composición cuando lo exija el contenido, no por cuota.
5. Patrones premium y animaciones solo si apoyan la narrativa y el preset.
6. **Si el preset es Bold Signal**: consultar `references/identity-adri.md` para 10 animaciones HTML reutilizables (timeline, line/bar chart, comparativas A/B, procesos lineal/circular, causa-consecuencia, radial top-down, estructura literaria) + logo (relleno vs monoline) + opción de importar `tokens.css` directo del repo

### Documento / contenido de lectura
1. **Elegir preset** → Paper & Ink o Notebook Tabs
2. Clase .prose → `references/typography.md` (65ch, line-height 1.5)
3. Colores suaves → `references/color-and-theme.md`

## Reglas core

**Invariantes:**

- Declarar preset y cargar sus fuentes canónicas.
- Mantener contraste AA, foco, teclado, labels y HTML semántico.
- Aplicar EAR a toda caja.
- Usar Lucide para iconos UI y `prefers-reduced-motion` cuando haya motion.
- Usar `tabular-nums` en datos numéricos comparables.

**Por superficie o preset:**

- Tema inicial, tema dual y toggle.
- Pareja tipográfica o single-font.
- Densidad, ancho, scroll, viewport-fit y breakpoints.
- Escala dramática, hero, tabs, bento, sombras, gradientes y motion.
- Visualizaciones: solo cuando representan datos o explican una relación.

**Heurísticas:**

- Escala fluida, `text-wrap: balance`, activos reales y jerarquía clara.
- Variar layout cuando mejora la lectura; no cumplir cuotas numéricas.
- Más de ocho cajas redondeadas visibles sugiere revisar EAR, no implica fallo.
- En fondos oscuros, preferir near-black y contraste medido.

**Eliminar como requisito:**

- SVG decorativo obligatorio.
- Mínimos de componentes, layouts o niveles tipográficos.
- Eyebrows, números gigantes, gradientes o splits universales.
- Cuerpo a 40–45 % de opacidad: sustituir por contraste AA verificable.

**IMÁGENES PROTAGONISTAS (contenido visual educativo):**
- Usar imágenes reales cuando el contenido lo pida: fotos de autores, portadas de libros, ilustraciones de época
- En piezas sobre marca/producto/lugar/obra concreta, verificar identidad visual antes de diseñar: logo si existe, imagen oficial o captura real, colores/fuentes solo como apoyo. No sustituir un producto real por una silueta dibujada ni una UI real por cajas abstractas.
- En un split imagen+texto, asignar espacio según la importancia real de cada parte; 55/45 es una receta posible, no un contrato.
- Imágenes con `object-fit: cover`, `border-radius: var(--radius)`, sombra sutil con border
- Placeholder si no hay imagen real: fondo tintado con icono Lucide SVG grande (no cuadrado gris vacío)
- En contenido literario/editorial: las imágenes aportan contexto visual — NO son decoración

**EJERCICIOS INTERACTIVOS (receta cuando existe texto fuente + varias actividades):**
- Mantener el fragmento accesible mientras se responde; `sticky` es una opción si no roba viewport.
- Usar pestañas solo cuando reducen carga cognitiva y conservan estado.
- Evitar scroll interno salvo que la superficie lo necesite.
- Dar feedback accesible inmediato al comprobar; el color no puede ser la única señal.

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
- Mismo font-family para display y body cuando `single_font=false` en el contrato
- padding: var(--space-2xl) en 4+ secciones uniformemente (falta jerarquia de espaciado)
- h2 { margin-top: var(--space-xl) } global cuando las secciones ya tienen padding grande
- Footer margin-top: var(--space-xl) o mayor

**NEVER (anti-AI-slop — ver `references/components.md` § ANTI-AI-SLOP):**
- `bg-indigo-500` ni purple gradients genericos (Tailwind default, cada IA genera esto)
- 3 cards identicas con icono en grid como layout principal (el layout mas generico)
- Inter como única fuente salvo que el preset declare `single_font=true`
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
| Container | Depende de la superficie |
| Prose | max-width: 65ch |
| Radio | Según preset y función |
| Transicion | 0.2s ease |
| Line-height body | 1.55 (dark), 1.5 (light) |
| Line-height titles | 1.05 |
| Letter-spacing titles | -0.04em (dark), -0.03em (light) |
| Grays | Siempre tinted: hsl(210, 15%, N%) o hsl(30, 8%, N%) |
| Body text dark | #E8E8E8 off-white (no #FFFFFF puro) |

## Checklist de revision

- [ ] Escala fluida con --step-* (no px fijos)
- [ ] Fontes cargadas con display=swap
- [ ] Roles tipográficos necesarios definidos; display/body respetan el contrato
- [ ] Tema y toggle solo si la superficie los necesita
- [ ] Datos numericos con font-mono + tabular-nums
- [ ] Layout y densidad responden a la superficie
- [ ] Visuales solo cuando aportan información
- [ ] Responsive proporcional al contenido
- [ ] Motion sigue el preset y respeta reduced-motion
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

- `assets/global.css` — Template legacy; no usar para outputs nuevos
- `assets/base.css` — Base legacy con decisiones de Minimalista Adri; no es un contrato universal
- `assets/preset-catalog.html` — Catálogo generado desde `presets.json`

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
