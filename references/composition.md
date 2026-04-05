# Composicion dinamica

Principio: cada seccion/slide tiene su propia logica compositiva. La posicion del texto depende de lo que haya en el resto de la pantalla, no de un patron predefinido.

## Regla fundamental

> El texto se coloca donde el contenido visual lo necesite, no donde una plantilla lo dicte.

Antes de colocar texto, preguntarse:
1. Que elemento visual domina esta seccion? (grafica, imagen, diagrama, tabla, nada)
2. Donde tiene ese elemento su zona de interes? (centro, lateral, parte superior)
3. Donde queda espacio natural para texto sin competir con el visual?
4. Cual es el flujo de lectura natural? (Z-pattern, F-pattern, punto focal)

## Patrones compositivos (elegir segun contenido)

### 1. Visual dominante + texto acompañante

Cuando hay una grafica, diagrama o imagen que es el elemento principal.

```
+---------------------------+     +---------------------------+
| Titulo                    |     |        [GRAFICA]          |
|                           |     |                           |
|   [GRAFICA GRANDE]        |     +---------------------------+
|                           |     | Titulo                    |
| Parrafo explicativo       |     | Texto que explica lo que  |
| debajo de la grafica      |     | se ve arriba              |
+---------------------------+     +---------------------------+

+---------------------------+     +---------------------------+
| Titulo    |               |     |               | Titulo    |
| y texto   | [GRAFICA]     |     | [GRAFICA]     | y texto   |
| a la izq  |               |     |               | a la dcha |
|           |               |     |               |           |
+---------------------------+     +---------------------------+
```

**Regla:** el texto nunca compite con el visual por atencion. Si la grafica es compleja (muchos datos), el texto debe ser minimo. Si la grafica es simple, el texto puede extenderse.

### 2. Texto protagonista (sin visual o visual decorativo)

Cuando el contenido es conceptual y no hay visual explicativo.

```
+---------------------------+     +---------------------------+
|                           |     |     [icono decorativo]    |
|     Titulo grande         |     |                           |
|     centrado              |     |  Titulo alineado izquierda|
|                           |     |                           |
|     Parrafo breve         |     |  Parrafo con mucho        |
|     tambien centrado      |     |  whitespace a la derecha  |
|                           |     |                           |
+---------------------------+     +---------------------------+
```

**Regla:** usar tamaño tipografico grande (--step-4 o --step-5) para llenar el espacio. El whitespace generoso ES el diseño.

### 3. Comparativa / datos enfrentados

Cuando se comparan dos conceptos, antes/despues, pros/contras.

```
+---------------------------+     +---------------------------+
| [Concepto A]  | [Concepto B]   | Titulo                    |
|               |                 |                           |
| Texto         | Texto           | [Dato] [Dato] [Dato]     |
| descriptivo   | descriptivo     | [Dato] [Dato] [Dato]     |
|               |                 |                           |
| [metrica]     | [metrica]       | Texto resumen debajo     |
+---------------------------+     +---------------------------+
```

### 4. Secuencia / flujo

Cuando se explica un proceso paso a paso.

```
+---------------------------+
|  [1] -----> [2] -----> [3]|
|                           |
|  Texto      Texto     Texto|
|  paso 1     paso 2    paso3|
+---------------------------+

+---------------------------+
|  [1] Primer paso          |
|      Explicacion          |
|          |                |
|  [2] Segundo paso         |
|      Explicacion          |
|          |                |
|  [3] Tercer paso          |
+---------------------------+
```

### 5. Quote / destacado

Cuando una cita o dato impactante es lo central.

```
+---------------------------+
|                           |
|                           |
|    "Cita textual grande   |
|     en step-3 o step-4"  |
|                           |
|         — Autor           |
|                           |
+---------------------------+
```

## Principios de composicion

### Peso visual
- Imagenes y graficas pesan mas que texto
- Texto grande (hero) pesa mas que texto pequeño
- Color pesa mas que gris
- Elementos densos (tablas) pesan mas que elementos aireados

