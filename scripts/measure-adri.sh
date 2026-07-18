#!/usr/bin/env bash
# measure-adri.sh — Medición diaria de outputs adri (P4 #3, fase 30 días).
#
# Escanea directorios canónicos de outputs HTML, ejecuta audit-adri.sh modo
# rápido sobre cada uno, y registra resultado en JSONL en
# ~/Library/Application Support/adri-style-metrics/YYYY-MM-DD.jsonl
#
# Datos por output:
#   - ruta relativa
#   - preset declarado (data-preset, si existe)
#   - total issues, críticos, filtrados
#   - exit code audit (0=OK, 1=FAIL)
#   - hash del contenido (para detectar cambios entre días)
#   - tamaño líneas
#
# Uso: measure-adri.sh [--report]
#   sin args  → escanea + escribe JSONL del día.
#   --report  → genera report markdown de últimos 30 días en stdout.

set -euo pipefail

readonly SCRIPT_DIR="$(/usr/bin/dirname "$0")"
readonly AUDIT_BASIC="$SCRIPT_DIR/audit-adri.sh"
readonly METRICS_DIR="$HOME/Library/Application Support/adri-style-metrics"
readonly TODAY="$(/bin/date +%Y-%m-%d)"
readonly OUT="$METRICS_DIR/$TODAY.jsonl"

# Directorios escaneados (HTML adri-style outputs)
readonly SCAN_DIRS=(
    "$HOME/Proyectos/Claude/apps/adri-react/public"
    "$HOME/Proyectos/Claude/educacion"
    "$HOME/Proyectos/Claude/personal"
)

mkdir -p "$METRICS_DIR"

# ============================================================
# Modo --report
# ============================================================
if [[ "${1:-}" == "--report" ]]; then
    /usr/bin/find "$METRICS_DIR" -type f -name "*.jsonl" -mtime -30 | /usr/bin/sort | /usr/bin/tail -30 > /tmp/adri-jsonl-list.txt
    if [[ ! -s /tmp/adri-jsonl-list.txt ]]; then
        echo "(sin datos en últimos 30 días)"
        exit 0
    fi
    echo "# adri-style metrics — últimos 30 días"
    echo ""
    echo "Generado: $(/bin/date +%Y-%m-%d) · directorios escaneados: ${#SCAN_DIRS[@]}"
    echo ""
    echo "## Tendencia diaria (% outputs sin críticos)"
    echo ""
    echo "| Fecha | Total HTMLs | Sin críticos | % OK | Top anti-pattern |"
    echo "|---|---|---|---|---|"
    while IFS= read -r jsonl; do
        date_str="$(/usr/bin/basename "$jsonl" .jsonl)"
        total=$(wc -l < "$jsonl" | /usr/bin/tr -d ' ')
        ok=$(/usr/bin/awk -F'"critical":' '{if ($2 ~ /^0/) print}' "$jsonl" | wc -l | /usr/bin/tr -d ' ')
        if (( total > 0 )); then
            pct=$(( ok * 100 / total ))
            top=$(/usr/bin/awk -F'"top_tag":"' '{if ($2) print $2}' "$jsonl" | /usr/bin/sed 's/".*//' | /usr/bin/sort | /usr/bin/uniq -c | /usr/bin/sort -rn | /usr/bin/head -1 | /usr/bin/awk '{print $2}')
            printf "| %s | %d | %d | %d%% | %s |\n" "$date_str" "$total" "$ok" "$pct" "${top:-—}"
        fi
    done < /tmp/adri-jsonl-list.txt
    rm -f /tmp/adri-jsonl-list.txt
    exit 0
fi

# ============================================================
# Modo escaneo (default)
# ============================================================
> "$OUT"
declare -i scanned=0 ok=0 fail=0

for dir in "${SCAN_DIRS[@]}"; do
    [[ -d "$dir" ]] || continue
    while IFS= read -r html; do
        # Ignorar archivos test, baked, backups
        [[ "$html" =~ (test-|baked|\.bak\.|node_modules) ]] && continue
        ((scanned++)) || true
        rel="${html#$HOME/}"
        # Ejecutar audit y capturar
        if audit_out="$("$AUDIT_BASIC" "$html" 2>&1)"; then
            exit_code=0
            ((ok++)) || true
        else
            exit_code=1
            ((fail++)) || true
        fi
        total=$(echo "$audit_out" | /usr/bin/grep -oE 'Total issues: [0-9]+' | /usr/bin/awk '{print $3}' || echo 0)
        critical=$(echo "$audit_out" | /usr/bin/grep -oE 'Críticos: [0-9]+' | /usr/bin/awk '{print $2}' || echo 0)
        filtered=$(echo "$audit_out" | /usr/bin/grep -oE 'Filtrados \(excepción educativa\): [0-9]+' | /usr/bin/awk '{print $4}' || echo 0)
        preset=$(echo "$audit_out" | /usr/bin/grep -oE 'Preset declarado: [0-9]{2}-[a-z-]+' | /usr/bin/awk '{print $3}' || echo "")
        # Top anti-pattern (más frecuente)
        top_tag=$(echo "$audit_out" | /usr/bin/grep -oE '\[[a-z-]+\]' | /usr/bin/sort | /usr/bin/uniq -c | /usr/bin/sort -rn | /usr/bin/head -1 | /usr/bin/awk '{print $2}' | /usr/bin/tr -d '[]' || echo "")
        size=$(wc -l < "$html" | /usr/bin/tr -d ' ')
        hash=$(/sbin/md5 -q "$html")
        # JSONL line
        printf '{"date":"%s","path":"%s","preset":"%s","total":%s,"critical":%s,"filtered":%s,"top_tag":"%s","size":%s,"hash":"%s","exit":%s}\n' \
            "$TODAY" "$rel" "${preset:-}" "${total:-0}" "${critical:-0}" "${filtered:-0}" "${top_tag:-}" "$size" "$hash" "$exit_code" >> "$OUT"
    done < <(/usr/bin/find "$dir" -type f -name "index.html" 2>/dev/null)
done

echo "Escaneados: $scanned · OK (0 críticos): $ok · FAIL: $fail"
echo "Resultado: $OUT"
