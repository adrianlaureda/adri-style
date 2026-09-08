# adri-style v5.8

Sistema de diseño personal con 28 presets, tokens reutilizables, plantillas y validadores para agentes que generan HTML, dashboards, presentaciones y materiales educativos.

Este repo es la fuente versionada. La instalación local en `~/.dotfiles/ai/skills/adri-style/` debe derivarse del repo, no al revés.

## Estructura

```text
SKILL.md                         # Contrato operativo del sistema
templates/
  bootstrap-adri.html            # Punto de partida canónico
references/
  style-presets.md               # Catálogo humano de 28 presets
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
  base.css                       # Base inyectable para consumidores existentes
  preset-catalog.html            # Catálogo generado y comparador
scripts/
  audit-adri.sh                  # Auditoría rápida
  audit-adri-full.sh             # Auditoría completa
  export.py                      # Exportador DESIGN.md
  generate_catalog.py            # Generador determinista del catálogo
  generate_docs.py               # Tablas humanas y coherencia CSS/JSON
  preset_assets.py               # Fuentes y colores accesibles derivados
  measure-adri.sh                # Métricas de outputs
  validate_contract.py           # Validador único de catálogo e inyección
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

## Validación sin instalaciones

```bash
python3 -m unittest discover -s tests -v
node tests/run-browser.mjs
```

La batería de navegador requiere Node 22+ y Chrome ya instalados. Se puede
indicar `CHROME_BIN`. Comprueba 28 presets, cuatro superficies, comparación,
tema, anchos 320/375/768/1440 e impresión. CI ejecuta las mismas pruebas.
La carga real de fuentes externas requiere red y se revisa visualmente;
los checks de estructura no confunden fallback con una fuente descargada.

Tras editar `presets.json`, ejecutar `python3 scripts/generate_catalog.py` y
`python3 scripts/generate_docs.py`. Regenerar los ejemplos DESIGN.md con
`python3 scripts/export.py --preset bold-signal` y `--preset paper-and-ink`.
Los tests detectan drift de tablas, bloques CSS, catálogo y exports.

Ver [contrato de inyección y consumidores](references/injection-contract.md).
Se mantienen los 27 IDs originales y fuentes; los alias sin número se normalizan. La base
inyectable permanece; `global.css` se ha retirado por duplicación. No combinar
`base.css` con el reset autocontenido del bootstrap.

`audit-adri-full.sh` usa html-validate/pa11y ya instalados y devuelve 2 si faltan;
no usa npx ni instala paquetes. Impeccable sigue siendo una auditoría opcional
adicional, separada de los tests reproducibles del repositorio.

## OpenClaw

`OPENCLAW.md` contiene el paquete complementario. `setup-cora.sh` clona este repo en el workspace de Cora.

## Adri Console

`28-adri-console` conserva Barlow local (OFL), títulos 500, cuerpo 400 y el
fondo gris con gradiente sutil de `app-adri-console/app/src/index.css`. Se admite
este gradiente contextual; se evitan transiciones muy marcadas y ornamentación
que parezca generada por plantilla. No traslada la navegación de la aplicación.
Muestra reutilizable: [templates/adri-console.html](templates/adri-console.html).
Export: [exports/adri-console.design.md](exports/adri-console.design.md).
El CSS local se distribuye junto a `assets/fonts/barlow/`; sus rutas son relativas
al catálogo en `assets/` y deben ajustarse al copiarlo a otro documento.

## Licencia

Uso personal. Adrian Laureda, 2026.
