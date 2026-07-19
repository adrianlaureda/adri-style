# Layout

Estructura de página, grid y responsive del sistema Adri Style.
Principio: espacio generoso, contenido centrado, responsive natural.

## Reglas

- **Por superficie**: 1000px es el default de páginas generales, no de slides,
  galerías full-bleed o consolas densas.
- **Always** limitar texto de lectura a aproximadamente 65ch.
- **Always** adaptar grids al contenido y al viewport; 3→2→1 es una receta,
  no un contrato universal.

## Container estándar

```css
.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 1.5rem;  /* var(--space-md) */
}
```

## Clase .prose (bloques de lectura)

```css
.prose {
  max-width: 65ch;
  line-height: 1.45;
  margin: 0 auto;
}
.prose p + p {
  margin-top: 1em;
}
```

- Usar para: artículos, descripciones largas, contenido de lectura
- Line-height 1.45 (no 1.5 genérico, Butterick)

## Grid de tarjetas

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}
```

## Breakpoints

| Breakpoint | Columnas | Ajuste |
|------------|----------|--------|
| >900px | 3 columnas | Layout completo |
| 600-900px | 2 columnas | Tablet |
| <600px | 1 columna | Móvil, padding reducido |

```css
@media (max-width: 900px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .grid { grid-template-columns: 1fr; }
  .container { padding: 0 1rem; }
}
```

## Espaciado entre secciones

| Espacio | Variable | Valor | Uso |
|---------|----------|-------|-----|
| xs | --space-xs | 0.5rem | Dentro de componentes |
| sm | --space-sm | 1rem | Entre elementos hermanos |
| md | --space-md | 1.5rem | Padding de container |
| lg | --space-lg | 2.5rem | Entre secciones |
| xl | --space-xl | 4rem | Separación de bloques grandes |

## Checklist

- [ ] Container no supera 1000px
- [ ] Bloques de texto usan .prose (65ch)
- [ ] Grid es responsive: 3→2→1 columna
- [ ] Padding mínimo 1rem en móvil
- [ ] Espaciado generoso entre secciones (≥2.5rem)
