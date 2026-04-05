# Skills de materiales educativos — Paquete complementario para OpenClaw

> Este archivo NO define el rol ni la personalidad del agente. Es un paquete de
> capacidades adicionales para generar materiales educativos de alta calidad.
> Consultar estas instrucciones SOLO cuando Adri pida crear materiales educativos.

## Contexto educativo de Adri

- Docente de Lengua Castellana y Literatura en un IES de Galicia
- Sistema gallego, calificaciones 1-10 (aprobado >= 5)
- Idiomas: español y gallego normativo (para informes de tutoría)
- Cursos: 1 ESO a 2 Bachillerato
- Plataforma LMS: Moodle/Edixgal

## Dónde guardar los materiales generados

```
~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Materiales-Educativos/
├── lecciones/          # HTML interactivos
├── presentaciones/     # Slides HTML
├── cuestionarios/      # Archivos .gift
├── h5p/                # Paquetes .h5p y .zip SCORM
├── sesiones/           # Guiones de clase (.md)
├── informes/           # Informes de tutoría (.txt)
├── graficos/           # SVG + scripts Python
└── ilustraciones/      # PNG hand-drawn
```

## Restricciones de seguridad (solo para estos skills)

Al generar materiales:
- Guardar output SOLO en `~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Materiales-Educativos/` o `~/clawd/obsidian-vault/`
- No instalar dependencias del sistema sin permiso
- No acceder a servicios web con credenciales (Edixgal, ABALAR, XADE)
- No borrar archivos fuera de `~/clawd/`

---

# SKILLS DISPONIBLES

## 1. adri-style — Sistema de diseño visual

**Cuándo consultar:** SIEMPRE que generes cualquier HTML (lecciones, presentaciones, dashboards, ejercicios).

**Referencia principal:** `~/clawd/skills/adri-style/SKILL.md`

**Flujo rápido:**
1. Elegir preset de `skills/adri-style/references/style-presets.md` según contexto:
   - Dashboard/herramienta → Minimalista Adri, Swiss Modern
   - Presentación/landing → Bold Signal, Soffia Warm, Creative Voltage
   - Ejercicio interactivo → Pastel Geometry, Split Pastel, Electric Studio
   - Editorial/literario → Vintage Editorial, Paper & Ink, Dark Botanical
   - Futurista → Neon Cyber, Terminal Green
2. Copiar `skills/adri-style/assets/base.css` como punto de partida
3. Sobreescribir variables CSS con las del preset elegido
4. Consultar `references/` para tipografía, layout, componentes, animación

**Reglas innegociables:**
- Escala tipográfica fluida con `clamp()` y variables `--step-*`
- Font pairing real: `--font-display` DIFERENTE de `--font-body`
- Tema dual (oscuro por defecto) con toggle + localStorage
- Iconos Lucide SVG, NUNCA emojis en UI
- Near-black `#0a0a0a`, NUNCA `#000000`. Grises tintados, NUNCA puros
- Al menos 1 SVG inline por output. 2 breakpoints responsive mínimo
- NUNCA: box-shadow, animar padding/margin, Inter como única fuente, purple gradients

---

## 2. contenido-a-leccion — Lecciones HTML interactivas

**Cuándo:** Adri pide lección, material interactivo, o actividad sobre un texto literario.

**Output:** HTML autocontenido → `Materiales-Educativos/lecciones/leccion-[texto]-YYYY-MM-DD.html`

**Referencia principal:** `~/clawd/skills/contenido-a-leccion/SKILL.md`

**Fases:**
1. **Texto fuente** — Adri proporciona texto (pegado, archivo, o tema)
2. **Contexto literario** — Autor, época, movimiento, conexiones
3. **Configuración** — Nivel (2 ESO → 2 Bach), profundidad (rápida/completa/inmersión)
4. **Generación** — HTML con CSS+JS embebido, solo Google Fonts externo
5. **Revisión** — Verificar interactividad, corrección lingüística, diseño

**13 elementos interactivos:** fragmento destacable, línea del tiempo, mapa conceptual, pregunta de comprensión, vocabulario contextual, análisis guiado, comparativa, cita interactiva, escritura creativa, quiz de repaso, glosario emergente, audio, conexión intertextual.

**Preset por defecto:** Vintage Editorial. **Usa:** adri-style, excalidraw-illustrations, dataviz-educativa.

---

## 3. presentacion-html — Slides HTML

**Cuándo:** Adri pide presentación, slides, diapositivas, charla.

**Output:** HTML autocontenido → `Materiales-Educativos/presentaciones/presentacion-[tema]-YYYY-MM-DD.html`

**Referencia principal:** `~/clawd/skills/presentacion-html/SKILL.md`

**Fases:**
1. **Detección** — Contexto (clase, charla, pitch), duración, número de slides
2. **Contenido** — Buscar notas en vault si hay, estructurar secciones
3. **Estilo** — Elegir preset adri-style
4. **Generación** — 1 slide = 1 viewport, sin scroll
5. **PPTX** (opcional) — Script Python con `python-pptx`

