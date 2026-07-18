# DESIGN.md Spec — Subset compatible Stitch + extensiones Adri

**Estado**: spec canónica del formato `.design.md` exportado por `adri-style`. Vive en `adri-style/references/` porque `adri-style` es la **fuente canónica de diseño**. Los `.design.md` son **canal de interop, nunca fuente**.

## 1. Filosofía

`.design.md` es un **export portable** que permite intercambiar un preset visual con herramientas externas (Google Stitch, Visily, prototipadores externos) sin perder los tokens canónicos.

- **`adri-style` gana** ante cualquier conflicto, salvo override explícito del usuario.
- **No reimportar automáticamente**: si una herramienta externa modifica un `.design.md`, no se aplica al sistema canónico sin revisión manual.
- **Subset compatible** con la spec Google/Stitch de design tokens, ampliado con extensiones Adri (`text-secondary`, `text-muted`, `accent-surface`, alpha conservation, etc.).

## 2. Estructura del archivo

`.design.md` = **frontmatter YAML** + **cuerpo Markdown** (documentación humana).

### Frontmatter YAML (obligatorio)

```yaml
---
version: "alpha"
name: "<Nombre del preset>"
description: "<Descripción 1-2 frases>"
colors:
  bg: "#hex"
  bg-surface: "#hex"
  bg-elevated: "#hex"
  border: "#hex"
  text: "#hex"
  text-secondary: "#hex"
  text-muted: "#hex"
  accent: "#hex"
  accent-surface: "#hex"
typography:
  display:
    fontFamily: "'Nombre', system-ui, sans-serif"
    fontSize: "clamp(...)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.04em"
  body:
    fontFamily: "'Nombre', system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "0"
  mono:
    fontFamily: "'Nombre', monospace"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0"
    fontFeature: "tnum"
spacing:
  "3xs": "4px"
  "2xs": "8px"
  "xs": "12px"
  "s": "16px"
  "m": "24px"
  "l": "32px"
  "xl": "48px"
  "2xl": "72px"
  "3xl": "112px"
rounded:
  base: "0px"
  pill: "9999px"
components:
  card:
    background: "token(colors.bg-surface)"
    borderColor: "token(colors.border)"
    borderRadius: "token(rounded.base)"
    padding: "token(spacing.m)"
  button-primary:
    background: "token(colors.accent)"
    color: "token(colors.bg)"
    borderRadius: "token(rounded.base)"
    paddingX: "token(spacing.m)"
    paddingY: "token(spacing.2xs)"
    fontWeight: 500
  input:
    background: "token(colors.bg-surface)"
    borderColor: "token(colors.border)"
    borderRadius: "token(rounded.base)"
    paddingX: "token(spacing.xs)"
    paddingY: "token(spacing.2xs)"
# color alpha notes: <comentario sobre canal alpha conservado en CSS original>
---
```

### Cuerpo Markdown (recomendado)

Tras el frontmatter, secciones documentales humanas:

- `## Overview` — descripción extendida.
- `### Ideal for` — casos de uso.
- `### Notes` — notas sobre modo claro/oscuro, peculiaridades.
- `## Colors` — tabla `| Token | Hex | Fuente CSS |` con todos los tokens.
- `## Typography` — tabla `| Rol | Font family | Weight | Line height | Letter spacing |`.
- `## Layout` — container, prose, breakpoints, spacing scale.
- `## Elevation & Depth` — gradientes, sombras, planos.
- `## Shapes` — radius base, pills.
- `## Components` — descripción de cada componente.
- `## Do's and Don'ts` — reglas duras del preset.

## 3. Compatible subset (Google/Stitch)

Estos campos son **compatibles directamente** con la spec Google/Stitch de design tokens:

| Campo `.design.md` | Equivalente Stitch | Notas |
|---|---|---|
| `colors.bg` | `colors.background.primary` | hex base sin alpha |
| `colors.text` | `colors.foreground.primary` | hex base sin alpha |
| `colors.accent` | `colors.brand.primary` | hex base |
| `typography.display.fontFamily` | `typography.heading.fontFamily` | con fallback `system-ui` |
| `typography.body.fontFamily` | `typography.body.fontFamily` | |
| `spacing.*` | `spacing.*` | mismas claves t-shirt size |
| `rounded.base` | `radius.base` | |
| `components.card.*` | `components.card.*` | tokens del componente |

**Reglas de compatibilidad:**

1. Los hex declarados en `colors:` son **siempre el color base sRGB sin alpha**.
2. El canal alpha de origen se conserva en la tabla `## Colors` del cuerpo Markdown (columna `Fuente CSS`) y en el comentario final del frontmatter (`# color alpha notes`).
3. Si una herramienta externa parsea solo el frontmatter, obtiene el hex base — correcto para preview.
4. `token(<path>)` es la sintaxis canónica para referenciar valores del propio frontmatter. Stitch lo soporta; otras herramientas pueden necesitar resolución previa.

## 4. Extensiones Adri (no estándar, documentar como propias)

Estos campos son **extensiones Adri** que las herramientas externas pueden ignorar:

| Campo | Razón |
|---|---|
| `colors.text-secondary`, `colors.text-muted` | jerarquía tipográfica fina, no estándar Stitch |
| `colors.accent-surface` | variante alpha para backgrounds tintados (anti-AI-slop) |
| `colors.bg-surface`, `colors.bg-elevated` | 3 planos de elevación |
| `typography.mono.fontFeature: "tnum"` | tabular-nums para datos numéricos |
| `spacing` con escala "3xs"-"3xl" | Utopia fluid scale, no t-shirt simple |
| `rounded.pill: "9999px"` | pills explícitas |
| Comentario `# color alpha notes:` | conservación de canal alpha original |

