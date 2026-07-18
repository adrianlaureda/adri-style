# adri-style v5.8

Sistema de diseño personal con 27 presets, tokens reutilizables, plantillas y validadores para agentes que generan HTML, dashboards, presentaciones y materiales educativos.

Este repo es la fuente versionada. La instalación local en `~/.dotfiles/ai/skills/adri-style/` debe derivarse del repo, no al revés.

## Estructura

```text
SKILL.md                         # Contrato operativo del sistema
templates/
  bootstrap-adri.html            # Punto de partida canónico
references/
  style-presets.md               # Catálogo humano de 27 presets
  presets.json                   # Mirror programático
  identity-adri.md               # Identidad Bold Signal
  typography.md                  # Tipografía y escala fluida
  composition.md                 # Composición
  animation.md                   # Movimiento
  color-and-theme.md             # Tema, contraste y semántica
  colors-oklch.md                # Conversión de acentos
  components.md                  # Componentes y Test de la Caja
  layout.md                      # Grid y responsive
  ux-guidelines.md               # Reglas UX transversales
  design-md-spec.md              # Exportación DESIGN.md
assets/
  base.css                       # CSS base inyectable
  global.css                     # Template legacy pendiente de retirada
  preset-catalog.html            # Catálogo visual legacy pendiente de regenerar
scripts/
  audit-adri.sh                  # Auditoría rápida
  audit-adri-full.sh             # Auditoría completa
  export.py                      # Exportador DESIGN.md
  measure-adri.sh                # Métricas de outputs
exports/                         # Ejemplos DESIGN.md generados
```

## Uso

1. Copiar `templates/bootstrap-adri.html`.
2. Elegir preset en `references/style-presets.md`.
3. Sustituir fuentes, tokens y `data-preset` de forma coherente.
4. Ejecutar `scripts/audit-adri.sh <archivo.html>`.

Bold Signal es el default para marca Adri o contexto ambiguo. Los contextos funcionales, educativos y editoriales conservan sus presets específicos.

## Estado de consolidación

La versión v5.8 se recuperó desde la skill instalada el 2026-07-18. PRO-211 debe corregir después la deriva interna detectada:

- `SKILL.md`: v5.8.
- `references/presets.json`: v5.6.
- `assets/preset-catalog.html`: v5.2 y 25 previews.

No editar esos mirrors por separado: la siguiente fase debe introducir generación y validación de coherencia.

## OpenClaw

`OPENCLAW.md` contiene el paquete complementario. `setup-cora.sh` clona este repo en el workspace de Cora.

## Licencia

Uso personal. Adrian Laureda, 2026.