### Balance asimetrico
- NO buscar simetria perfecta — buscar equilibrio dinamico
- Un elemento grande a la izquierda se equilibra con varios pequeños a la derecha
- El whitespace es un elemento mas: "pesa" y equilibra

### Flujo de lectura
- Occidental: de izquierda a derecha, de arriba a abajo
- El ojo entra por el elemento de mayor peso visual
- Despues sigue la jerarquia tipografica (titulo → subtitulo → body)
- Los elementos visuales (graficas, iconos) actuan como puntos de anclaje

### Relacion texto-visual

| Tipo de visual | Posicion del texto | Tamaño del texto |
|----------------|-------------------|-----------------|
| Grafica compleja (muchos datos) | Debajo o lateral minimo | Pequeño (step--1 a step-0) |
| Grafica simple (1 metrica) | Al lado, mismo tamaño | Grande (step-2 a step-3) |
| Imagen decorativa | Superpuesto o adyacente | Libre |
| Diagrama/flujo | Debajo explicando | Medio (step-0) |
| Tabla de datos | Arriba como titulo | Medio-grande (step-1 a step-2) |
| Nada (solo texto) | Libre, usar whitespace | Grande (step-3 a step-5) |
| Icono conceptual | Al lado del icono | Medio (step-1) |

## Implementacion CSS

### Grid flexible (no fijar columnas)

```css
/* Seccion con visual lateral */
.section-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-l);
  align-items: center;
}

/* Visual dominante arriba, texto abajo */
.section-visual-top {
  display: grid;
  grid-template-rows: 2fr 1fr;
  gap: var(--space-m);
}

/* Texto asimetrico con whitespace */
.section-asymmetric {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--space-xl);
}

/* Responsive: todo apila en movil */
@media (max-width: 600px) {
  .section-split,
  .section-asymmetric {
    grid-template-columns: 1fr;
  }
}
```

### Posicionamiento contextual

```css
/* Texto que se adapta al visual */
.text-alongside-chart {
  align-self: end;          /* Alinear abajo si la grafica es alta */
}
.text-above-visual {
  padding-bottom: var(--space-s);  /* Espacio antes del visual */
}
.text-overlay {
  position: relative;
  z-index: 1;               /* Sobre imagen decorativa */
}
```

## Layout recipes

Patrones concretos con CSS completo. Usar variables del sistema (--space-*, --step-*, --bg, --bg-surface, --border, --text, --radius).

### Recipe 1: Spotlight grid (1 grande + N pequeños)

El primer item destaca ocupando 2 columnas y 2 filas. El resto rellena las celdas restantes. Ideal para features donde una es protagonista, portfolios, o dashboards con KPI principal.

```
+-------------------+--------+
|                   | [item] |
|   [SPOTLIGHT]     +--------+
|                   | [item] |
+--------+----------+--------+
| [item] | [item]   | [item] |
+--------+----------+--------+
```

```css
.spotlight-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto auto;
  gap: var(--space-m);
}

.spotlight-grid > :first-child {
  grid-column: 1 / 3;
  grid-row: 1 / 3;
  min-height: 20rem;
}

.spotlight-grid > :not(:first-child) {
  min-height: 9rem;
}

/* Card base para items del grid */
.spotlight-grid > * {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-m);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.spotlight-grid > :first-child {
  font-size: var(--step-2);
}

@media (max-width: 900px) {
  .spotlight-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .spotlight-grid > :first-child {
    grid-column: 1 / -1;
    grid-row: auto;
  }
}

@media (max-width: 600px) {
  .spotlight-grid {
    grid-template-columns: 1fr;
  }
}
```

---

### Recipe 2: Asymmetric split (2fr + 1fr)

Lado principal con contenido denso + sidebar con visual o datos complementarios. Funciona en ambas direcciones.

```
+------------------+--------+    +--------+------------------+
| Titulo           |        |    |        | Titulo           |
|                  | Visual |    | Visual |                  |
| Parrafos de      | o dato |    | o dato | Parrafos de      |
| contenido        | lateral|    | lateral| contenido        |
+------------------+--------+    +--------+------------------+
```

