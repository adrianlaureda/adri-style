# Componentes

Catalogo completo de componentes del sistema Adri Style.
Cada componente usa variables CSS del sistema (`--step-*`, `--space-*`, `--font-*`, `--bg-*`, `--text-*`, `--border`, `--accent`).
Principios: bordes (no sombras), transiciones sutiles, contraste moderado, `color-mix()` para superficies tintadas.

**Reglas universales:**
- `border: 1px solid var(--border)` — NUNCA `box-shadow`
- `border-radius: var(--radius)` (max 12px, 100px solo para pills)
- Hover: `transform` o `border-color` change
- `color-mix()` para tinted backgrounds
- `font-variant-numeric: tabular-nums` en datos numericos
- Lucide SVG: `stroke-width="1.5"`, `fill="none"`, `stroke="currentColor"`
- No gradientes, no emojis

---

## 1. STAT CARDS Y KPIs

### 1A. Stat card basico

Numero + etiqueta + indicador de cambio. Para KPIs individuales.

```html
<div class="stat-card">
  <span class="stat-label">Usuarios activos</span>
  <span class="stat-value">2,431</span>
  <span class="stat-change positive">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="14" height="14"><path d="m18 15-6-6-6 6"/></svg>
    +12.5%
  </span>
</div>
```

```css
.stat-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  transition: border-color var(--transition);
}
.stat-card:hover {
  border-color: var(--text-secondary);
}
.stat-label {
  font-size: var(--step--2);
  font-weight: 500;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.stat-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-3);
  font-weight: 600;
  line-height: 1.1;
}
.stat-change {
  display: inline-flex;
  align-items: center;
  gap: var(--space-3xs);
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step--2);
  font-weight: 500;
}
.stat-change.positive { color: #22c55e; }
.stat-change.negative { color: #ef4444; }
```

### 1B. Stat row (3-4 KPIs en linea con divisores)

Fila horizontal de metricas separadas por lineas verticales. Para dashboards y resumen de pagina.

```html
<div class="stat-row">
  <div class="stat-row-item">
    <span class="stat-row-value">1,234</span>
    <span class="stat-row-label">Ventas</span>
  </div>
  <div class="stat-row-divider"></div>
  <div class="stat-row-item">
    <span class="stat-row-value">45K</span>
    <span class="stat-row-label">Ingresos</span>
  </div>
  <div class="stat-row-divider"></div>
  <div class="stat-row-item">
    <span class="stat-row-value">89%</span>
    <span class="stat-row-label">Conversion</span>
  </div>
</div>
```

```css
.stat-row {
  display: flex;
  align-items: center;
  gap: var(--space-l);
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.stat-row-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3xs);
  flex: 1;
}
.stat-row-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-2);
  font-weight: 600;
}
.stat-row-label {
  font-size: var(--step--2);
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.stat-row-divider {
  width: 1px;
  height: 3rem;
  background: var(--border);
  flex-shrink: 0;
}

@media (max-width: 600px) {
  .stat-row { flex-direction: column; gap: var(--space-s); }
  .stat-row-divider { width: 3rem; height: 1px; }
}
```

### 1C. Spotlight stat (1 numero grande + descripcion)

Un unico dato protagonista. Para hero sections o abrir una seccion con impacto.

```html
<div class="spotlight-stat">
  <span class="spotlight-value">73%</span>
  <span class="spotlight-desc">de los estudiantes aprobaron en la primera convocatoria</span>
</div>
```

```css
.spotlight-stat {
  text-align: center;
  max-width: 40ch;
}
.spotlight-value {
  display: block;
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-5);
  font-weight: 600;
  line-height: 1;
  color: var(--accent, var(--text));
}
.spotlight-desc {
  display: block;
  margin-top: var(--space-xs);
  font-size: var(--step-0);
  color: var(--text-secondary);
  line-height: 1.4;
}
```

### 1D. Stat card con sparkline

Metrica con mini grafica de tendencia. Para mostrar evolucion junto al dato.

```html
<div class="stat-spark">
  <div class="stat-spark-info">
    <span class="stat-label">Trafico mensual</span>
    <span class="stat-value">45,231</span>
    <span class="stat-change positive">+23%</span>
  </div>
  <svg class="sparkline" viewBox="0 0 80 24" preserveAspectRatio="none">
    <polyline points="0,20 12,16 24,18 36,8 48,12 60,6 72,10 80,3"
              fill="none" stroke="var(--accent, var(--text-secondary))"
              stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
```

```css
.stat-spark {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-m);
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.stat-spark-info {
  display: flex;
  flex-direction: column;
  gap: var(--space-3xs);
}
.sparkline {
  width: 6rem;
  height: 2rem;
  flex-shrink: 0;
}
```

### 1E. Stat card con mini bar

Metrica con barra de progreso incorporada. Para datos con un total conocido (porcentajes, cuotas).

```html
<div class="stat-bar-card">
  <div class="stat-bar-header">
    <span class="stat-label">Completado</span>
    <span class="stat-value" style="font-size: var(--step-2)">68%</span>
  </div>
  <div class="mini-bar-track">
    <div class="mini-bar-fill" style="--pct: 68%"></div>
  </div>
</div>
```

```css
.stat-bar-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.stat-bar-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.mini-bar-track {
  height: 6px;
  background: var(--bg-elevated);
  border-radius: 3px;
  overflow: hidden;
}
.mini-bar-fill {
  height: 100%;
  width: var(--pct);
  background: var(--accent, var(--text-secondary));
  border-radius: 3px;
  transition: width 0.6s var(--ease-out);
}
```

---

## 2. VISUALIZACIONES (CSS-only, sin Chart.js)

### 2A. Barras horizontales (progress-style)

Para rankings, comparaciones de cantidades o progreso. La mas versatil.

```html
<div class="h-bars">
  <div class="h-bar-item">
    <span class="h-bar-label">Producto A</span>
    <div class="h-bar-track">
      <div class="h-bar-fill" style="--pct: 85%"></div>
    </div>
    <span class="h-bar-value">85%</span>
  </div>
  <div class="h-bar-item">
    <span class="h-bar-label">Producto B</span>
    <div class="h-bar-track">
      <div class="h-bar-fill" style="--pct: 62%"></div>
    </div>
    <span class="h-bar-value">62%</span>
  </div>
  <div class="h-bar-item">
    <span class="h-bar-label">Producto C</span>
    <div class="h-bar-track">
      <div class="h-bar-fill" style="--pct: 41%"></div>
    </div>
    <span class="h-bar-value">41%</span>
  </div>
</div>
```

```css
.h-bars {
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
  width: 100%;
}
.h-bar-item {
  display: grid;
  grid-template-columns: 8rem 1fr 3rem;
  align-items: center;
  gap: var(--space-xs);
}
.h-bar-label {
  font-size: var(--step--1);
  color: var(--text-secondary);
  text-align: right;
}
.h-bar-track {
  height: 8px;
  background: var(--bg-elevated);
  border-radius: 4px;
  overflow: hidden;
}
.h-bar-fill {
  height: 100%;
  width: var(--pct);
  background: var(--accent, var(--text-secondary));
  border-radius: 4px;
  transition: width 0.6s var(--ease-out);
}
.h-bar-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step--1);
  text-align: right;
}

@media (max-width: 600px) {
  .h-bar-item { grid-template-columns: 5rem 1fr 2.5rem; }
}
```

