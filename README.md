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
  presets.json                   # Contrato estructurado canónico
  presets.schema.json            # Esquema documentado del contrato
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
  base.css                       # Base legacy, no universal
  global.css                     # Template legacy pendiente de retirada
  preset-catalog.html            # Catálogo generado y comparador
scripts/
  audit-adri.sh                  # Auditoría rápida
  audit-adri-full.sh             # Auditoría completa
  export.py                      # Exportador DESIGN.md
  generate_catalog.py            # Generador determinista del catálogo
  measure-adri.sh                # Métricas de outputs
  validate_contract.py           # Validador fail-closed
tests/fixtures/surfaces/         # Un contrato aplicado a cuatro superficies
exports/                         # Ejemplos DESIGN.md generados
```

## Uso

1. Elegir preset en `assets/preset-catalog.html`.
2. Para una página general, copiar `templates/bootstrap-adri.html`; para una superficie especializada, partir de su skill o fixture.
3. Sustituir fuentes, tokens y `data-preset` de forma coherente.
4. Ejecutar `scripts/validate_contract.py <archivo.html>` y `scripts/audit-adri.sh <archivo.html>`.

Bold Signal es el default para marca Adri o contexto ambiguo. Los contextos funcionales, educativos y editoriales conservan sus presets específicos.

## Contrato v5.8

`references/presets.json` gobierna ids, fuentes, modos y estado. El catálogo y
los exports se generan o validan contra él. `style-presets.md` conserva
explicaciones y CSS detallado sin redefinir esos campos.

`audit-adri.sh` usa exit 0 para aprobación, 1 para incumplimiento y 2 para
infraestructura incompleta. Un exit 2 nunca cuenta como verde en métricas.

## OpenClaw

`OPENCLAW.md` contiene el paquete complementario. `setup-cora.sh` clona este repo en el workspace de Cora.

## Licencia

Uso personal. Adrian Laureda, 2026.
