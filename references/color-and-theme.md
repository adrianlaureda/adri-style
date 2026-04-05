# Color y tema

Fuentes: Butterick (uso del color), práctica actual de adri-app.com.
Principio: el color debe ser funcional, no decorativo.

## Reglas

- **Always** implementar tema dual (oscuro por defecto)
- **Always** usar #1a1a1a en light mode para texto (no negro puro, Butterick)
- **Always** reservar color para enlaces (denota clickabilidad, Butterick)
- **Always** persistir preferencia de tema en localStorage
- **Never** usar colores saturados o de acento llamativos
- **Never** usar gradientes de fondo
- **Never** usar blanco puro (#fff) sobre negro puro (#000) en texto largo
- **Consider** el semáforo educativo para dashboards de calificaciones
- **Consider** "cuando todo está enfatizado, nada lo está" (principio Butterick)

## Variables CSS - Modo oscuro (default)

| Variable | Valor | Uso |
|----------|-------|-----|
| --bg | #0a0a0a | Fondo principal (near-black, NUNCA #000000) |
| --bg-surface | #111111 | Fondo de tarjetas (+3% lightness) |
| --bg-elevated | #1a1a1a | Fondo elevado, hover (+6% lightness) |
| --border | #222222 | Bordes |
| --text | #ffffff | Texto principal |
| --text-secondary | #999999 | Texto secundario |
| --text-muted | #666666 | Texto silenciado |

## Variables CSS - Modo claro

| Variable | Valor | Uso |
|----------|-------|-----|
| --bg | #ffffff | Fondo principal |
| --bg-surface | #fafafa | Fondo de tarjetas |
| --bg-elevated | #f5f5f5 | Fondo elevado |
| --border | #e5e5e5 | Bordes |
| --text | #1a1a1a | Texto (no #000, Butterick) |
| --text-secondary | #666666 | Texto secundario |
| --text-muted | #999999 | Texto silenciado |

## Semáforo educativo

Para dashboards y materiales con calificaciones (1-10, aprobado ≥5):

| Color | Hex | Uso |
|-------|-----|-----|
| Verde | #22c55e | Aprobado (≥5) |
| Amarillo | #eab308 | Advertencia (5-6, riesgo) |
| Rojo | #ef4444 | Suspenso (<5) |

## Toggle de tema

```javascript
// Leer tema guardado
const theme = localStorage.getItem('theme') || 'dark';
if (theme === 'light') {
  document.documentElement.setAttribute('data-theme', 'light');
}
// Icono: luna (lucide:moon) en oscuro → sol (lucide:sun) en claro
```

## Checklist

- [ ] Variables CSS con ambos temas definidas
- [ ] Light mode usa #1a1a1a para --text (no #000000)
- [ ] Color reservado para enlaces
- [ ] Toggle con persistencia localStorage
- [ ] Contraste suficiente en ambos modos
