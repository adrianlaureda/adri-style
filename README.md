# adri-style v5.1

Sistema de diseno personal con 15 presets visuales, tipografia fluida y layouts expresivos.

Pensado como **skill inyectable** para agentes de IA (Claude Code, OpenClaw) que generan materiales educativos: presentaciones HTML, dashboards, lecciones interactivas, ejercicios.

## Estructura

```
SKILL.md                    # Instrucciones principales del skill
references/
  style-presets.md          # 15 presets con variables CSS completas
  typography.md             # Sistema tipografico fluido (Utopia)
  composition.md            # Composicion visual dinamica
  animation.md              # Easings y transiciones
  color-and-theme.md        # Tema dual, contraste, semantica
  components.md             # Cards, botones, patrones premium
  layout.md                 # Grid, container, responsive
assets/
  base.css                  # CSS base inyectable con reset y tema dual
  global.css                # Template CSS (default: Minimalista Adri)
  preset-catalog.html       # Catalogo visual de los 15 presets
```

## Presets disponibles

| Preset | Uso recomendado |
|--------|----------------|
| Minimalista Adri | Dashboards, herramientas |
| Swiss Modern | Datos, informes |
| Bold Signal | Landing pages, presentaciones |
| Soffia Warm | Editorial calido |
| Creative Voltage | Impacto visual |
| Electric Studio | Funcional, ejercicios |
| Pastel Geometry | Actividades, infantil |
| Split Pastel | Ejercicios interactivos |
| Vintage Editorial | Literario, clasico |
| Paper & Ink | Lectura, documentos |
| Dark Botanical | Naturaleza, ciencias |
| Neon Cyber | Futurista, gaming |
| Notebook Tabs | Pestanas, presentaciones |
| Terminal Green | Hacker, datos |
| Retro Pop | Colorido, dinamico |

## Uso con OpenClaw

Clonar en el workspace de OpenClaw y anadir como referencia en las instrucciones del agente. Ver seccion de configuracion en el repo.

## Licencia

Uso personal. Adrian Laureda, 2026.