```css
/* Texto a la izquierda, visual a la derecha */
.split-2-1 {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--space-l);
  align-items: start;
}

/* Texto a la derecha, visual a la izquierda */
.split-1-2 {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: var(--space-l);
  align-items: start;
}

.split-2-1 > .content,
.split-1-2 > .content {
  font-size: var(--step-0);
  line-height: 1.5;
}

.split-2-1 > .aside,
.split-1-2 > .aside {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-m);
}

@media (max-width: 900px) {
  .split-2-1,
  .split-1-2 {
    grid-template-columns: 1fr;
  }
  /* En movil, el aside va debajo sin importar el orden visual */
  .split-1-2 > .aside {
    order: 1;
  }
}
```

---

### Recipe 3: Hero con fila de metricas

Titulo grande + subtitulo arriba, fila de 3-4 stat cards debajo. Para dashboards, landing pages y secciones de apertura con datos clave.

```
+----------------------------------+
|                                  |
|        Titulo grande             |
|        Subtitulo                 |
|                                  |
+--------+--------+--------+------+
| [stat] | [stat] | [stat] |[stat]|
+--------+--------+--------+------+
```

```css
.hero-metrics {
  display: flex;
  flex-direction: column;
  gap: var(--space-l);
}

.hero-metrics > .hero-text {
  text-align: center;
  padding: var(--space-xl) 0 var(--space-m);
}

.hero-metrics > .hero-text h1 {
  font-size: var(--step-5);
  font-family: var(--font-display);
  line-height: 1.1;
  text-wrap: balance;
}

.hero-metrics > .hero-text p {
  font-size: var(--step-1);
  color: var(--text-secondary);
  margin-top: var(--space-s);
  max-width: 50ch;
  margin-inline: auto;
}

.metrics-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(10rem, 1fr));
  gap: var(--space-m);
}

.metric-card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-m);
  text-align: center;
}

.metric-card .value {
  font-size: var(--step-3);
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}

.metric-card .label {
  font-size: var(--step--1);
  color: var(--text-secondary);
  margin-top: var(--space-3xs);
}

@media (max-width: 600px) {
  .metrics-row {
    grid-template-columns: repeat(2, 1fr);
  }
  .hero-metrics > .hero-text h1 {
    font-size: var(--step-4);
  }
}
```

---

### Recipe 4: Content + sidebar

Contenido principal (prose) con sidebar de navegacion o datos complementarios. Sidebar sticky en desktop, colapsa a bloque en movil. Para documentacion, articulos largos, guias.

```
+---------------------+-----------+
| Contenido principal | Sidebar   |
| (prose, max 65ch)   | (sticky)  |
|                     |           |
| Parrafos de texto   | - Nav     |
| con heading, listas | - Links   |
| y visuales inline   | - TOC     |
+---------------------+-----------+
```

```css
.content-sidebar {
  display: grid;
  grid-template-columns: 1fr 16rem;
  gap: var(--space-xl);
  align-items: start;
}

.content-sidebar > .main {
  max-width: 65ch;
  font-size: var(--step-0);
  line-height: 1.5;
}

.content-sidebar > .main h2 {
  font-size: var(--step-2);
  margin-top: var(--space-l);
  margin-bottom: var(--space-s);
}

.content-sidebar > .sidebar {
  position: sticky;
  top: var(--space-l);
}

.content-sidebar > .sidebar nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
  font-size: var(--step--1);
}

.content-sidebar > .sidebar nav a {
  color: var(--text-secondary);
  text-decoration: none;
  padding: var(--space-3xs) var(--space-xs);
  border-left: 2px solid var(--border);
  transition: color var(--transition), border-color var(--transition);
}

.content-sidebar > .sidebar nav a:hover,
.content-sidebar > .sidebar nav a.active {
  color: var(--text);
  border-left-color: var(--text);
}

@media (max-width: 900px) {
  .content-sidebar {
    grid-template-columns: 1fr;
  }
  .content-sidebar > .sidebar {
    position: static;
    order: -1; /* Nav va arriba en movil */
    border-bottom: 1px solid var(--border);
    padding-bottom: var(--space-m);
    margin-bottom: var(--space-m);
  }
  .content-sidebar > .sidebar nav {
    flex-direction: row;
    flex-wrap: wrap;
  }
  .content-sidebar > .sidebar nav a {
    border-left: none;
    border-bottom: 2px solid var(--border);
  }
}
```

