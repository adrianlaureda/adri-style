# Color y tema

El preset aporta identidad; la superficie elige cómo aplicarla. Los colores
base y acento viven en `presets.json`; los temas y tokens completos se muestran
en `style-presets.md`. No copiar una paleta genérica encima de un preset.

Texto normal: contraste mínimo 4.5:1 sobre el fondo efectivo, incluida la
composición alpha. Texto grande: 3:1. Controles y foco: comprobar visibilidad
sobre todos los fondos que atraviesan. Aumentar el peso no compensa un contraste
insuficiente. Los grises `text-muted` también necesitan contraste si llevan texto.

El acento original puede servir como fondo o muestra de identidad sin ser
válido para texto pequeño. Catálogo y exports derivan `accent-ink` para texto
sobre el fondo base y `on-accent` para texto sobre el acento. Si cambia el fondo,
recalcular el contraste; no suponer que `--bg` funciona como texto de un botón.

El modo inicial procede de `mode_default` salvo contrato de superficie. El
bootstrap incluye tema dual y persistencia protegida frente a localStorage
bloqueado. Su icono indica la acción: luna en light para activar oscuro; sol en
dark para activar claro. Ver implementación única en `templates/bootstrap-adri.html`.

En impresión: fondo blanco, texto oscuro, eliminar toggles, animaciones, fondos
ornamentales y alturas de viewport. Mantener datos y significado sin depender
del color. Revisar también páginas generadas desde modo oscuro.

## Semáforo educativo

Verde identifica aprobado (nota ≥5), amarillo advierte riesgo cuando el contexto
lo define y rojo suspenso (<5). Acompañar con nota/etiqueta, nunca solo color.
Las demás métricas usan neutros. Las variantes claras de badges están en
`base.css`; no usar amarillo brillante como texto sobre blanco.