**Convención**: las extensiones se documentan en `## Notes` del cuerpo Markdown.

## 5. Reglas de consistencia `components` ↔ `colors/rounded/spacing`

Cuando un componente referencia un valor con `token(<path>)`:

- El path **debe existir** en el frontmatter.
- Si se quiere un valor literal en vez de token, escribirlo directamente (`background: "#0e0e0e"`).
- **No mezclar**: dentro de la misma clave `card.background`, o es `token(...)` o es hex literal. No es válido `"token(colors.bg-surface)"` si la clave `colors.bg-surface` no existe.

**Validador (§7) detecta**:
- Hex literales que duplican un token existente (ej: `background: "#0e0e0e"` cuando `colors.bg-surface == "#0e0e0e"`) → recomendar `token(colors.bg-surface)`.
- `token(<path>)` con path inexistente.
- Mezcla incoherente entre `components.card.background` con hex y `borderColor` con token.

## 6. Reglas de no-reimport

- Si una herramienta externa edita un `.design.md` y devuelve el archivo modificado, **no aplicar automáticamente** al sistema `adri-style`.
- El usuario revisa los cambios y decide si actualizar:
  - Tokens canónicos → modificar `references/style-presets.md` y `presets.json`.
  - Cambios solo de documentación → puede aplicarse a `.design.md` sin tocar lo canónico.
- **Versión `alpha`** señala que el formato puede cambiar; bump a `1.0` cuando esté estable.

## 7. Validador Python

Script mínimo para validar un `.design.md`:

```python
#!/usr/bin/env python3
"""Validador .design.md — verifica frontmatter, claves obligatorias y tokens coherentes."""
import re, sys, yaml

REQUIRED = ("colors", "typography", "spacing", "rounded", "components")
COLOR_KEYS_REQ = ("bg", "bg-surface", "bg-elevated", "border", "text",
                  "text-secondary", "text-muted", "accent", "accent-surface")
TYPO_ROLES = ("display", "body", "mono")
TYPO_KEYS = ("fontFamily", "fontSize", "fontWeight", "lineHeight", "letterSpacing")

def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return None, "No frontmatter YAML detectado"
    return m.group(1), m.group(2)

def resolve_token(ref, fm):
    # ref like "token(colors.bg-surface)"
    m = re.match(r"token\(([\w.-]+)\)", ref)
    if not m:
        return None, f"Token mal formado: {ref}"
    path = m.group(1).split(".")
    cur = fm
    for p in path:
        if not isinstance(cur, dict) or p not in cur:
            return None, f"Token path no encontrado: {ref}"
        cur = cur[p]
    return cur, None

def validate(path):
    text = open(path).read()
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        return [body]
    errors = []
    try:
        fm = yaml.safe_load(fm_text)
    except Exception as e:
        return [f"YAML inválido: {e}"]
    for k in REQUIRED:
        if k not in fm:
            errors.append(f"Falta clave: {k}")
    colors = fm.get("colors", {})
    for k in COLOR_KEYS_REQ:
        if k not in colors:
            errors.append(f"colors.{k} ausente")
        elif not re.match(r"^#[0-9a-fA-F]{6}$", str(colors[k])):
            errors.append(f"colors.{k} no es hex sRGB válido: {colors[k]}")
    typo = fm.get("typography", {})
    for role in TYPO_ROLES:
        if role not in typo:
            errors.append(f"typography.{role} ausente")
            continue
        for tk in TYPO_KEYS:
            if tk not in typo[role]:
                errors.append(f"typography.{role}.{tk} ausente")
    for cname, cobj in (fm.get("components") or {}).items():
        if not isinstance(cobj, dict):
            continue
        for prop, val in cobj.items():
            if isinstance(val, str) and val.startswith("token("):
                resolved, err = resolve_token(val, fm)
                if err:
                    errors.append(f"components.{cname}.{prop}: {err}")
    return errors

if __name__ == "__main__":
    for path in sys.argv[1:]:
        errs = validate(path)
        if not errs:
            print(f"OK: {path}")
        else:
            print(f"FAIL: {path}")
            for e in errs:
                print(f"  - {e}")
        if errs:
            sys.exit(1)
```

Uso:

```bash
python3 design_md_validator.py adri-style/exports/bold-signal.design.md
```

## 8. Convención de coherencia hex/token en `components:`

**Regla canónica** (aplicada al corregir los 2 exports existentes):

- Si el valor coincide con un token declarado en `colors/rounded/spacing` → usar `token(<path>)`.
- Si el valor es literal único del componente → hex/px directo.
- **No mezclar dentro del mismo objeto** sin razón documentada.

Ejemplo correcto:

```yaml
card:
  background: "token(colors.bg-surface)"   # bg-surface está declarado
  borderColor: "token(colors.border)"
  borderRadius: "token(rounded.base)"
  padding: "token(spacing.m)"
```

Ejemplo incorrecto (corregir):

```yaml
card:
  background: "#0e0e0e"                    # duplica colors.bg-surface = "#0e0e0e"
  borderColor: "token(colors.border)"      # inconsistente
```

## 9. Versionado

- Actual: `version: "alpha"`.
- Bump a `"1.0"` cuando: (a) Stitch publica spec estable, (b) Adri valida 5+ presets exportados, (c) ninguna herramienta externa rompe con la convención.
- Migraciones se documentan aquí, sección `## Versions`.

## 10. No reimportar automáticamente

Cláusula explícita: **`adri-style` no consume `.design.md` para regenerar sus presets internos**. Los `.design.md` son output; la fuente sigue siendo `references/style-presets.md` y `references/presets.json`. Si el usuario quiere actualizar un preset desde una edición externa, lo hace manualmente.