---

### Recipe 5: Alternating sections (zigzag)

Secciones que alternan visual izquierda/derecha para crear ritmo visual al hacer scroll. Seccion A: imagen izquierda + texto derecha. Seccion B: texto izquierda + imagen derecha.

```
+--[VISUAL]--+--[TEXTO]---+
|             |            |
+--[TEXTO]---+--[VISUAL]--+
|             |            |
+--[VISUAL]--+--[TEXTO]---+
|             |            |
```

```css
.alternating-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-l);
  align-items: center;
  padding: var(--space-l) 0;
}

/* Cada seccion par invierte el orden */
.alternating-section:nth-child(even) > .visual {
  order: 1;
}

.alternating-section > .visual {
  border-radius: var(--radius);
  overflow: hidden;
  aspect-ratio: 4/3;
  background: var(--bg-surface);
  border: 1px solid var(--border);
}

.alternating-section > .visual img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.alternating-section > .text h2 {
  font-size: var(--step-3);
  font-family: var(--font-display);
  line-height: 1.15;
  margin-bottom: var(--space-s);
}

.alternating-section > .text p {
  font-size: var(--step-0);
  color: var(--text-secondary);
  line-height: 1.5;
  max-width: 45ch;
}

/* Separador sutil entre secciones */
.alternating-section + .alternating-section {
  border-top: 1px solid var(--border);
}

@media (max-width: 900px) {
  .alternating-section {
    grid-template-columns: 1fr;
  }
  /* En movil, visual siempre arriba */
  .alternating-section > .visual {
    order: -1 !important;
  }
  .alternating-section > .text {
    text-align: center;
  }
  .alternating-section > .text p {
    max-width: none;
  }
}
```

---

### Recipe 6: Bento grid

Grid con celdas de tamaños mixtos: algunas 2x2, otras 1x1, otras 1x2 horizontal. Para feature showcases, portfolios, o resumen de capacidades.

```
+----------+----------+----------+
|          |          |          |
|  [2x2]   | [1x1]   |  [1x2   |
|          +----------+  horiz] |
|          | [1x1]   |          |
+----------+----------+----------+
| [1x1]   | [1x1]   | [1x1]    |
+----------+----------+----------+
```

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(10rem, auto);
  gap: var(--space-m);
}

.bento-grid > * {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-m);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: var(--space-xs);
  overflow: hidden;
}

/* Celdas que ocupan mas espacio */
.bento-grid > .span-2x2 {
  grid-column: span 2;
  grid-row: span 2;
}

.bento-grid > .span-h {
  grid-column: span 2;
}

.bento-grid > .span-v {
  grid-row: span 2;
}

/* Tipografia segun tamaño de celda */
.bento-grid > .span-2x2 h3 {
  font-size: var(--step-3);
}

.bento-grid > :not(.span-2x2) h3 {
  font-size: var(--step-1);
}

.bento-grid p {
  font-size: var(--step--1);
  color: var(--text-secondary);
  line-height: 1.4;
}

/* Celda con icono decorativo */
.bento-grid .bento-icon {
  font-size: var(--step-4);
  color: var(--text-muted);
  margin-bottom: auto; /* Empuja contenido abajo */
}

@media (max-width: 900px) {
  .bento-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .bento-grid > .span-2x2 {
    grid-column: 1 / -1;
    grid-row: span 1;
  }
  .bento-grid > .span-h {
    grid-column: 1 / -1;
  }
}

