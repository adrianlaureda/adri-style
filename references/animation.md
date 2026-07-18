# Animación

Fuente principal: Emil Kowalski. Principio: las animaciones deben ser casi
imperceptibles — si el usuario nota la animación, es demasiado.

## Reglas

- **Always** usar ≤300ms para interacciones de UI
- **Always** animar solo `transform` y `opacity` (propiedades composited)
- **Always** usar ease-out para elementos que entran, ease-in para los que salen
- **Always** definir transform-origin desde el punto de activación, no desde el centro
- **Always** para barras de progreso usar `transform: scaleX/scaleY` con `transform-origin`, NO `transition: width/height` (ver `components.md §14`)
- **Always** respetar `prefers-reduced-motion: reduce` desactivando animaciones no esenciales
- **Never** animar `padding`, `margin`, `width`, `height`, `border`, `top`, `left` (causan reflow/layout shift; detectado en producción 2026-05-08 en 2 sites)
- **Never** animar desde scale(0) — mínimo 0.9 para mantener contexto
- **Never** usar animaciones >600ms (parecen lentas)
- **Never** usar `cubic-bezier(...> 1.0...)` (overshoot/bounce/elastic) por defecto. Solo si el preset lo justifica como decisión documentada (ej. preset Micro-interactions con bounce intencional). Detectado en producción como anti-pattern AI-tell en `branding-adri` y `adri-app`.
- **Consider** custom cubic-bezier sobre ease genérico para más personalidad — preferir curvas de salida natural (`cubic-bezier(0.16, 1, 0.3, 1)`) sobre overshoot
- **Consider** blur(2px) como fallback sutil cuando otras animaciones no funcionan

## Valores de referencia

| Propiedad | Valor | Uso |
|-----------|-------|-----|
| Duración UI | 150-300ms | Hover, toggle, feedback |
| Duración entrada | 300-500ms | Fade-in, slide-in |
| Fade-in slides | ≤300ms | Presentaciones HTML |
| Ease-out | cubic-bezier(0.16, 1, 0.3, 1) | Entrada de elementos |
| Ease-in | cubic-bezier(0.4, 0, 1, 1) | Salida de elementos |
| Scale :active | 0.97 | Feedback de click en botones |
| Scale mínimo | 0.9 | Nunca escalar por debajo |
| Blur fallback | 2px | Transición sutil de aparición |
| Hover translateY | -2px máximo | Efecto de elevación |

## Ejemplos

<!-- Good: animación de entrada sutil -->
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(12px);  /* Desplazamiento sutil */
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.card {
  animation: fadeInUp 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

<!-- Bad: animación exagerada -->
```css
@keyframes bounce {
  from {
    opacity: 0;
    transform: translateY(50px) scale(0.5);  /* Demasiado movimiento */
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
.card {
  animation: bounce 0.8s ease;  /* Demasiado lenta */
}
```

<!-- Good: hover discreto -->
```css
.card:hover {
  transform: translateY(-2px);
  border-color: var(--text-secondary);
  transition: all 0.2s ease;
}
```

<!-- Bad: hover exagerado -->
```css
.card:hover {
  transform: translateY(-8px) scale(1.05);  /* Movimiento excesivo */
  box-shadow: 0 20px 40px rgba(0,0,0,0.3);  /* Sin box-shadow en adri-style */
}
```

## Stagger de entrada con CSS custom property

Para listas de N elementos que entran en cascada (timeline, cards, ítems de menú). Usar `--i` en el HTML y `calc(var(--i, 0) * Xms)` en el CSS. Más robusto que `nth-child` porque funciona con cualquier N sin enumerar selectores.

```html
<!-- HTML: cada item lleva --i con su índice (0-based) -->
<div class="card" style="--i:0">…</div>
<div class="card" style="--i:1">…</div>
<div class="card" style="--i:2">…</div>
```

```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.card {
  animation: fadeInUp 0.35s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: calc(var(--i, 0) * 65ms);
}
```

Valores de referencia para el delay:
- `50ms` — listas cortas (≤4 items), ritmo rápido
- `65ms` — timelines y pipelines (5-8 items), ritmo natural
- `80ms` — listas largas (>8 items) donde el stagger es narrativo

## Checklist

- [ ] Ninguna animación supera 600ms
- [ ] Solo se animan `transform` y `opacity`
- [ ] Hover no desplaza más de 2px
- [ ] No hay scale por debajo de 0.9
- [ ] transform-origin correcto según punto de activación
- [ ] **v5.3** Barras de progreso usan `transform: scaleX/scaleY`, NO `width/height` animado
- [ ] **v5.3** No hay `cubic-bezier(...> 1.0...)` (overshoot/bounce) por defecto
- [ ] **v5.3** `@media (prefers-reduced-motion: reduce)` desactiva animaciones no esenciales
