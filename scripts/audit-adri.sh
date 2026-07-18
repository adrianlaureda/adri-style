#!/usr/bin/env bash
# audit-adri.sh — Linter pre-entrega para outputs de Adri.
# Combina Impeccable detect + filtros de excepciones locales con verificación de coherencia.
#
# Uso: audit-adri.sh <ruta-html|url>
#
# Filtros locales aplicados (NO los marca como anti-patterns):
#   - side-tab + border-left con var(--accent|yellow|red|green|info|success|warning|danger)
#     → semáforo educativo legítimo (memoria visual de calificación/estado).
#   - overused-font cuando el HTML declara <html data-preset="NN-name"> Y carga
#     TODAS las fuentes canónicas que ese preset declara (display + body).
#     Si el preset declarado pide Satoshi+Inter pero solo se carga Inter, el
#     filtro NO aplica (preset declarado es ai-slop disfrazado).
#
# v5.5: filtro 2 verifica coherencia preset↔fuentes (catálogo bash hardcoded).
# v5.6: catálogo se lee de `references/presets.json` (fuente programática única).
# Eliminada la duplicación bash↔markdown. La fuente humana sigue siendo
# `references/style-presets.md § Audit v5.4`; el JSON es mirror programático.
#
# Bloquea (exit 1) si encuentra issues NO filtrables. WARN (exit 0) si solo filtrables.

set -euo pipefail

readonly IMPECCABLE_REPO="${IMPECCABLE_REPO:-$HOME/Proyectos/Claude/config/impeccable-integration/sandbox/impeccable}"
readonly NODE="${NODE:-/opt/homebrew/bin/node}"
readonly JQ="${JQ:-/opt/homebrew/bin/jq}"
readonly PRESETS_JSON="${PRESETS_JSON:-$(/usr/bin/dirname "$0")/../references/presets.json}"

usage() {
    echo "Uso: $0 <ruta-html|url>"
    echo "Ejemplo: $0 dist/index.html"
    echo "Ejemplo: $0 https://midominio.com/page"
    exit 64
}

require_tool() {
    [[ -x "$1" ]] || { echo "FATAL: $1 no encontrado"; exit 1; }
}

# Devuelve las fuentes canónicas del preset NN-name leídas de presets.json.
# Cada fuente en una línea (TSV-friendly). Vacío si preset desconocido o JSON ausente.
# Si el preset es single-font, devuelve solo 1 línea (no duplica display/body).
preset_canonical_fonts() {
    local preset_id="$1"
    [[ -f "$PRESETS_JSON" ]] || return 0
    [[ -x "$JQ" ]] || return 0
    "$JQ" -r --arg id "$preset_id" '
        .presets[]
        | select(.id==$id)
        | if .fonts.single_font then [.fonts.display]
          else [.fonts.display, .fonts.body]
          end
        | .[]
    ' "$PRESETS_JSON" 2>/dev/null
}

# Verifica que el HTML carga una fuente concreta (vía Google/Fontshare URL, font-family,
# o vía override externo `adri-overrides.css` que se sabe que carga Satoshi + General Sans).
# Args: $1 = ruta archivo, $2 = nombre fuente (puede tener espacios)
html_loads_font() {
    local file="$1"
    local font="$2"
    # Buscar en URLs de Google Fonts (family=Foo+Bar) o Fontshare (f[]=foo)
    local font_url="${font// /+}"
    local font_url_lc
    font_url_lc="$(echo "$font" | /usr/bin/tr '[:upper:]' '[:lower:]' | /usr/bin/tr ' ' '-')"
    if /usr/bin/grep -qiE "(family=|f\[\]=)[^\"' ]*${font_url}" "$file" 2>/dev/null; then return 0; fi
    if /usr/bin/grep -qE "f\[\]=${font_url_lc}" "$file" 2>/dev/null; then return 0; fi
    # O bien mencionada en una declaración font-family (acepta postfix " Variable" para
    # variantes variable fonts como "Fraunces Variable", "Inter Variable", etc.).
    if /usr/bin/grep -qE "font-family[[:space:]]*:[^;]*['\"]${font}( Variable)?['\"]" "$file" 2>/dev/null; then return 0; fi
    # O bien el HTML enlaza la capa override externa adri-overrides.css que se sabe que
    # carga la pareja canónica Bold Signal (Satoshi + General Sans + Inter como fallback).
    # Esto permite que outputs legacy regenerados con la capa override pasen el chequeo.
    if [[ "$font" == "Satoshi" || "$font" == "Inter" || "$font" == "General Sans" ]]; then
        if /usr/bin/grep -qE 'href="[^"]*adri-overrides\.css' "$file" 2>/dev/null; then return 0; fi
    fi
    return 1
}

