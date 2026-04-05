# Animación

Fuente principal: Emil Kowalski. Principio: las animaciones deben ser casi
imperceptibles — si el usuario nota la animación, es demasiado.

## Reglas

- **Always** usar ≤300ms para interacciones de UI
- **Always** animar solo transform y opacity (propiedades composited)
- **Always** usar ease-out para elementos que entran, ease-in para los que salen
- **Always** definir transform-origin desde el punto de activación, no desde el centro
- **Never** animar padding, margin, width, height, border (causan reflow/layout shift)
- **Never** animar desde scale(0) — mínimo 0.9 para mantener contexto
- **Never** usar animaciones >600ms (parecen lentas)
- **Consider** custom cubic-bezier sobre ease genérico para más personalidad
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

## Checklist

- [ ] Ninguna animación supera 600ms
- [ ] Solo se animan transform y opacity
- [ ] Hover no desplaza más de 2px
- [ ] No hay scale por debajo de 0.9
- [ ] transform-origin correcto según punto de activación
