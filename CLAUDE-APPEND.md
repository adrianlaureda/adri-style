
# Skills de materiales educativos

Tienes acceso a un paquete de skills especializados en `~/clawd/skills/` para generar materiales educativos de alta calidad. Consulta las instrucciones completas en `~/clawd/skills/adri-style/OPENCLAW.md`.

## Cuándo activar estos skills

Cuando Adri pida crear, generar o revisar materiales educativos. Para todo lo demás, sigue funcionando como siempre.

## Contexto educativo de Adri

- Docente de Lengua Castellana y Literatura, IES en Galicia
- Sistema gallego, calificaciones 1-10 (aprobado >= 5), idiomas español/gallego
- Cursos: 1 ESO a 2 Bachillerato. Plataforma LMS: Moodle/Edixgal

## Skills disponibles

| Trigger (Adri pide...) | Skill | Lee primero |
|------------------------|-------|-------------|
| Lección, material interactivo, actividad sobre texto literario | contenido-a-leccion | `skills/contenido-a-leccion/SKILL.md` |
| Presentación, slides, diapositivas, charla | presentacion-html | `skills/presentacion-html/SKILL.md` |
| Cuestionario, quiz, test, preguntas Moodle | crear-cuestionario | `skills/crear-cuestionario/SKILL.md` |
| Planificar clase, sesión, dinámica de aula | sesion-interactiva | `skills/sesion-interactiva/SKILL.md` |
| Contenido H5P, actividad Edixgal, SCORM | cmd-crear-h5p | `skills/cmd-crear-h5p/SKILL.md` |
| Evaluar, revisar calidad de un material | quality-check | `skills/quality-check/SKILL.md` |
| Informe de un alumno para tutoría | informe-alumnos | `skills/informe-alumnos/SKILL.md` |
| Informes de varios profes sobre un alumno | agregador-informes | `skills/agregador-informes/SKILL.md` |
| Gráfico, chart, distribución, comparativa | dataviz-educativa | `skills/dataviz-educativa/SKILL.md` |
| Sketch, dibujo pizarra, diagrama hand-drawn | excalidraw-illustrations | `skills/excalidraw-illustrations/SKILL.md` |

## Skills de soporte (no se invocan solos)

- **adri-style** — Sistema de diseño visual. Leer `skills/adri-style/SKILL.md` SIEMPRE que generes HTML. Elegir preset de `skills/adri-style/references/style-presets.md`.
- **obsidian-markdown** — Referencia de sintaxis. Consultar al escribir en `~/clawd/obsidian-vault/`.
- **writing-clearly** — Reglas de escritura. Aplicar automáticamente en textos largos.

## Dónde guardar output

Todo material generado va a `~/clawd/output/` en la subcarpeta correspondiente:
lecciones/, presentaciones/, cuestionarios/, h5p/, sesiones/, informes/, graficos/, ilustraciones/

## Reglas de formato

- **HTML**: siempre autocontenido (CSS+JS embebido), solo Google Fonts externo
- **GIFT** (Moodle): formato con HTML (`<b>`, `<i>`, `<br>`), NUNCA Markdown
- **Informes de tutoría**: gallego normativo, texto plano
- **Notas Obsidian**: sintaxis Obsidian Flavored Markdown

## Restricciones para estos skills

- Guardar output SOLO en `~/clawd/output/` o `~/clawd/obsidian-vault/`
- NO subir nada a Edixgal, XADE ni ningún servicio web con credenciales
- NO enviar emails ni mensajes a terceros
- NO instalar dependencias sin permiso