### 2B. Barras verticales

Para comparar categorias discretas (meses, productos, anos).

```html
<div class="v-bars" style="--bar-count: 5">
  <div class="v-bar-item">
    <span class="v-bar-value">80%</span>
    <div class="v-bar" style="--pct: 80%"></div>
    <span class="v-bar-label">2021</span>
  </div>
  <div class="v-bar-item">
    <span class="v-bar-value">65%</span>
    <div class="v-bar" style="--pct: 65%"></div>
    <span class="v-bar-label">2022</span>
  </div>
  <div class="v-bar-item">
    <span class="v-bar-value">92%</span>
    <div class="v-bar accent" style="--pct: 92%"></div>
    <span class="v-bar-label">2023</span>
  </div>
</div>
```

```css
.v-bars {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: var(--space-m);
  height: 16rem;
  padding-top: var(--space-m);
}
.v-bar-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2xs);
  flex: 1;
  max-width: 4rem;
  height: 100%;
  justify-content: flex-end;
}
.v-bar-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step--2);
  color: var(--text-secondary);
}
.v-bar {
  width: 100%;
  height: var(--pct);
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 6px 6px 0 0;
  transition: height 0.6s var(--ease-out);
}
.v-bar.accent {
  background: color-mix(in srgb, var(--accent) 20%, var(--bg-surface));
  border-color: var(--accent);
}
.v-bar-label {
  font-size: var(--step--2);
  color: var(--text-muted);
}
```

### 2C. Donut / Ring chart (SVG stroke-dashoffset)

Para mostrar un porcentaje de un total. El circulo completo = circumference (2 * pi * r).

```html
<div class="donut">
  <svg viewBox="0 0 100 100" class="donut-svg">
    <circle cx="50" cy="50" r="40" class="donut-track"/>
    <circle cx="50" cy="50" r="40" class="donut-fill" style="--pct: 75"/>
  </svg>
  <div class="donut-center">
    <span class="donut-value">75%</span>
    <span class="donut-label">Completado</span>
  </div>
</div>
```

```css
/* r=40 → circumference = 2 * 3.14159 * 40 = 251.33 */
.donut {
  position: relative;
  width: 10rem;
  height: 10rem;
}
.donut-svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}
.donut-track {
  fill: none;
  stroke: var(--bg-elevated);
  stroke-width: 8;
}
.donut-fill {
  fill: none;
  stroke: var(--accent, var(--text-secondary));
  stroke-width: 8;
  stroke-linecap: round;
  stroke-dasharray: 251.33;
  stroke-dashoffset: calc(251.33 - (251.33 * var(--pct) / 100));
  transition: stroke-dashoffset 0.8s var(--ease-out);
}
.donut-center {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.donut-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-2);
  font-weight: 600;
}
.donut-label {
  font-size: var(--step--2);
  color: var(--text-muted);
}
```

### 2D. Gauge / semicirculo

Para mediciones con un rango (velocidad, rendimiento, puntuacion). El arco = mitad del circulo.

```html
<div class="gauge">
  <svg viewBox="0 0 100 60" class="gauge-svg">
    <!-- r=40, semi-circle arc length = pi * 40 = 125.66 -->
    <path d="M10,50 A40,40 0 0,1 90,50" class="gauge-track"/>
    <path d="M10,50 A40,40 0 0,1 90,50" class="gauge-fill" style="--pct: 70"/>
  </svg>
  <div class="gauge-value">7.0</div>
  <div class="gauge-label">Nota media</div>
</div>
```

```css
.gauge {
  position: relative;
  width: 12rem;
  text-align: center;
}
.gauge-svg { width: 100%; }
.gauge-track {
  fill: none;
  stroke: var(--bg-elevated);
  stroke-width: 8;
  stroke-linecap: round;
}
.gauge-fill {
  fill: none;
  stroke: var(--accent, var(--text-secondary));
  stroke-width: 8;
  stroke-linecap: round;
  /* pi * 40 = 125.66 */
  stroke-dasharray: 125.66;
  stroke-dashoffset: calc(125.66 - (125.66 * var(--pct) / 100));
  transition: stroke-dashoffset 0.8s var(--ease-out);
}
.gauge-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-3);
  font-weight: 600;
  margin-top: calc(-1 * var(--space-s));
}
.gauge-label {
  font-size: var(--step--2);
  color: var(--text-muted);
}
```

### 2E. Progress bar con etiqueta

Barra lineal con titulo y porcentaje. Para mostrar progreso de tareas, objetivos.

```html
<div class="progress">
  <div class="progress-header">
    <span class="progress-title">Unidad 3 — Sintaxis</span>
    <span class="progress-pct">75%</span>
  </div>
  <div class="progress-track">
    <div class="progress-fill" style="--pct: 75%"></div>
  </div>
</div>
```

```css
.progress {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.progress-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.progress-title {
  font-size: var(--step--1);
  color: var(--text);
}
.progress-pct {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step--1);
  color: var(--text-secondary);
}
.progress-track {
  height: 6px;
  background: var(--bg-elevated);
  border-radius: 3px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  width: var(--pct);
  background: var(--accent, var(--text-secondary));
  border-radius: 3px;
  transition: width 0.6s var(--ease-out);
}
```

### 2F. Sparkline (SVG polyline)

Mini grafica de tendencia. Para insertar en cards, filas de tabla o junto a metricas.

```html
<svg class="sparkline" viewBox="0 0 80 24" preserveAspectRatio="none">
  <polyline points="0,20 12,16 24,18 36,8 48,12 60,6 72,10 80,3"
            fill="none" stroke="var(--accent, var(--text-secondary))"
            stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

```css
.sparkline {
  width: 6rem;
  height: 1.5rem;
  display: block;
}
```

### 2G. Mini inline bar (para celdas de tabla)

Barra minima para usar dentro de tablas. Sin etiqueta, solo la barra.

```html
<td>
  <div class="inline-bar">
    <div class="inline-bar-fill" style="--pct: 72%"></div>
  </div>
</td>
```

```css
.inline-bar {
  width: 4rem;
  height: 4px;
  background: var(--bg-elevated);
  border-radius: 2px;
  overflow: hidden;
  display: inline-block;
  vertical-align: middle;
}
.inline-bar-fill {
  height: 100%;
  width: var(--pct);
  background: var(--accent, var(--text-secondary));
  border-radius: 2px;
}
```

---

## 3. TABLAS

### 3A. Tabla basica estilizada

Tabla con bordes sutiles y hover en filas. Para cualquier dato tabular.

```html
<table class="table">
  <thead>
    <tr>
      <th>Alumno</th>
      <th>Nota</th>
      <th>Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Garcia, Ana</td>
      <td class="data-value">8.5</td>
      <td><span class="badge badge-success">Aprobado</span></td>
    </tr>
    <tr>
      <td>Lopez, Carlos</td>
      <td class="data-value">4.2</td>
      <td><span class="badge badge-danger">Suspenso</span></td>
    </tr>
  </tbody>
