# Contrato de inyección

El repositorio es la fuente versionada. Las copias instaladas en dotfiles y
OpenClaw se sincronizan por sus propios flujos; editar este repo no las actualiza.

## Autoridad y compatibilidad

`presets.json` fija IDs, familias, pesos permitidos, color base/acento, modo y
estado. `style-presets.md` conserva tokens de superficie, temas alternativos,
CSS de composición y recetas. Sus tablas son generadas; sus bloques CSS se
contrastan con los campos canónicos. No se mantiene otro catálogo manual.

Declarar `data-preset` en `html` o un contenedor real (`body`, `main`, `div`,
`section`, `article`, `aside`, `header`, `footer`, `nav`). Se validan todos los
contenedores declarados, también si la página mezcla presets. Los slugs sin
número se resuelven desde el ID canónico: `soffia-warm` → `14-soffia-warm`.
Los outputs nuevos usan el ID completo. `data-theme`, si existe junto a la
marca, debe ser `light` o `dark`; la superficie puede elegir otro tema inicial.

## Carga de fuentes

Se aceptan enlaces de stylesheet de Google Fonts/Fontshare con familias exactas,
`@font-face` con `src`, y CSS locales enlazados o importados (ciclos limitados).
Un `font-family` solo selecciona una fuente: no demuestra que esté cargada.
Comentarios, scripts, templates, preconnect y nombres parciales no son prueba.
No hay excepciones por llamar un archivo `adri-overrides.css`.

El validador es estático y no hace peticiones de red. No comprueba que un WOFF
responda, que un `local()` exista o que un selector aplique a un elemento: eso
se verifica en navegador con `document.fonts`, estilos calculados y capturas.
Los CSS remotos distintos de los proveedores reconocidos deben verificarse
localmente (guardar el HTML y sus recursos mediante el flujo del consumidor).
No se resuelven paquetes de bundler ni rutas absolutas de servidor.

## Orden de inyección

Para consumidores de `base.css`: reset/base primero, después el bloque completo
del preset y sus overrides `[data-theme]`, después CSS propio de la superficie.
Copiar las cargas tipográficas y declarar `data-preset`. La base conserva clases
como `.container`, `.prose`, `.btn`, `.badge` y `.card`; usar cajas solo si pasan EAR.
`global.css` era otra base y se ha eliminado: usar `base.css` con el preset.

Para una página autocontenida, `bootstrap-adri.html` contiene su base y toggle.
No añadir además `base.css`: duplicaría reset y tokens. Las presentaciones
conservan su CSS de viewport y los dashboards su contrato semántico.

## Consumidores revisados (solo lectura, 2026-09-08)

| Consumidor | Contrato conservado |
|---|---|
| `presentacion-html` | `data-preset` en html/contenedor, Lucide, CSS viewport propio |
| `dashboard-educativo` | alias `soffia-warm`, semáforo para notas, superficie propia |
| `contenido-a-leccion` | preset + `base.css` + fuentes, Vintage Editorial/Paper & Ink |
| `OPENCLAW.md`, `CLAUDE-APPEND.md` | bootstrap y rutas del paquete de skills |
| `uso_real` en JSON | IDs y familias conservados; etiquetas históricas no prueban actividad actual |

`frontend-design` no estaba disponible en la ruta local documentada. No se
han modificado consumidores ni instalaciones. No se encontraron importaciones
de `assets/global.css` en los skills locales revisados.

## Verificación

`python3 -m unittest discover -s tests -v` comprueba contrato, negativos,
exports, tablas y catálogo. `node tests/run-browser.mjs` usa Node 22+ y Chrome
ya instalados, sin paquetes npm. `scripts/audit-adri.sh` añade Impeccable cuando
está instalado. `audit-adri-full.sh` añade html-validate/pa11y instalados.

Exit 0: pasa ese nivel. Exit 1: incumplimiento. Exit 2: infraestructura
incompleta, nunca aprobación. Las pruebas de repositorio y navegador no
sustituyen una auditoría WCAG completa de cada output final.
