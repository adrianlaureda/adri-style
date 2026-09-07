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
# v5.6: catálogo se lee de `references/presets.json`.
# v5.8/PRO-211: el JSON es el contrato estructurado canónico y la validación
# fail-closed ocurre antes de cualquier herramienta externa.
#
# Exit: 0 conforme, 1 incumplimiento del output, 2 fallo de infraestructura.

set -euo pipefail

readonly IMPECCABLE_REPO="${IMPECCABLE_REPO:-$HOME/Proyectos/Claude/config/impeccable-integration/sandbox/impeccable}"
readonly NODE="${NODE:-$(command -v node || true)}"
readonly PYTHON="${PYTHON:-$(command -v python3 || true)}"
readonly PRESETS_JSON="${PRESETS_JSON:-$(/usr/bin/dirname "$0")/../references/presets.json}"
readonly CONTRACT_VALIDATOR="${CONTRACT_VALIDATOR:-$(/usr/bin/dirname "$0")/validate_contract.py}"

usage() {
    echo "Uso: $0 <ruta-html|url>"
    echo "Ejemplo: $0 dist/index.html"
    echo "Ejemplo: $0 https://midominio.com/page"
    exit 64
}

require_tool() {
    [[ -n "$1" && -x "$1" ]] || {
        echo "INFRASTRUCTURE_ERROR: herramienta no encontrada"
        exit 2
    }
}

main() {
    [[ $# -eq 1 ]] || usage
    local target="$1"

    # Si es URL, descargar a tmp con curl
    local file="$target"
    local tmp=""
    if [[ "$target" =~ ^https?:// ]]; then
        tmp="$(/usr/bin/mktemp /tmp/audit-adri.XXXXXX.html)"
        trap "rm -f '$tmp'" EXIT
        /usr/bin/curl --connect-timeout 10 --max-time 30 -fsSL "$target" -o "$tmp" || {
            echo "INFRASTRUCTURE_ERROR: no pude descargar $target"
            exit 2
        }
        file="$tmp"
    fi

    [[ -f "$file" ]] || { echo "FATAL: $file no existe"; exit 1; }

    # El contrato local es autónomo y se valida antes de herramientas externas.
    require_tool "$PYTHON"
    local contract_output contract_rc
    set +e
    contract_output="$("$PYTHON" "$CONTRACT_VALIDATOR" "$file" --catalog "$PRESETS_JSON" --json 2>&1)"
    contract_rc=$?
    set -e
    printf '%s\n' "$contract_output"
    if (( contract_rc != 0 )); then
        exit "$contract_rc"
    fi

    require_tool "$NODE"
    [[ -d "$IMPECCABLE_REPO/cli" ]] || {
        echo "INFRASTRUCTURE_ERROR: Impeccable no disponible en $IMPECCABLE_REPO"
        exit 2
    }

    # Un único validador decide preset y fuentes, también para CSS externos.
    local declared_preset
    declared_preset="$(printf '%s' "$contract_output" | "$PYTHON" -c 'import json,sys; print(", ".join(json.load(sys.stdin)["preset_ids"]))')"

    # Ejecutar Impeccable detect
    local raw_output impeccable_rc
    set +e
    raw_output="$("$NODE" "$IMPECCABLE_REPO/cli/bin/cli.js" detect "$file" 2>&1)"
    impeccable_rc=$?
    set -e
    # Impeccable devuelve 2 cuando encuentra patrones; validar también el formato.
    if (( impeccable_rc != 0 && impeccable_rc != 2 )); then
        echo "INFRASTRUCTURE_ERROR: Impeccable terminó con exit $impeccable_rc"
        printf '%s\n' "$raw_output"
        exit 2
    fi

    # El CLI instalado no emite texto cuando termina sin hallazgos.
    if (( impeccable_rc == 0 )) && [[ -z "$raw_output" ]]; then
        echo "OK: $target sin anti-patterns"
        exit 0
    fi
    if (( impeccable_rc == 0 )) && echo "$raw_output" | /usr/bin/grep -qE "^[[:space:]]*(0 anti-patterns found|No anti-patterns found)[.![:space:]]*$"; then
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

            # Border redondeado: solo se filtran tokens semánticos explícitos.
            if [[ "$tag" == "border-accent-on-rounded" ]]; then
                local raw_line
                raw_line="$(/usr/bin/sed -n "${lineno}p" "$file" 2>/dev/null)"
                if [[ "$raw_line" =~ var\(--(accent|yellow|red|green|info|success|warning|danger|ink|text|text-primary|text-secondary|text-muted) ]]; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (var semáforo/texto base)\n"
                    continue
                fi
            fi

            # Bounce solo se filtra con una declaración explícita del output.
            if [[ "$tag" == "bounce-easing" ]]; then
                if /usr/bin/grep -qE 'data-(output="game"|allow-bounce)' "$file" 2>/dev/null; then
                    filtered=$((filtered + 1))
                    report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (minijuego — bounce es UX intencional)\n"
                    continue
                fi
            fi

            # El contrato ya comprobó las cargas; no repetir heurísticas bash.
            if [[ "$tag" == "overused-font" || "$tag" == "single-font" ]]; then
                filtered=$((filtered + 1))
                report+="  line $lineno: [$tag] $snippet  ✓ FILTRADO (contrato de fuentes $declared_preset validado)\n"
                continue
            fi

            critical=$((critical + 1))
            report+="  line $lineno: [$tag] $snippet  ✗ CRÍTICO\n"
        fi
    done <<< "$raw_output"

    echo "audit-adri report for: $target"
    if (( total == 0 )); then
        echo "INFRASTRUCTURE_ERROR: respuesta de Impeccable no reconocida"
        exit 2
    fi
    echo "Preset declarado: $declared_preset · fuentes coherentes"
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