</table>
```

```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--step--1);
}
.table th {
  text-align: left;
  padding: var(--space-xs) var(--space-s);
  font-size: var(--step--2);
  font-weight: 500;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid var(--border);
}
.table td {
  padding: var(--space-xs) var(--space-s);
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
}
.table tbody tr {
  transition: background-color var(--transition);
}
.table tbody tr:hover {
  background: var(--bg-surface);
}
.table .data-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}
```

### 3B. Tabla con micro-bars en celdas

Tabla que incluye mini barras junto a valores numericos. Para rankings con representacion visual.

```html
<table class="table">
  <thead>
    <tr><th>Equipo</th><th>Puntos</th><th>Rendimiento</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Equipo A</td>
      <td class="data-value">92</td>
      <td>
        <div class="cell-bar-row">
          <div class="inline-bar"><div class="inline-bar-fill" style="--pct: 92%"></div></div>
          <span class="data-value">92%</span>
        </div>
      </td>
    </tr>
    <tr>
      <td>Equipo B</td>
      <td class="data-value">67</td>
      <td>
        <div class="cell-bar-row">
          <div class="inline-bar"><div class="inline-bar-fill" style="--pct: 67%"></div></div>
          <span class="data-value">67%</span>
        </div>
      </td>
    </tr>
  </tbody>