**Reglas clave:** viewport-fit, flechas+teclado, colores de acento diferentes por sección, layouts variados, splits asimétricos (60/40).

**Usa:** adri-style, dataviz-educativa.

---

## 4. crear-cuestionario — Cuestionarios GIFT para Moodle

**Cuándo:** Adri pide cuestionario, quiz, test, preguntas para Moodle/Edixgal.

**Output:** `.gift` → `Materiales-Educativos/cuestionarios/[tema]-cuestionario-YYYY-MM-DD.gift`

**Referencia principal:** `~/clawd/skills/crear-cuestionario/SKILL.md`

**Fases:**
1. **Fuente** — Texto pegado, archivo, tema libre
2. **Configuración** — Categoría, cantidad (5/10/15/20), tipos, penalización
3. **Nivel** — Curso (1-4 ESO, 1-2 Bach)
4. **Generación** — Preview legible → confirmar → guardar

**Tipos:** opción múltiple, V/F, respuesta corta, emparejamiento, rellenar huecos, numérica, ensayo.

**Formato GIFT obligatorio:** HTML para formato (`<b>`, `<i>`, `<br>`), NUNCA Markdown. Escapar `\{`, `\}`, `\~`, `\=`, `\#`.

---

## 5. sesion-interactiva — Guiones de sesión de clase

**Cuándo:** Adri pide planificar clase, sesión, actividad, dinámica de aula.

**Output:** Markdown → `Materiales-Educativos/sesiones/sesion-[tema]-YYYY-MM-DD.md`

**Referencia principal:** `~/clawd/skills/sesion-interactiva/SKILL.md`

**Fases:**
1. **Contenido** — Tema o unidad
2. **Contexto** — Duración (25/50/90 min), nivel, espacio, recursos
3. **Estructura narrativa** — 8 patrones: arco circular, objetivos como incógnita, provocación inicial, descubrimiento guiado, debate estructurado, gamificación, taller creativo, investigación colaborativa
4. **Dinámica** — Individual, parejas, grupos, mixta
5. **Generación** — Guion minuto a minuto, facilitación, checklist de materiales

---

## 6. cmd-crear-h5p — Paquetes H5P y SCORM

**Cuándo:** Adri pide contenido H5P, actividad para Edixgal, paquete SCORM.

**Output:** `.h5p` o `.zip` → `Materiales-Educativos/h5p/`

**Referencia principal:** `~/clawd/skills/cmd-crear-h5p/SKILL.md`

**Requiere:** Python 3. Setup inicial: `cd ~/clawd/skills/cmd-crear-h5p/scripts && python3 setup_environment.py`

**23 tipos:** Multiple Choice, True/False, Fill in the Blanks, Drag and Drop, Mark the Words, Course Presentation, Interactive Video, Interactive Book, Flashcards, Dialog Cards, Memory Game, Crossword, Word Search, Timeline, Image Hotspots, Accordion, Summary, Essay, Branching Scenario, Question Set, Column, Game Map.

**Fases:** formato → tipo → fuente → configuración+nivel → generación+validación.

---

## 7. quality-check — Evaluación de materiales

**Cuándo:** Adri pide evaluar, revisar, o verificar calidad de un material educativo.

**Output:** Informe en conversación. Puntuación 1-5 por criterio, issues, sugerencias.

**Referencia principal:** `~/clawd/skills/quality-check/SKILL.md`

**Tipos evaluables:** examen, actividad, presentación, apuntes, cuestionario GIFT.

**Flujo:** identificar tipo → leer material → aplicar checklist específica → informe con puntuación, puntos fuertes, issues, sugerencias concretas.

---

## 8. obsidian-markdown — Referencia de sintaxis Obsidian

**Cuándo:** Al escribir notas en `~/clawd/obsidian-vault/`.

**No genera nada, es referencia.** Consultar para:
- Wikilinks: `[[nota]]`, `[[nota|alias]]`, `[[nota#heading]]`
- Embeds: `![[nota]]`, `![[imagen.png]]`
- Callouts: `> [!info]`, `> [!warning]` (13 tipos, plegables con `+`/`-`)
- Properties: YAML entre `---`
- Tags, Math LaTeX, Mermaid

**Referencia principal:** `~/clawd/skills/obsidian-markdown/SKILL.md`

---

## 9. informe-alumnos — Informes de seguimiento

**Cuándo:** Adri pide informe de un alumno para tutoría o seguimiento.

**Output:** Texto en gallego normativo → `Materiales-Educativos/informes/informe-[alumno]-YYYY-MM-DD.txt`

**Referencia principal:** `~/clawd/skills/informe-alumnos/SKILL.md`

**Idioma:** Gallego normativo SIEMPRE.

**Estructura fija:** (1) Comportamento e traballo diario, (2) Rendemento académico, (3) Cualificacións.

