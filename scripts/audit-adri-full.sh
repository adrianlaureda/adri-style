#!/usr/bin/env bash
# audit-adri-full.sh — Quality-check unificado para outputs adri (P4 #2).
#
# Combina:
#   1. audit-adri.sh        — Impeccable + filtros adri (anti-cajas, preset coherente).
#   2. html-validate        — HTML estructural válido (npx, sin instalación).
#   3. pa11y                — Accesibilidad WCAG 2.1 AA (npx, sin instalación).
#   4. broken-link-checker  — Enlaces internos+externos (opcional, --links).
#
# Uso: audit-adri-full.sh <ruta-html> [--links] [--quick]
#   --links  añade verificación de enlaces (lento, ~30s por output).
#   --quick  salta html-validate y pa11y (solo Impeccable + filtros adri).
#
# Exit code:
#   0 = todo OK (warnings filtrados ok)
#   1 = al menos una categoría con críticos
#   64 = uso incorrecto

set -euo pipefail

readonly SCRIPT_DIR="$(/usr/bin/dirname "$0")"
readonly AUDIT_BASIC="$SCRIPT_DIR/audit-adri.sh"
readonly NPX="${NPX:-/Users/adrianlauredaleon/.nvm/versions/node/v24.14.0/bin/npx}"

usage() {
    echo "Uso: $0 <ruta-html> [--links] [--quick]"
    echo "  --links  añade verificación de enlaces (lento)"
    echo "  --quick  solo audit-adri (sin html-validate ni pa11y)"
    exit 64
}

[[ $# -lt 1 ]] && usage
target="$1"
shift || true

WITH_LINKS=0
QUICK=0
for arg in "$@"; do
    case "$arg" in
        --links) WITH_LINKS=1 ;;
        --quick) QUICK=1 ;;
        *) echo "Argumento desconocido: $arg"; usage ;;
    esac
done

[[ -f "$target" ]] || [[ "$target" =~ ^https?:// ]] || { echo "FATAL: $target no existe"; exit 1; }

# Acumuladores
declare -i fail_basic=0 fail_html=0 fail_a11y=0 fail_links=0
declare -a section_reports=()

separator() { printf '\n%s\n' "============================================================"; }

# ============================================================
# 1. Basic: audit-adri.sh (Impeccable + filtros adri)
# ============================================================
separator
echo "1/$((QUICK ? 1 : (WITH_LINKS ? 4 : 3))): audit-adri (Impeccable + filtros adri)"
separator
if "$AUDIT_BASIC" "$target"; then
    section_reports+=("✓ adri-audit OK")
else
    fail_basic=1
    section_reports+=("✗ adri-audit FAIL")
fi

if (( QUICK )); then
    separator
    echo "MODO QUICK — saltando html-validate, pa11y y enlaces"
    printf '%s\n' "${section_reports[@]}"
    exit $(( fail_basic ))
fi

# ============================================================
# 2. HTML válido: html-validate via npx (descarga primera vez ~5s)
# ============================================================
separator
echo "2/$((WITH_LINKS ? 4 : 3)): html-validate (estructura HTML válida)"
separator
if "$NPX" --yes html-validate@latest "$target" 2>&1 | /usr/bin/tail -20; then
    section_reports+=("✓ html-validate OK")
else
    fail_html=1
    section_reports+=("✗ html-validate FAIL")
fi

# ============================================================
# 3. A11y: pa11y WCAG 2.1 AA (npx)
# ============================================================
separator
echo "3/$((WITH_LINKS ? 4 : 3)): pa11y (accesibilidad WCAG 2.1 AA)"
separator
# pa11y necesita URL absoluta o file://
pa11y_target="$target"
if [[ ! "$target" =~ ^https?:// ]]; then
    pa11y_target="file://$(/usr/bin/realpath "$target" 2>/dev/null || echo "$target")"
fi
if "$NPX" --yes pa11y@latest --standard WCAG2AA "$pa11y_target" 2>&1 | /usr/bin/tail -30; then
    section_reports+=("✓ pa11y OK")
else
    fail_a11y=1
    section_reports+=("✗ pa11y FAIL (algunos issues toleran ajuste — revisar manualmente)")
fi

# ============================================================
# 4. Enlaces (opcional --links)
# ============================================================
if (( WITH_LINKS )); then
    separator
    echo "4/4: broken-link-checker"
    separator
    if [[ "$target" =~ ^https?:// ]]; then
        if "$NPX" --yes broken-link-checker@latest "$target" --recursive=false --get 2>&1 | /usr/bin/tail -10; then
            section_reports+=("✓ links OK")
        else
            fail_links=1
            section_reports+=("✗ links FAIL")
        fi
    else
        section_reports+=("⊘ links (skip — broken-link-checker requiere URL servida HTTP)")
    fi
fi

# ============================================================
# Resumen final
# ============================================================
separator
echo "RESUMEN audit-adri-full · $target"
separator
printf '%s\n' "${section_reports[@]}"

total_fail=$(( fail_basic + fail_html + fail_a11y + fail_links ))
if (( total_fail > 0 )); then
    echo ""
    echo "VEREDICTO: FAIL ($total_fail categorías con críticos)"
    exit 1
fi
echo ""
echo "VEREDICTO: OK"
exit 0