</table>
```

```css
.cell-bar-row {
  display: flex;
  align-items: center;
  gap: var(--space-xs);
}
.cell-bar-row .inline-bar { width: 5rem; }
.cell-bar-row .data-value {
  font-size: var(--step--2);
  color: var(--text-secondary);
}
```

### 3C. Tabla con badges de estado

Tabla con badges coloreados con `color-mix()`. Para tablas con columnas de estado/categoria.

```html
<span class="badge badge-success">Aprobado</span>
<span class="badge badge-warning">En riesgo</span>
<span class="badge badge-danger">Suspenso</span>
<span class="badge badge-info">Pendiente</span>
```

```css
.badge {
  display: inline-block;
  padding: var(--space-3xs) var(--space-xs);
  font-size: var(--step--2);
  font-weight: 500;
  border-radius: 100px;
  white-space: nowrap;
}
.badge-success {
  color: #22c55e;
  background: color-mix(in srgb, #22c55e 12%, var(--bg-surface));
  border: 1px solid color-mix(in srgb, #22c55e 25%, transparent);
}
.badge-warning {
  color: #eab308;
  background: color-mix(in srgb, #eab308 12%, var(--bg-surface));
  border: 1px solid color-mix(in srgb, #eab308 25%, transparent);
}
.badge-danger {
  color: #ef4444;
  background: color-mix(in srgb, #ef4444 12%, var(--bg-surface));
  border: 1px solid color-mix(in srgb, #ef4444 25%, transparent);
}
.badge-info {
  color: var(--accent, var(--text-secondary));
  background: color-mix(in srgb, var(--accent, var(--text-secondary)) 12%, var(--bg-surface));
  border: 1px solid color-mix(in srgb, var(--accent, var(--text-secondary)) 25%, transparent);
}
```

### 3D. Tabla de comparacion (feature matrix)

Tabla con checks y cruces para comparar features. Usar iconos Lucide inline.

```html
<table class="table table-compare">
  <thead>
    <tr><th>Caracteristica</th><th>Plan Basic</th><th>Plan Pro</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Exportar PDF</td>
      <td class="check-cell">
        <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="18" height="18"><path d="M20 6 9 17l-5-5"/></svg>
      </td>
      <td class="check-cell">
        <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="18" height="18"><path d="M20 6 9 17l-5-5"/></svg>
      </td>
    </tr>
    <tr>
      <td>API access</td>
      <td class="check-cell">
        <svg viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.5" width="18" height="18"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
      </td>
      <td class="check-cell">
        <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="18" height="18"><path d="M20 6 9 17l-5-5"/></svg>
      </td>
    </tr>
  </tbody>
</table>
```

```css
.table-compare th:not(:first-child),
.table-compare td:not(:first-child) {
  text-align: center;
}
.check-cell {
  text-align: center;
}
.check-cell svg {
  vertical-align: middle;
}
```

---

## 4. TIMELINES Y PROCESOS

### 4A. Timeline vertical

Eventos en orden cronologico con linea conectora y puntos. Para historiales, roadmaps, biografias.

```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-dot active"></div>
    <div class="timeline-content">
      <span class="timeline-date">Septiembre 2025</span>
      <h4 class="timeline-title">Inicio del curso</h4>
      <p class="timeline-desc">Evaluacion diagnostica y planificacion del trimestre.</p>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
      <span class="timeline-date">Diciembre 2025</span>
      <h4 class="timeline-title">Primera evaluacion</h4>
      <p class="timeline-desc">Examen parcial y entrega de trabajos.</p>
    </div>
  </div>
  <div class="timeline-item">
    <div class="timeline-dot"></div>
    <div class="timeline-content">
      <span class="timeline-date">Marzo 2026</span>
      <h4 class="timeline-title">Segunda evaluacion</h4>
      <p class="timeline-desc">Proyecto de investigacion y examen.</p>
    </div>
  </div>
</div>
```

```css
.timeline {
  position: relative;
  padding-left: var(--space-l);
}
.timeline::before {
  content: '';
  position: absolute;
  left: 5px;
  top: 8px;
  bottom: 8px;
  width: 1px;
  background: var(--border);
}
.timeline-item {
  position: relative;
  padding-bottom: var(--space-l);
}
.timeline-item:last-child { padding-bottom: 0; }
.timeline-dot {
  position: absolute;
  left: calc(-1 * var(--space-l) + 1px);
  top: 6px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
}
.timeline-dot.active {
  background: var(--accent, var(--text-secondary));
  border-color: var(--accent, var(--text-secondary));
}
.timeline-date {
  font-size: var(--step--2);
  font-weight: 500;
  color: var(--accent, var(--text-secondary));
  letter-spacing: 0.02em;
}
.timeline-title {
  font-size: var(--step-0);
  font-weight: 500;
  margin-top: var(--space-3xs);
  margin-bottom: var(--space-3xs);
}
.timeline-desc {
  font-size: var(--step--1);
  color: var(--text-secondary);
  line-height: 1.5;
}
```

### 4B. Proceso horizontal (steps)

Pasos de un flujo con lineas conectoras. Para workflows, instrucciones, fases de un proyecto.

```html
<div class="steps">
  <div class="step completed">
    <div class="step-circle">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="16" height="16"><path d="M20 6 9 17l-5-5"/></svg>
    </div>
    <span class="step-label">Investigar</span>
  </div>
  <div class="step-line completed"></div>
  <div class="step active">
    <div class="step-circle">2</div>
    <span class="step-label">Redactar</span>
  </div>
  <div class="step-line"></div>
  <div class="step">
    <div class="step-circle">3</div>
    <span class="step-label">Revisar</span>
  </div>
  <div class="step-line"></div>
  <div class="step">
    <div class="step-circle">4</div>
    <span class="step-label">Entregar</span>
  </div>
</div>
```

```css
.steps {
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-xs);
}
.step-circle {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: var(--step--1);
  font-weight: 500;
  color: var(--text-muted);
  transition: all var(--transition);
}
.step.active .step-circle {
  background: color-mix(in srgb, var(--accent) 15%, var(--bg-surface));
  border-color: var(--accent);
  color: var(--accent);
}
.step.completed .step-circle {
  background: color-mix(in srgb, #22c55e 15%, var(--bg-surface));
  border-color: #22c55e;
  color: #22c55e;
}
.step-label {
  font-size: var(--step--2);
  color: var(--text-muted);
}
.step.active .step-label { color: var(--text); }
.step.completed .step-label { color: var(--text-secondary); }
.step-line {
  width: 3rem;
  height: 1px;
  background: var(--border);
  margin-top: 1.25rem; /* centrado con el circulo */
  flex-shrink: 0;
}
.step-line.completed { background: #22c55e; }

@media (max-width: 600px) {
  .steps { flex-direction: column; align-items: flex-start; }
  .step { flex-direction: row; }
  .step-line { width: 1px; height: 1.5rem; margin-top: 0; margin-left: 1.25rem; }
}
```

### 4C. Roadmap con fases

Fases de un proyecto con estados diferenciados. Para planificaciones trimestrales, product roadmaps.

```html
<div class="roadmap">
  <div class="roadmap-phase done">
    <div class="roadmap-header">
      <span class="roadmap-quarter">T1 2025</span>
      <span class="badge badge-success">Completado</span>
    </div>
    <ul class="roadmap-items">
      <li>Evaluacion diagnostica</li>
      <li>Unidad 1: Comunicacion</li>
    </ul>
  </div>
  <div class="roadmap-phase current">
    <div class="roadmap-header">
      <span class="roadmap-quarter">T2 2025</span>
      <span class="badge badge-info">En curso</span>
    </div>
    <ul class="roadmap-items">
      <li>Unidad 2: Narracion</li>
      <li>Proyecto de lectura</li>
    </ul>
  </div>
  <div class="roadmap-phase pending">
    <div class="roadmap-header">
      <span class="roadmap-quarter">T3 2025</span>
      <span class="badge" style="color: var(--text-muted); border: 1px solid var(--border);">Pendiente</span>
    </div>
    <ul class="roadmap-items">
      <li>Unidad 3: Argumentacion</li>
      <li>Examen final</li>
    </ul>
  </div>
</div>
```

```css
.roadmap {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: var(--space-s);
}
.roadmap-phase {
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.roadmap-phase.current {
  border-color: var(--accent, var(--text-secondary));
}
.roadmap-phase.pending {
  opacity: 0.6;
}
.roadmap-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-s);
}
.roadmap-quarter {
  font-family: var(--font-mono);
  font-size: var(--step--1);
  font-weight: 500;
}
.roadmap-items {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.roadmap-items li {
  font-size: var(--step--1);
  color: var(--text-secondary);
  padding-left: var(--space-s);
  position: relative;
}
.roadmap-items li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.6em;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--text-muted);
}
```

---

## 5. COMPARACIONES

### 5A. Before / After (bloques lado a lado)

Dos bloques que contrastan un estado anterior y uno posterior. Para cambios, mejoras, transformaciones.

```html
<div class="before-after">
  <div class="ba-block before">
    <span class="ba-label">Antes</span>
    <div class="ba-content">
      <p>Texto desorganizado sin estructura, parrafos largos y confusos, sin jerarquia visual.</p>
    </div>
  </div>
  <div class="ba-block after">
    <span class="ba-label">Despues</span>
    <div class="ba-content">
      <p>Contenido estructurado con headings claros, parrafos cortos y elementos visuales de apoyo.</p>
    </div>
  </div>
</div>
```

```css
.before-after {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-s);
}
.ba-block {
  padding: var(--space-m);
  border-radius: var(--radius);
  border: 1px solid var(--border);
}
.ba-block.before {
  background: color-mix(in srgb, #ef4444 5%, var(--bg-surface));
  border-color: color-mix(in srgb, #ef4444 20%, var(--border));
}
.ba-block.after {
  background: color-mix(in srgb, #22c55e 5%, var(--bg-surface));
  border-color: color-mix(in srgb, #22c55e 20%, var(--border));
}
.ba-label {
  display: inline-block;
  font-size: var(--step--2);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: var(--space-xs);
}
.ba-block.before .ba-label { color: #ef4444; }
.ba-block.after .ba-label { color: #22c55e; }
.ba-content {
  font-size: var(--step--1);
  color: var(--text-secondary);
  line-height: 1.5;
}

@media (max-width: 600px) {
  .before-after { grid-template-columns: 1fr; }
}
```

### 5B. Versus (A vs B con numeros grandes)

Comparacion directa entre dos valores enfrentados. Para confrontar datos.

```html
<div class="versus">
  <div class="versus-side">
    <span class="versus-value negative">15%</span>
    <span class="versus-label">Competencia</span>
  </div>
  <div class="versus-divider">
    <span>vs</span>
  </div>
  <div class="versus-side">
    <span class="versus-value positive">85%</span>
    <span class="versus-label">Nosotros</span>
  </div>
</div>
```

```css
.versus {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-l);
}
.versus-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3xs);
}
.versus-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-4);
  font-weight: 600;
  line-height: 1;
}
.versus-value.positive { color: #22c55e; }
.versus-value.negative { color: #ef4444; }
.versus-label {
  font-size: var(--step--1);
  color: var(--text-muted);
}
.versus-divider {
  font-size: var(--step--1);
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
```

### 5C. Comparacion de features (pros/cons cards)

Dos cards con listas de ventajas e inconvenientes. Para evaluar opciones.

```html
<div class="pros-cons">
  <div class="pc-card pros">
    <h4 class="pc-title">
      <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="18" height="18"><path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/></svg>
      Ventajas
    </h4>
    <ul class="pc-list">
      <li>Facil de implementar</li>
      <li>Buena documentacion</li>
      <li>Comunidad activa</li>
    </ul>
  </div>
  <div class="pc-card cons">
    <h4 class="pc-title">
      <svg viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.5" width="18" height="18"><path d="M17 14V2"/><path d="M9 18.12 10 14H4.17a2 2 0 0 1-1.92-2.56l2.33-8A2 2 0 0 1 6.5 2H20a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-2.76a2 2 0 0 0-1.79 1.11L12 22a3.13 3.13 0 0 1-3-3.88Z"/></svg>
      Inconvenientes
    </h4>
    <ul class="pc-list">
      <li>Rendimiento limitado</li>
      <li>Curva de aprendizaje</li>
    </ul>
  </div>
</div>
```

```css
.pros-cons {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-s);
}
.pc-card {
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.pc-card.pros {
  border-color: color-mix(in srgb, #22c55e 25%, var(--border));
}
.pc-card.cons {
  border-color: color-mix(in srgb, #ef4444 25%, var(--border));
}
.pc-title {
  display: flex;
  align-items: center;
  gap: var(--space-2xs);
  font-size: var(--step-0);
  font-weight: 500;
  margin-bottom: var(--space-s);
}
.pc-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.pc-list li {
  font-size: var(--step--1);
  color: var(--text-secondary);
  padding-left: var(--space-s);
  position: relative;
}
.pc-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.65em;
  width: 4px;
  height: 4px;
  border-radius: 50%;
}
.pros .pc-list li::before { background: #22c55e; }
.cons .pc-list li::before { background: #ef4444; }

@media (max-width: 600px) {
  .pros-cons { grid-template-columns: 1fr; }
}
```

---

## 6. CALLOUTS Y CITAS

### 6A. Blockquote con borde de acento

Cita con borde lateral coloreado. Para citas textuales o fragmentos destacados.

```html
<blockquote class="blockquote">
  <p>La tipografia existe para honrar el contenido.</p>
  <cite>Robert Bringhurst</cite>
</blockquote>
```

```css
.blockquote {
  padding: var(--space-s) var(--space-m);
  border-left: 3px solid var(--accent, var(--text-secondary));
  background: var(--bg-surface);
  border-radius: 0 var(--radius) var(--radius) 0;
}
.blockquote p {
  font-size: var(--step-0);
  font-style: italic;
  color: var(--text);
  line-height: 1.5;
}
.blockquote cite {
  display: block;
  margin-top: var(--space-xs);
  font-size: var(--step--1);
  font-style: normal;
  color: var(--text-muted);
}
.blockquote cite::before {
  content: '\2014\00a0';
}
```

### 6B. Callouts: info / warning / success / danger

Bloques de aviso con fondo tintado via `color-mix()`. Para mensajes contextuales.

```html
<div class="callout callout-info">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
  <div class="callout-body">
    <strong>Nota:</strong> Este ejercicio es optativo y no cuenta para la nota final.
  </div>
</div>

<div class="callout callout-warning">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>
  <div class="callout-body">
    <strong>Atencion:</strong> Fecha limite de entrega el viernes.
  </div>
</div>

<div class="callout callout-success">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/></svg>
  <div class="callout-body">
    <strong>Correcto:</strong> Tu respuesta es valida.
  </div>
</div>

<div class="callout callout-danger">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg>
  <div class="callout-body">
    <strong>Error:</strong> Revisa la concordancia sujeto-verbo.
  </div>
</div>
```

```css
.callout {
  display: flex;
  align-items: flex-start;
  gap: var(--space-xs);
  padding: var(--space-s) var(--space-m);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  font-size: var(--step--1);
  line-height: 1.5;
}
.callout svg { flex-shrink: 0; margin-top: 2px; }
.callout-body strong {
  font-weight: 500;
}

.callout-info {
  background: color-mix(in srgb, #3b82f6 8%, var(--bg-surface));
  border-color: color-mix(in srgb, #3b82f6 20%, var(--border));
  color: var(--text);
}
.callout-info svg { stroke: #3b82f6; }

.callout-warning {
  background: color-mix(in srgb, #eab308 8%, var(--bg-surface));
  border-color: color-mix(in srgb, #eab308 20%, var(--border));
  color: var(--text);
}
.callout-warning svg { stroke: #eab308; }

.callout-success {
  background: color-mix(in srgb, #22c55e 8%, var(--bg-surface));
  border-color: color-mix(in srgb, #22c55e 20%, var(--border));
  color: var(--text);
}
.callout-success svg { stroke: #22c55e; }

.callout-danger {
  background: color-mix(in srgb, #ef4444 8%, var(--bg-surface));
  border-color: color-mix(in srgb, #ef4444 20%, var(--border));
  color: var(--text);
}
.callout-danger svg { stroke: #ef4444; }
```

### 6C. Pull quote (cita destacada grande)

Cita con tipografia grande centrada. Para abrir secciones con impacto.

```html
<div class="pull-quote">
  <p>Lo que no se mide, no se mejora.</p>
  <cite>Peter Drucker</cite>
</div>
```

```css
.pull-quote {
  text-align: center;
  max-width: 40ch;
  margin: 0 auto;
  padding: var(--space-l) 0;
}
.pull-quote p {
  font-family: var(--font-display);
  font-size: var(--step-3);
  font-weight: 500;
  line-height: 1.25;
  color: var(--text);
  text-wrap: balance;
}
.pull-quote cite {
  display: block;
  margin-top: var(--space-s);
  font-size: var(--step--1);
  font-style: normal;
  color: var(--text-muted);
}
.pull-quote cite::before {
  content: '\2014\00a0';
}
```

---

## 7. CARDS (expandido)

### 7A. Card basica

Contenedor generico con borde y hover. Para agrupar contenido relacionado.

```html
<div class="card">
  <h3 class="card-title">Titulo de la tarjeta</h3>
  <p class="card-desc">Descripcion breve del contenido que contiene esta tarjeta.</p>
</div>
```

```css
.card {
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  transition: border-color var(--transition), transform var(--transition);
}
.card:hover {
  border-color: var(--text-secondary);
  transform: translateY(-2px);
}
.card-title {
  font-size: var(--step-1);
  font-weight: 500;
  margin-bottom: var(--space-2xs);
}
.card-desc {
  font-size: var(--step--1);
  color: var(--text-secondary);
  line-height: 1.5;
}
```

### 7B. Spotlight card (tinted border)

Card destacada con borde coloreado. Para el elemento principal en un grid de cards.

```html
<div class="card card-spotlight">
  <span class="card-eyebrow">Destacado</span>
  <h3 class="card-title">Resultado del trimestre</h3>
  <p class="card-desc">El 78% del alumnado ha superado los objetivos minimos.</p>
</div>
```

```css
.card-spotlight {
  border-color: var(--accent, var(--text-secondary));
  background: color-mix(in srgb, var(--accent, var(--text-secondary)) 5%, var(--bg-surface));
}
.card-eyebrow {
  display: inline-block;
  font-size: var(--step--2);
  font-weight: 500;
  color: var(--accent, var(--text-secondary));
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: var(--space-xs);
}
```

### 7C. Card con icono header

Card con icono Lucide arriba. Para feature grids, servicios.

```html
<div class="card card-icon">
  <div class="card-icon-box">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="24" height="24">
      <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
    </svg>
  </div>
  <h3 class="card-title">Lectura comprensiva</h3>
  <p class="card-desc">Estrategias para mejorar la comprension lectora en secundaria.</p>
</div>
```

```css
.card-icon-box {
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: color-mix(in srgb, var(--accent, var(--text-secondary)) 10%, var(--bg-surface));
  border: 1px solid color-mix(in srgb, var(--accent, var(--text-secondary)) 25%, var(--border));
  border-radius: 8px;
  margin-bottom: var(--space-s);
  color: var(--accent, var(--text-secondary));
}
```

### 7D. Card grid con jerarquia (1 grande + 2 pequenas)

Evitar 4 cards identicas en fila. El spotlight destaca uno, el resto son secundarios.

```html
<div class="card-grid-hierarchy">
  <div class="card card-spotlight card-big">
    <span class="card-eyebrow">Principal</span>
    <h3 class="card-title">Resultado global</h3>
    <span class="stat-value">78%</span>
    <p class="card-desc">Porcentaje de aprobados en la primera evaluacion.</p>
  </div>
  <div class="card">
    <h3 class="card-title">Media de notas</h3>
    <span class="stat-value" style="font-size: var(--step-2)">6.4</span>
  </div>
  <div class="card">
    <h3 class="card-title">Asistencia</h3>
    <span class="stat-value" style="font-size: var(--step-2)">91%</span>
  </div>
</div>
```

```css
.card-grid-hierarchy {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  grid-template-rows: auto auto;
  gap: var(--space-s);
}
.card-grid-hierarchy .card-big {
  grid-row: 1 / -1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

@media (max-width: 600px) {
  .card-grid-hierarchy {
    grid-template-columns: 1fr;
  }
  .card-grid-hierarchy .card-big {
    grid-row: auto;
  }
}
```

### 7E. Metric card (icono + numero + label + trend)

Card compacta para KPI con todos los elementos. Para dashboard grids.

```html
<div class="metric-card">
  <div class="metric-card-header">
    <div class="card-icon-box">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="20" height="20"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    </div>
    <span class="stat-change positive">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="14" height="14"><path d="m18 15-6-6-6 6"/></svg>
      +5.2%
    </span>
  </div>
  <span class="stat-value" style="font-size: var(--step-2)">1,247</span>
  <span class="stat-label">Alumnos matriculados</span>
</div>
```

```css
.metric-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.metric-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: var(--space-2xs);
}
```

---

## 8. LISTAS Y NAVEGACION

### 8A. Check list (Lucide icons)

Lista con iconos de check/cross. Para requisitos, criterios de evaluacion, checklists.

```html
<ul class="check-list">
  <li class="check-yes">
    <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="16" height="16"><path d="M20 6 9 17l-5-5"/></svg>
    Presenta estructura clara
  </li>
  <li class="check-yes">
    <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="16" height="16"><path d="M20 6 9 17l-5-5"/></svg>
    Usa conectores textuales
  </li>
  <li class="check-no">
    <svg viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.5" width="16" height="16"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
    Contiene errores ortograficos
  </li>
</ul>
```

```css
.check-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.check-list li {
  display: flex;
  align-items: center;
  gap: var(--space-xs);
  font-size: var(--step--1);
}
.check-list li svg { flex-shrink: 0; }
.check-list .check-no {
  color: var(--text-muted);
}
```

### 8B. Numbered steps (numero grande + texto)

Lista de pasos con numeros destacados. Para instrucciones, tutoriales.

```html
<ol class="big-steps">
  <li>
    <span class="big-step-num">01</span>
    <div class="big-step-content">
      <strong>Lee el texto completo</strong>
      <p>Haz una primera lectura rapida para captar la idea general.</p>
    </div>
  </li>
  <li>
    <span class="big-step-num">02</span>
    <div class="big-step-content">
      <strong>Subraya las ideas principales</strong>
      <p>Marca con un color las frases que resumen cada parrafo.</p>
    </div>
  </li>
  <li>
    <span class="big-step-num">03</span>
    <div class="big-step-content">
      <strong>Redacta el resumen</strong>
      <p>Conecta las ideas con tus propias palabras.</p>
    </div>
  </li>
</ol>
```

```css
.big-steps {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-m);
}
.big-steps li {
  display: flex;
  align-items: flex-start;
  gap: var(--space-m);
}
.big-step-num {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-3);
  font-weight: 600;
  line-height: 1;
  color: var(--text-muted);
  flex-shrink: 0;
  min-width: 2.5rem;
}
.big-step-content strong {
  display: block;
  font-size: var(--step-0);
  font-weight: 500;
  margin-bottom: var(--space-3xs);
}
.big-step-content p {
  font-size: var(--step--1);
  color: var(--text-secondary);
  line-height: 1.5;
}
```

### 8C. Sidebar navigation con estado activo

Navegacion vertical con items seleccionables. Para dashboards con secciones.

```html
<nav class="sidebar-nav">
  <a href="#" class="nav-item active">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
    Inicio
  </a>
  <a href="#" class="nav-item">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    Alumnos
  </a>
  <a href="#" class="nav-item">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="18" height="18"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
    Estadisticas
  </a>
</nav>
```

```css
.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-3xs);
  width: 14rem;
}
.nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-xs);
  padding: var(--space-xs) var(--space-s);
  font-size: var(--step--1);
  color: var(--text-secondary);
  border-radius: 8px;
  transition: all var(--transition);
  text-decoration: none;
}
.nav-item:hover {
  background: var(--bg-surface);
  color: var(--text);
}
.nav-item.active {
  background: color-mix(in srgb, var(--accent, var(--text-secondary)) 10%, var(--bg-surface));
  color: var(--accent, var(--text));
  border: 1px solid color-mix(in srgb, var(--accent, var(--text-secondary)) 20%, var(--border));
}
.nav-item svg { flex-shrink: 0; }
```

### 8D. Breadcrumb

Ruta de navegacion. Para indicar posicion en la jerarquia.

```html
<nav class="breadcrumb">
  <a href="#">Inicio</a>
  <span class="breadcrumb-sep">/</span>
  <a href="#">Alumnos</a>
  <span class="breadcrumb-sep">/</span>
  <span class="breadcrumb-current">Garcia, Ana</span>
</nav>
```

```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: var(--space-2xs);
  font-size: var(--step--1);
}
.breadcrumb a {
  color: var(--text-muted);
  text-decoration: none;
  transition: color var(--transition);
}
.breadcrumb a:hover { color: var(--text); }
.breadcrumb-sep { color: var(--text-muted); }
.breadcrumb-current { color: var(--text); }
```

### 8E. Tag cloud

Grupo de tags con tamanos variados. Para categorias, temas, keywords.

```html
<div class="tag-cloud">
  <span class="tag tag-lg">Sintaxis</span>
  <span class="tag">Morfologia</span>
  <span class="tag">Semantica</span>
  <span class="tag tag-lg">Ortografia</span>
  <span class="tag tag-sm">Fonetica</span>
  <span class="tag">Pragmatica</span>
  <span class="tag tag-sm">Lexicografia</span>
</div>
```

```css
.tag {
  display: inline-block;
  padding: var(--space-3xs) var(--space-xs);
  font-size: var(--step--2);
  font-weight: 500;
  color: var(--text-muted);
  border: 1px solid var(--border);
  border-radius: 100px;
  transition: border-color var(--transition);
}
.tag:hover { border-color: var(--text-secondary); }
.tag-lg {
  font-size: var(--step--1);
  padding: var(--space-2xs) var(--space-s);
}
.tag-sm {
  font-size: clamp(0.56rem, 0.52rem + 0.2vw, 0.7rem);
  padding: 2px var(--space-2xs);
}
.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2xs);
  align-items: center;
}
```

---

## 9. HEROES Y HEADERS

### 9A. Hero con eyebrow + titulo + subtitulo + CTA

Seccion de apertura con jerarquia completa. Para landing pages, presentaciones.

```html
<section class="hero">
  <span class="hero-eyebrow">Curso 2025-26</span>
  <h1 class="hero-title">Lengua Castellana<br>y <span class="accent">Literatura</span></h1>
  <p class="hero-subtitle">Material complementario para 4.o de ESO. Ejercicios interactivos, apuntes y recursos de refuerzo.</p>
  <div class="hero-actions">
    <a href="#contenido" class="btn btn-primary">Ver contenido</a>
    <a href="#info" class="btn btn-ghost">Mas informacion</a>
  </div>
</section>
```

```css
.hero {
  padding: var(--space-2xl) 0 var(--space-xl);
  max-width: 40ch;
}
.hero-eyebrow {
  display: inline-block;
  font-size: var(--step--2);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent, var(--text-muted));
  margin-bottom: var(--space-s);
}
.hero-title {
  font-family: var(--font-display);
  font-size: var(--step-5);
  font-weight: 600;
  line-height: 1.05;
  letter-spacing: -0.03em;
  text-wrap: balance;
  margin-bottom: var(--space-m);
}
.accent { color: var(--accent, var(--text-secondary)); }
.hero-subtitle {
  font-size: var(--step-0);
  color: var(--text-secondary);
  line-height: 1.5;
  max-width: 50ch;
  margin-bottom: var(--space-l);
}
.hero-actions {
  display: flex;
  gap: var(--space-s);
  flex-wrap: wrap;
}

/* Botones */
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2xs);
  padding: var(--space-xs) var(--space-m);
  font-family: var(--font-body);
  font-size: var(--step--1);
  font-weight: 500;
  border-radius: 8px;
  text-decoration: none;
  transition: all var(--transition);
  cursor: pointer;
}
.btn-primary {
  background: var(--text);
  color: var(--bg);
  border: 1px solid var(--text);
}
.btn-primary:hover {
  opacity: 0.85;
  transform: translateY(-1px);
}
.btn-ghost {
  background: transparent;
  color: var(--text-secondary);
  border: 1px solid var(--border);
}
.btn-ghost:hover {
  border-color: var(--text-secondary);
  color: var(--text);
}
.btn:active { transform: scale(0.97); }
```

### 9B. Hero con stat highlight

Hero con un numero grande al lado del titulo. Para abrir con un dato de impacto.

```html
<section class="hero hero-with-stat">
  <div class="hero-text">
    <span class="hero-eyebrow">Informe trimestral</span>
    <h1 class="hero-title">Evaluacion<br><span class="accent">1.er trimestre</span></h1>
    <p class="hero-subtitle">Resultados academicos del grupo 4.o A.</p>
  </div>
  <div class="hero-stat">
    <span class="spotlight-value">78%</span>
    <span class="spotlight-desc">tasa de aprobados</span>
  </div>
</section>
```

```css
.hero-with-stat {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-xl);
  max-width: none;
}
.hero-text { max-width: 30ch; }
.hero-stat { text-align: center; flex-shrink: 0; }

@media (max-width: 600px) {
  .hero-with-stat { flex-direction: column; align-items: flex-start; }
}
```

### 9C. Section header con icono

Encabezado de seccion con icono y separador. Para dividir secciones dentro de una pagina larga.

```html
<div class="section-header">
  <div class="section-icon">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="20" height="20"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
  </div>
  <div>
    <h2 class="section-title">Estadisticas</h2>
    <p class="section-desc">Resumen del rendimiento academico del grupo.</p>
  </div>
</div>
```

```css
.section-header {
  display: flex;
  align-items: center;
  gap: var(--space-s);
  padding-bottom: var(--space-s);
  border-bottom: 1px solid var(--border);
  margin-bottom: var(--space-l);
}
.section-icon {
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: color-mix(in srgb, var(--accent, var(--text-secondary)) 10%, var(--bg-surface));
  border: 1px solid color-mix(in srgb, var(--accent, var(--text-secondary)) 25%, var(--border));
  border-radius: 8px;
  color: var(--accent, var(--text-secondary));
  flex-shrink: 0;
}
.section-title {
  font-size: var(--step-2);
  font-weight: 500;
  margin: 0;
}
.section-desc {
  font-size: var(--step--1);
  color: var(--text-muted);
  margin-top: var(--space-3xs);
}
```

---

## 10. FORMS E INTERACTIVO

### 10A. Form group (label + input)

Campo de formulario estandar. Para formularios, busquedas, configuracion.

```html
<div class="form-group">
  <label for="nombre" class="form-label">Nombre del alumno</label>
  <input type="text" id="nombre" class="form-input" placeholder="Escribe aqui...">
</div>
```

```css
.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.form-label {
  font-size: var(--step--1);
  font-weight: 500;
  color: var(--text-secondary);
}
.form-input {
  padding: var(--space-xs) var(--space-s);
  font-family: var(--font-body);
  font-size: var(--step-0);
  color: var(--text);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  outline: none;
  transition: border-color var(--transition);
}
.form-input::placeholder {
  color: var(--text-muted);
}
.form-input:focus-visible {
  border-color: var(--accent, var(--text-secondary));
  outline: 2px solid color-mix(in srgb, var(--accent, var(--text-secondary)) 25%, transparent);
  outline-offset: 2px;
}
```

### 10B. Radio / checkbox group para quizzes

Grupo de opciones para ejercicios interactivos. Con estados de feedback.

```html
<fieldset class="quiz-group">
  <legend class="form-label">Cual es el sujeto de la oracion?</legend>
  <label class="quiz-option">
    <input type="radio" name="q1" value="a">
    <span class="quiz-option-text">El perro</span>
  </label>
  <label class="quiz-option">
    <input type="radio" name="q1" value="b">
    <span class="quiz-option-text">En el parque</span>
  </label>
  <label class="quiz-option">
    <input type="radio" name="q1" value="c">
    <span class="quiz-option-text">Corria rapido</span>
  </label>
</fieldset>
```

```css
.quiz-group {
  border: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.quiz-group legend {
  margin-bottom: var(--space-s);
}
.quiz-option {
  display: flex;
  align-items: center;
  gap: var(--space-xs);
  padding: var(--space-xs) var(--space-s);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  transition: border-color var(--transition);
}
.quiz-option:hover {
  border-color: var(--text-secondary);
}
.quiz-option input[type="radio"],
.quiz-option input[type="checkbox"] {
  accent-color: var(--accent, var(--text-secondary));
  width: 1rem;
  height: 1rem;
  flex-shrink: 0;
}
.quiz-option-text {
  font-size: var(--step--1);
}
```

### 10C. Feedback states (correct / incorrect con color-mix)

Estados de respuesta para ejercicios. Aplicar despues de comprobar.

```html
<!-- Correcto -->
<label class="quiz-option correct">
  <input type="radio" name="q1" value="a" checked disabled>
  <span class="quiz-option-text">El perro</span>
  <svg viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="1.5" width="16" height="16" class="quiz-icon"><path d="M20 6 9 17l-5-5"/></svg>
</label>

<!-- Incorrecto -->
<label class="quiz-option incorrect">
  <input type="radio" name="q2" value="b" checked disabled>
  <span class="quiz-option-text">En el parque</span>
  <svg viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="1.5" width="16" height="16" class="quiz-icon"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
</label>
```

```css
.quiz-option.correct {
  background: color-mix(in srgb, #22c55e 8%, var(--bg-surface));
  border-color: color-mix(in srgb, #22c55e 30%, var(--border));
}
.quiz-option.incorrect {
  background: color-mix(in srgb, #ef4444 8%, var(--bg-surface));
  border-color: color-mix(in srgb, #ef4444 30%, var(--border));
}
.quiz-option:has(input:disabled) {
  cursor: default;
  opacity: 0.85;
}
.quiz-icon {
  margin-left: auto;
  flex-shrink: 0;
}
```

### 10D. Score display bar

Barra de puntuacion con colores del semaforo educativo. Para mostrar nota final de un ejercicio.

```html
<div class="score-display">
  <div class="score-header">
    <span class="score-title">Resultado</span>
    <span class="score-value good">8 / 10</span>
  </div>
  <div class="score-bar">
    <div class="score-fill good" style="--pct: 80%"></div>
  </div>
  <span class="score-feedback">Bien hecho. Revisa las preguntas 3 y 7.</span>
</div>
```

```css
.score-display {
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
  padding: var(--space-m);
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.score-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.score-title {
  font-size: var(--step--1);
  color: var(--text-secondary);
}
.score-value {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
  font-size: var(--step-1);
  font-weight: 600;
}
.score-value.good { color: #22c55e; }
.score-value.warning { color: #eab308; }
.score-value.bad { color: #ef4444; }
.score-bar {
  height: 8px;
  background: var(--bg-elevated);
  border-radius: 4px;
  overflow: hidden;
}
.score-fill {
  height: 100%;
  width: var(--pct);
  border-radius: 4px;
  transition: width 0.6s var(--ease-out);
}
.score-fill.good { background: #22c55e; }
.score-fill.warning { background: #eab308; }
.score-fill.bad { background: #ef4444; }
.score-feedback {
  font-size: var(--step--1);
  color: var(--text-muted);
}
```

---

## 11. UTILIDADES COMPARTIDAS

### Iconos Lucide (recordatorio)

Todas las instancias de iconos deben ser SVG inline de Lucide:

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
     stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
     width="18" height="18">
  <!-- paths de lucide.dev -->
</svg>
```

- **Always** `stroke-width="1.5"` (nunca 2 o mas)
- **Always** `fill="none"`, `stroke="currentColor"` para heredar color del tema
- **Never** emojis como iconos de UI
- Tamano estandar: 16-24px

### Header fijo con blur

```css
.header {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  padding: var(--space-s) var(--space-m);
  background: var(--bg);
  transition: all var(--transition);
}
.header.scrolled {
  background: color-mix(in srgb, var(--bg) 80%, transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
}
```

### Imagen de fondo decorativa (paginas interiores)

```css
.page::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url('/images/bg.jpg');
  background-size: cover;
  background-position: center;
  filter: grayscale(100%) blur(2px);
  opacity: 0.08;
  z-index: -1;
  pointer-events: none;
}
[data-theme="light"] .page::before {
  opacity: 0.05;
}
```

---

## PREMIUM DARK MODE PATTERNS

### Radial gradient depth
Background glow effect for hero sections in dark themes:
```css
.hero-glow {
  background-color: var(--bg);
  background-image: radial-gradient(
    ellipse 80% 50% at 50% -10%,
    color-mix(in srgb, var(--accent) 12%, transparent),
    transparent
  );
}
```

### Glassmorphism header
Sticky header with blur effect:
```css
.header-glass {
  position: sticky;
  top: 0;
  z-index: 100;
  background: color-mix(in srgb, var(--bg) 85%, transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
}
```

### Hero title glow
Subtle glow effect on large titles in dark mode:
```css
.title-glow {
  text-shadow: 0 0 80px color-mix(in srgb, var(--accent) 30%, transparent);
}
[data-theme="light"] .title-glow {
  text-shadow: none;
}
```

### Surface depth system
Three explicit levels for visual hierarchy:
```css
:root {
  /* --bg: base level */
  /* --bg-surface: cards, panels (+3% lightness) */
  /* --bg-elevated: modals, tooltips, hover (+6% lightness) */
}
```

### Gradient borders (Linear-style)
Cards with directional light illusion:
```css
.card-premium {
  background: var(--bg-surface);
  border-radius: var(--radius);
  box-shadow:
    inset 0 0 0 1px rgba(255, 255, 255, 0.06),
    inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
  border: none;
}
[data-theme="light"] .card-premium {
  box-shadow: none;
  border: 1px solid var(--border);
}
```

### Noise texture overlay
Micro-texture for depth (SVG turbulence):
```css
.noise::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity: 0.035;
  mix-blend-mode: overlay;
  pointer-events: none;
  border-radius: inherit;
}
.noise { position: relative; }
```

## ANTI-AI-SLOP RULES

These patterns are banned because they produce generic "AI-generated" looking output:

| Pattern | Why it's banned | Alternative |
|---------|----------------|-------------|
| `bg-indigo-500` / purple gradients | Every AI generates this (Tailwind default) | Use preset accent colors |
| 3 identical icon+text cards in a row | Most generic layout possible | Use spotlight (1 large + N small) or bento grid |
| Inter as only font (display = body) | Zero typographic contrast | Always pair with a display font |
| Pure gray `hsl(0, 0%, N%)` | Feels lifeless, no personality | Tinted grays: `hsl(210, 15%, N%)` or `hsl(30, 8%, N%)` |
| Centered hero + 3-column grid + CTA | "Startup template" cliché | Asymmetric layouts, bento, split sections |
| Single box-shadow for depth | Flat and generic | Multi-layer shadows or border-only approach |

## BENTO GRID

Variable-sized grid cells for modern dashboard/portfolio layouts:

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-s);
}
.bento-2x1 { grid-column: span 2; }
.bento-1x2 { grid-row: span 2; }
.bento-2x2 { grid-column: span 2; grid-row: span 2; }

@media (max-width: 900px) {
  .bento-grid { grid-template-columns: repeat(2, 1fr); }
  .bento-2x2 { grid-column: span 2; grid-row: span 1; }
}
@media (max-width: 600px) {
  .bento-grid { grid-template-columns: 1fr; }
  .bento-2x1, .bento-1x2, .bento-2x2 { grid-column: span 1; grid-row: span 1; }
}
```

```html
<div class="bento-grid">
  <div class="card bento-2x2"><!-- Hero card --></div>
  <div class="card bento-2x1"><!-- Wide card --></div>
  <div class="card"><!-- Standard --></div>
  <div class="card"><!-- Standard --></div>
  <div class="card bento-1x2"><!-- Tall card --></div>
  <div class="card bento-2x1"><!-- Wide card --></div>
</div>
```

---

## Checklist de componentes

- [ ] Cards usan `border: 1px solid var(--border)` (no box-shadow)
- [ ] Hover con `transform` o `border-color` change
- [ ] Badges/callouts usan `color-mix()` para fondo tintado
- [ ] Datos numericos con `font-family: var(--font-mono)` + `tabular-nums`
- [ ] Todas las medidas de texto con `var(--step-*)`
- [ ] Todos los espaciados con `var(--space-*)`
- [ ] Iconos son Lucide SVG con `stroke-width="1.5"`
- [ ] No hay emojis, gradientes ni box-shadow
- [ ] Formularios tienen `:focus-visible` accesible
- [ ] Ejercicios tienen feedback con `color-mix()` para `.correct`/`.incorrect`
- [ ] Grid de cards con jerarquia (no 4 identicas en fila)
- [ ] Responsive a 900px y 600px