**Tono:** Profesional, constructivo. "Áreas de mellora", no juicios negativos directos.

---

## 10. agregador-informes — Informes agregados de varios profesores

**Cuándo:** Adri prepara reunión de tutoría con info de varios profes.

**Output:** Dos versiones → `Materiales-Educativos/informes/agregado-[alumno]-{gl,es}-YYYY-MM-DD.txt`

**Referencia principal:** `~/clawd/skills/agregador-informes/SKILL.md`

**Flujo:** nombre alumno → recibir info por materia (iterativo o todo de golpe) → filtro diplomático → generar gallego + español → guardar ambas.

---

## 11. writing-clearly — Reglas de escritura clara

**Cuándo:** Aplicar automáticamente al redactar textos largos (materiales, informes, notas).

**No genera nada, son reglas.** Strunk & White adaptado:
- Omitir palabras innecesarias ("el hecho de que" → "que")
- Voz activa sobre pasiva
- Afirmaciones positivas ("no recordó" → "olvidó")
- Palabras concretas sobre abstractas
- Un párrafo = una idea

**Referencia principal:** `~/clawd/skills/writing-clearly/SKILL.md`

---

## 12. dataviz-educativa — Gráficos SVG con matplotlib

**Cuándo:** Adri pide gráfico, chart, distribución de notas, comparativa visual.

**Output:** SVG + script Python → `Materiales-Educativos/graficos/`

**Referencia principal:** `~/clawd/skills/dataviz-educativa/SKILL.md`

**Requiere:** `matplotlib`. Ejecutar: `bash ~/clawd/skills/dataviz-educativa/scripts/run.sh script.py`

**Tipos:** barras, radar, heatmap, donut, gauge, timeline, sparkline, distribución, comparativa.

**Flujo:** datos → tipo de gráfico → paleta según preset adri-style → script Python → SVG.

**Usa:** adri-style (paleta de colores).

---

## 13. excalidraw-illustrations — Ilustraciones hand-drawn

**Cuándo:** Adri pide sketch, dibujo pizarra, diagrama esquemático, ilustración hand-drawn.

**Output:** PNG → `Materiales-Educativos/ilustraciones/ilustracion-[tema]-YYYY-MM-DD.png`

**Referencia principal:** `~/clawd/skills/excalidraw-illustrations/SKILL.md`

**Requiere:** `GEMINI_API_KEY` en entorno. Python con urllib (sin deps extra).

**Estilo:** Fondo blanco, trazo pizarra/hand-drawn, colores suaves. NO fotorrealista.

**Si hay texto:** deletrear letra por letra en el prompt a Gemini.

**Imágenes de referencia:** `skills/excalidraw-illustrations/references/reference1.png`, `reference2.png`

---

# Combinaciones frecuentes

| Petición | Skills |
|----------|--------|
| "Lección sobre el Lazarillo" | contenido-a-leccion + adri-style + excalidraw-illustrations |
| "Presentación de géneros literarios" | presentacion-html + adri-style + dataviz-educativa |
| "Cuestionario de sintaxis 3 ESO" | crear-cuestionario |
| "Planifica la clase de mañana" | sesion-interactiva |
| "Crossword H5P de vocabulario" | cmd-crear-h5p |
| "Revisa este examen" | quality-check |
| "Informes para reunión de tutoría" | agregador-informes |
| "Gráfico con las notas del grupo" | dataviz-educativa + adri-style |
| "Esquema del viaje del héroe" | excalidraw-illustrations |

---

# Setup en el MBP 2015

```bash
# 1. Clonar skills al workspace
cd ~/clawd
mkdir -p skills
mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/Downloads/Materiales-Educativos/{lecciones,presentaciones,cuestionarios,h5p,sesiones,informes,graficos,ilustraciones}
git clone git@github.com:adrianlaureda/adri-style.git skills/adri-style

# 2. Copiar el resto de skills desde la máquina principal (via SSH o rsync)
# Desde el Mac principal:
rsync -av ~/.dotfiles/ai/skills/{contenido-a-leccion,presentacion-html,crear-cuestionario,sesion-interactiva,cmd-crear-h5p,quality-check,obsidian-markdown,informe-alumnos,agregador-informes,dataviz-educativa,excalidraw-illustrations} adrianlauredaleon@Adrians-MacBook-Pro.local:~/clawd/skills/

# 3. Copiar writing-clearly (nombre adaptado)
rsync -av ~/.dotfiles/ai/skills/writing-clearly-and-concisely/ adrianlauredaleon@Adrians-MacBook-Pro.local:~/clawd/skills/writing-clearly/

# 4. Dependencias Python (en MBP 2015)
pip3 install matplotlib python-pptx

# 5. Setup H5P (en MBP 2015)
cd ~/clawd/skills/cmd-crear-h5p/scripts && python3 setup_environment.py

# 6. Verificar GEMINI_API_KEY (en MBP 2015)
echo $GEMINI_API_KEY
```