# Verifica coherencia preset↔fuentes. Devuelve 0 si todas las fuentes canónicas
# del preset están cargadas en el HTML; 1 si falta alguna o si preset desconocido.
preset_fonts_coherent() {
    local file="$1"
    local preset="$2"
    local fonts
    fonts="$(preset_canonical_fonts "$preset")"
    [[ -z "$fonts" ]] && return 1  # preset desconocido o JSON ausente → no filtrar

    while IFS= read -r f; do
        [[ -z "$f" ]] && continue
        if ! html_loads_font "$file" "$f"; then
            return 1
        fi
    done <<< "$fonts"
    return 0
}

main() {
    [[ $# -eq 1 ]] || usage
    local target="$1"

    require_tool "$NODE"
    [[ -d "$IMPECCABLE_REPO/cli" ]] || {
        echo "FATAL: Impeccable no clonado en $IMPECCABLE_REPO"
        echo "Ejecuta: gh repo clone pbakaus/impeccable $IMPECCABLE_REPO"
        exit 1
    }

    # Si es URL, descargar a tmp con curl
    local file="$target"
    local tmp=""
    if [[ "$target" =~ ^https?:// ]]; then
        tmp="$(/usr/bin/mktemp /tmp/audit-adri.XXXXXX.html)"
        trap "rm -f '$tmp'" EXIT
        /usr/bin/curl -fsSL "$target" -o "$tmp" || {
            echo "FATAL: no pude descargar $target"
            exit 1
        }
        file="$tmp"
    fi

    [[ -f "$file" ]] || { echo "FATAL: $file no existe"; exit 1; }

    # Detectar preset declarado y verificar coherencia con sus fuentes canónicas.
    local declared_preset=""
    local preset_coherent=1  # 1 = NO coherente / no aplicable
    if /usr/bin/grep -qE 'data-preset="[0-9]{2}-[a-z-]+"' "$file" 2>/dev/null; then
        declared_preset="$(/usr/bin/grep -oE 'data-preset="[0-9]{2}-[a-z-]+"' "$file" | /usr/bin/head -1 | /usr/bin/sed 's/data-preset="//; s/"//')"
        if preset_fonts_coherent "$file" "$declared_preset"; then
            preset_coherent=0
        fi
    fi

    # Ejecutar Impeccable detect
    local raw_output
    raw_output="$("$NODE" "$IMPECCABLE_REPO/cli/bin/cli.js" detect "$file" 2>&1 || true)"

    if echo "$raw_output" | /usr/bin/grep -q "0 anti-patterns found\|No anti-patterns found"; then
        echo "OK: $target sin anti-patterns"
        exit 0
    fi

    local total=0
    local filtered=0
    local critical=0
    local report=""

    while IFS= read -r line; do
        if [[ "$line" =~ ^\ \ line\ ([0-9]+):\ \[([a-z-]+)\]\ (.*)$ ]]; then
            local lineno="${BASH_REMATCH[1]}"
            local tag="${BASH_REMATCH[2]}"
            local snippet="${BASH_REMATCH[3]}"
            total=$((total + 1))

            # Filtro 1: side-tab + border-left semáforo educativo
            if [[ "$tag" == "side-tab" && "$snippet" =~ var\(--(accent|yellow|red|green|info|success|warning|danger) ]]; then
                filtered=$((filtered + 1))
                report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (semáforo educativo)\n"
                continue
            fi

            # Filtro 1b v5.8.1: side-tab con vars de texto neutro o tokens estructurales.
            # --ink, --text, --text-primary, --border, --fg, --link, --color-link son base
            # del documento o tokens funcionales (link), no decoración cromática.
            if [[ "$tag" == "side-tab" && "$snippet" =~ var\(--(ink|text|text-primary|text-secondary|text-muted|fg|foreground|border|line|link|color-link) ]]; then
                filtered=$((filtered + 1))
                report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (color base/neutro o token funcional, no decoración cromática)\n"
                continue
            fi

            # Filtro 1d v5.8.2: side-tab/border-accent con HEX hardcoded cuando hay 3+ colores
            # distintos en el archivo (heurística codificación de categorías). Útil para outputs
            # legacy con paleta inline antes de adoptar var() del preset.
            if [[ "$tag" == "side-tab" && "$snippet" =~ border-(left|right|top|bottom):[[:space:]]*[0-9]+px[[:space:]]+solid[[:space:]]+\#[0-9a-fA-F]{3,8} ]]; then
                # Contar colores únicos border-* en el archivo (heurística "codifica categorías")
                local color_count
                color_count="$(/usr/bin/grep -oE 'border-(left|right|top|bottom):[[:space:]]*[0-9]+px[[:space:]]+solid[[:space:]]+#[0-9a-fA-F]{3,8}' "$file" 2>/dev/null | /usr/bin/sort -u | wc -l | /usr/bin/tr -d ' ')"
                if [[ "${color_count:-0}" -ge 3 ]]; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (≥3 colores distintos = codifica categorías)\n"
                    continue
                fi
            fi

            # Filtro 1c v5.8.1: border-accent-on-rounded con var() del preset.
            # Cuando data-preset declarado Y el border usa una var() (cualquiera del preset),
            # se considera color funcional (codifica dato/categoría) — no decoración inventada.
            if [[ "$tag" == "border-accent-on-rounded" ]]; then
                local raw_line
                raw_line="$(/usr/bin/sed -n "${lineno}p" "$file" 2>/dev/null)"
                if [[ "$raw_line" =~ var\(-- ]] && [[ -n "$declared_preset" ]]; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (var() del preset codifica dato)\n"
                    continue
                fi
                # Aún sin preset declarado, aceptar vars semáforo bien conocidas
                if [[ "$raw_line" =~ var\(--(accent|yellow|red|green|info|success|warning|danger|ink|text|text-primary|text-secondary|text-muted) ]]; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (var semáforo/texto base)\n"
                    continue
                fi
            fi

            # Filtro 5 v5.8.1: bounce-easing en outputs marcados como minijuego o como
            # definición de design system token (:root con --ease-* var). Bounce es UX
            # intencional cuando el output es interactivo o cuando es token de paleta de
            # animaciones (no se aplica directamente, queda disponible en var()).
            if [[ "$tag" == "bounce-easing" ]]; then
                if [[ "$file" == *"adri-react/public/"* ]] \
                   || /usr/bin/grep -qE 'data-(output="game"|allow-bounce)' "$file" 2>/dev/null; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (minijuego — bounce es UX intencional)\n"
                    continue
                fi
                # Token de design system: si la línea define una variable CSS dentro de :root
                local raw_line
                raw_line="$(/usr/bin/sed -n "${lineno}p" "$file" 2>/dev/null)"
                if [[ "$raw_line" =~ --ease ]] || [[ "$raw_line" =~ --bounce ]] || [[ "$raw_line" =~ --overshoot ]]; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (token de design system, no aplicación directa)\n"
                    continue
                fi
                # Animación legítima de UI: scroll-indicator, attention-pulse, etc.
                local context_start=$((lineno > 8 ? lineno - 8 : 1))
                if /usr/bin/sed -n "${context_start},${lineno}p" "$file" 2>/dev/null | \
                   /usr/bin/grep -qE '\.(scroll-indicator|attention-|pulse-|notify-|bounce-)' ; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (UI affordance — scroll/attention/pulse)\n"
                    continue
                fi
            fi

            # Filtro 6 v5.8.1: layout-transition: height/width fuera de progress bar dentro de
            # minijuegos legacy donde el comportamiento (revelar pista, expandir card) es
            # intencional. Solo si data-preset declarado Y ruta de minijuego.
            if [[ "$tag" == "layout-transition" ]]; then
                if [[ "$file" == *"adri-react/public/"* ]] && [[ -n "$declared_preset" ]]; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (minijuego con preset — transición intencional)\n"
                    continue
                fi
            fi

            # Filtro 2 v5.5: overused-font cuando el preset declarado existe Y
            # carga sus dos fuentes canónicas. Si declara preset pero no carga
            # las fuentes que el preset documenta, el filtro NO aplica.
            if [[ "$tag" == "overused-font" && -n "$declared_preset" ]]; then
                if (( preset_coherent == 0 )); then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (preset $declared_preset coherente)\n"
                    continue
                else
                    critical=$((critical + 1))
                    local expected
                    expected="$(preset_canonical_fonts "$declared_preset" | /usr/bin/tr '\n' ',' | /usr/bin/sed 's/,$//' | /usr/bin/sed 's/,/, /g')"
                    report+="  line $lineno: [$tag] $snippet  ✗ CRÍTICO (preset $declared_preset declarado pero fuentes incoherentes; esperado: $expected)\n"
                    continue
                fi
            fi

            # Filtro 3 v5.8: single-font cuando hay capa override externa (adri-overrides.css)
            # Y data-preset coherente. Impeccable analiza solo HTML+CSS inline; no sigue el <link>
            # externo que sí carga la pareja display+body completa. Este patrón es legítimo en
            # outputs legacy regenerados con override CSS añadido (ver adri-react/public).
            if [[ "$tag" == "single-font" && -n "$declared_preset" ]] && (( preset_coherent == 0 )); then
                if /usr/bin/grep -qE 'href="[^"]*adri-overrides\.css' "$file" 2>/dev/null; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (override externo adri-overrides.css gestiona fuentes)\n"
                    continue
                fi
            fi

            # Filtro 4 v5.8.1: layout-transition (transition: width) dentro de progress/timer bars.
            # Una progress bar codifica datos (tiempo, score, %) — el width animado ES la UI.
            # Heurística: leer 8 líneas previas a la del issue y buscar selectores típicos de barra.
            if [[ "$tag" == "layout-transition" && "$snippet" =~ transition[[:space:]]*:[[:space:]]*width ]]; then
                local context_start=$((lineno > 8 ? lineno - 8 : 1))
                if /usr/bin/sed -n "${context_start},${lineno}p" "$file" 2>/dev/null | \
                   /usr/bin/grep -qE '\.(timer-bar|progress-bar|progress-fill|score-bar|fill-bar|aval-bar|loading-bar|bar-fill|goal-bar|goal-bar-fill|level-progress|level-progress-fill|stat-bar|kpi-bar)' ; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (progress/timer bar codifica datos)\n"
                    continue
                fi
            fi

            critical=$((critical + 1))
            report+="  line $lineno: [$tag] $snippet  ✗ CRÍTICO\n"
        fi
    done <<< "$raw_output"

    echo "audit-adri report for: $target"
    if [[ -n "$declared_preset" ]]; then
        if (( preset_coherent == 0 )); then
            echo "Preset declarado: $declared_preset · fuentes coherentes ✓"
        else
            local expected
            expected="$(preset_canonical_fonts "$declared_preset" | /usr/bin/tr '\n' ',' | /usr/bin/sed 's/,$//' | /usr/bin/sed 's/,/, /g')"
            if [[ -z "$expected" ]]; then
                echo "Preset declarado: $declared_preset · DESCONOCIDO en references/presets.json"
            else
                echo "Preset declarado: $declared_preset · INCOHERENTE — fuentes canónicas esperadas: $expected"
            fi
        fi
    fi
    echo "Total issues: $total | Críticos: $critical | Filtrados (excepción educativa): $filtered"
    echo ""
    printf "%b" "$report"
    echo ""

    if (( critical > 0 )); then
        echo "RESULTADO: FAIL ($critical issues críticos pendientes)"
        exit 1
    fi
    echo "RESULTADO: OK con WARNINGS ($filtered filtrados como excepción educativa)"
    exit 0
}

main "$@"
