# Identity Adri — Marca personal + animaciones

Sistema de identidad visual personal (logo, tokens compartidos, 10 animaciones HTML reutilizables). Es la materialización del preset **Bold Signal** (Default Adri) en assets concretos importables.

- **Brandbook live**: https://branding-adri.adrianlaureda.workers.dev/
- **Repo local**: `~/Proyectos/Claude/config/branding-adri/`
- **Repo GitHub**: `git@github.com:adrianlaureda/claude-branding-adri.git` (privado)
- **Tipografía cuerpo**: Inter **300** (fina) — discrepancia explícita con Inter default 400
- **Tipografía display**: Satoshi 900
- **Geometría**: ángulos rectos (`--radius: 0`)

## Cuándo invocar esta reference

Esta reference se consulta cuando:
- El proyecto necesita **logo** (favicon, header, footer, presentación firmada).
- Se busca **animación HTML reutilizable** (timeline, charts, procesos, comparativas).
- Se quiere **tokens.css importable** en vez de copiar variables CSS sueltas (proyectos pequeños, prototipos rápidos, slides standalone).
- Se necesita confirmar **paleta o pesos exactos** del brandbook live.

NO se consulta para definir presets nuevos ni para layouts/tipografía generales — eso lo cubre `style-presets.md`, `layout.md`, `typography.md`.

## Logo

Dos variantes en `~/Proyectos/Claude/config/branding-adri/assets/`:

| Archivo | Forma | Cuándo usar |
|---------|-------|-------------|
| `logo.svg` | Triángulo prisma 3D, **relleno** | Marca principal, hero, header, splash, favicon ≥32px |
| `logo-monoline.svg` | Triángulo, **outline** monoline | Marca discreta, watermark, footer, favicon pequeño, contextos donde el relleno compite con la tipografía |

**Sincronía con React**: el logo también vive en `apps/adri-react/src/components/Logo.tsx`. Cualquier cambio del SVG debe replicarse en ambos sitios para mantener consistencia entre el portfolio React y el brandbook.

## Importar tokens.css directo (alternativa rápida)

En lugar de copiar las variables CSS del preset Bold Signal a un archivo nuevo, se puede importar `tokens.css` directamente del repo. Útil para prototipos, slides standalone o componentes aislados.

```html
<link rel="stylesheet" href="../../../Proyectos/Claude/config/branding-adri/tokens.css">
```

O via URL live (si el proyecto vive online):

```html
<link rel="stylesheet" href="https://branding-adri.adrianlaureda.workers.dev/tokens.css">
```

Lo que aporta `tokens.css`:
- Inter variable self-hosted (300/400/500/600/700) + Satoshi via Fontshare CDN
- Light por defecto + dark via `[data-theme="dark"]`
- 6 acentos opcionales (`<body class="accent-azul">`, `accent-violeta`, `accent-verde`, `accent-naranja`, `accent-cyan`, `accent-rosa`)
- 5 utilidades tipográficas (`.t-overline`, `.t-section`, `.t-display`, `.t-h2`, `.t-mono`)
- Reset mínimo + accesibilidad (`prefers-reduced-motion`, `:focus-visible`, `::selection`)

## Catálogo de 10 animaciones HTML

10 animaciones standalone en `~/Proyectos/Claude/config/branding-adri/animations/`. Cada una es **autocontenida** (CSS + JS inline), respeta `prefers-reduced-motion: reduce`, tiene tema dual con persistencia en `localStorage` y un botón **↻ Reproducir** para relanzar la coreografía sin recargar.

| # | Patrón | Caso típico |
|---|--------|-------------|
| 01 | Timeline vertical | Historia, biografía, evolución personal/colectiva |
| 02 | Timeline horizontal | Roadmap, programación trimestral, fases de proyecto |
| 03 | Line chart SVG | Evolución de notas, métricas longitudinales |
| 04 | Bar chart | Comparativa por grupo, evaluación, encuestas |
| 05 | Comparativa A vs B | "Antes vs después", método A vs método B |
| 06 | Proceso lineal | Pipeline didáctico, pasos secuenciales |
| 07 | Proceso circular | Ciclo de evaluación, rueda PDCA, fases iterativas |
| 08 | Causa-consecuencia | Análisis del "por qué" de un fenómeno |
| 09 | Radial top-down | Mapa conceptual, taxonomía, jerarquía |
| 10 | Estructura literaria | Pirámide de Freytag, narrativa cíclica, tres actos |

**Ruta canónica**: `~/Proyectos/Claude/config/branding-adri/animations/0X-<nombre>.html`
**URL live**: `https://branding-adri.adrianlaureda.workers.dev/animations/0X-<nombre>` (sin `.html`, redirect 307→200)

### Cómo reutilizar una animación

```bash
cp ~/Proyectos/Claude/config/branding-adri/animations/03-line-chart.html mi-proyecto/
# Ajusta el <link> a tokens.css según tu ruta relativa
# Edita el bloque `const DATA = [...]` al inicio del <script> con tus datos
```

### Cuándo embeber vs cuándo enlazar

- **Embeber** (copiar HTML al slide / lección): cuando la animación es protagonista y vive dentro de la presentación. Se modifican los datos directamente.
- **Enlazar al live** (`<iframe>` a la URL pública): cuando se quiere mostrar la versión canónica del brandbook como referencia visual sin tocar datos.

### Tips por skill consumidor

- **`presentacion-html`**: embeber la animación dentro de un slide full-viewport (sin scroll). La animación ya respeta viewport fitting porque es autocontenida y usa `min-height: 100vh`.
- **`contenido-a-leccion`**: usar como hook visual al inicio de un capítulo o como remate al final de un bloque conceptual.
- **`dashboard-educativo`**: 03 (line chart) y 04 (bar chart) son embebibles directos como widgets del dashboard. 07 (proceso circular) como visualización de "ciclo de evaluación".
- **`video-educativo`**: capturar la animación con HyperFrames + screenshot timing → b-roll para el vídeo.

## Acentos por dominio (overlay sobre Bold Signal)

Cuando el proyecto necesita **un punto de color** sin abandonar la marca neutra de Bold Signal, aplicar un acento via clase en `<body>`:

```html
<body class="accent-azul">      <!-- educativo / informativo -->
<body class="accent-violeta">   <!-- creatividad / brainstorming -->
<body class="accent-verde">     <!-- éxito / nutrición / progreso -->
<body class="accent-naranja">   <!-- urgente / alerta cálida -->
<body class="accent-cyan">      <!-- técnico / data -->
<body class="accent-rosa">      <!-- emocional / cuidado / familia -->
```

Solo cambia `--accent` y `--accent-surface`. Tipografía, layout y geometría se mantienen idénticos al brandbook.

## Mantenimiento

- **Cambios al brandbook live**: requieren `wrangler deploy` manual. NO hay auto-deploy on push (Workers Static Assets, no Pages).
- **Tokens son fuente única**: cualquier proyecto que importe `tokens.css` hereda automáticamente cambios futuros.
- **Animaciones nuevas**: añadir en `animations/` numeradas correlativamente, registrar en `index.html` (sección "Animaciones") y actualizar la tabla de esta reference.