@media (max-width: 600px) {
  .bento-grid {
    grid-template-columns: 1fr;
  }
  .bento-grid > .span-2x2,
  .bento-grid > .span-h,
  .bento-grid > .span-v {
    grid-column: auto;
    grid-row: auto;
  }
}
```

---

### Recipe 7: Timeline + content

Timeline vertical a la izquierda con linea conectora, tarjetas de contenido a la derecha. Para cronologias, procesos, roadmaps, historias.

```
      |
  [o]-+--- [Contenido paso 1]
      |
  [o]-+--- [Contenido paso 2]
      |
  [o]-+--- [Contenido paso 3]
      |
```

```css
.timeline-content {
  display: grid;
  grid-template-columns: 3rem 1fr;
  gap: 0 var(--space-m);
  position: relative;
}

/* Linea vertical continua */
.timeline-content::before {
  content: '';
  position: absolute;
  left: calc(1.5rem - 1px); /* Centrado en la columna de markers */
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--border);
}

/* Cada item es un par: marker + card */
.timeline-content > .tl-marker {
  display: flex;
  justify-content: center;
  padding-top: var(--space-m);
  position: relative;
  z-index: 1;
}

.timeline-content > .tl-marker::before {
  content: '';
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--bg);
  border: 2px solid var(--text-muted);
  flex-shrink: 0;
}

.timeline-content > .tl-marker.active::before {
  border-color: var(--text);
  background: var(--text);
}

.timeline-content > .tl-card {
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-m);
  margin-bottom: var(--space-m);
}

.timeline-content > .tl-card .tl-date {
  font-size: var(--step--1);
  color: var(--text-muted);
  font-family: var(--font-mono);
  margin-bottom: var(--space-2xs);
}

.timeline-content > .tl-card h3 {
  font-size: var(--step-1);
  margin-bottom: var(--space-xs);
}

.timeline-content > .tl-card p {
  font-size: var(--step-0);
  color: var(--text-secondary);
  line-height: 1.5;
}

@media (max-width: 600px) {
  .timeline-content {
    grid-template-columns: 2rem 1fr;
    gap: 0 var(--space-s);
  }
  .timeline-content::before {
    left: calc(1rem - 1px);
  }
  .timeline-content > .tl-marker::before {
    width: 10px;
    height: 10px;
  }
}
```

---

## Composition rules

Reglas duras para garantizar variedad visual y evitar monotonia.

### Variedad obligatoria

1. **NUNCA** usar el mismo patron de layout en 3 secciones consecutivas
2. Cada pagina debe usar **al menos 2 patrones de layout diferentes**
3. **Alternar** entre secciones text-heavy y visual-heavy
4. La primera seccion despues del hero **debe incluir un elemento visual** (grafica, imagen, grid, icono grande) — nunca solo texto
5. Cada seccion con datos densos necesita una **visualizacion** (grafica, chart, diagrama) — nunca solo una tabla

### Ritmo visual

6. Si una seccion es ancha (full-width grid), la siguiente debe ser estrecha (prose 65ch o split asimetrico)
7. Si una seccion tiene muchos elementos pequeños (grid 3-4 cols), la siguiente debe tener pocos elementos grandes (spotlight, hero, quote)
8. Los bloques de texto consecutivos sin visual no pueden superar 2 secciones

### Checklist de composicion

- [ ] Cada seccion tiene una razon para su layout (no "porque toca")
- [ ] El texto no compite con el visual — uno domina, el otro acompaña
- [ ] Hay variedad compositiva entre secciones consecutivas
- [ ] El whitespace es intencional, no accidental
- [ ] En movil, los elementos se reordenan logicamente
- [ ] Los datos numericos usan font-mono + graficas de apoyo
- [ ] Al menos 2 patrones de layout diferentes en la pagina
- [ ] No hay 3 secciones consecutivas con el mismo layout
- [ ] La primera seccion post-hero tiene un visual
- [ ] Secciones de datos incluyen visualizacion, no solo tablas
