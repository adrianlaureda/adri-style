#!/bin/bash
# Setup de skills educativos para Cora (OpenClaw) en MBP 2015
# Ejecutar desde el MBP 2015 o via SSH desde el Mac principal
#
# Uso:
#   ssh adrianlauredaleon@Adrians-MacBook-Pro.local 'bash -s' < setup-cora.sh
#   o directamente en el MBP 2015:
#   bash setup-cora.sh

set -euo pipefail

CLAWD="$HOME/clawd"
SKILLS_DIR="$CLAWD/skills"
OUTPUT_DIR="$CLAWD/output"
MAC_PRINCIPAL="adrianlauredaleon@mbp-adri.local"

echo "=== Setup de skills educativos para Cora ==="

# 1. Crear estructura de directorios
echo "[1/5] Creando directorios..."
mkdir -p "$SKILLS_DIR"
mkdir -p "$OUTPUT_DIR"/{lecciones,presentaciones,cuestionarios,h5p,sesiones,informes,graficos,ilustraciones}

# 2. Clonar adri-style desde GitHub
echo "[2/5] Clonando adri-style..."
if [ -d "$SKILLS_DIR/adri-style" ]; then
    echo "  adri-style ya existe, actualizando..."
    cd "$SKILLS_DIR/adri-style" && git pull
else
    git clone git@github.com:adrianlaureda/adri-style.git "$SKILLS_DIR/adri-style"
fi

# 3. Copiar skills desde el Mac principal via rsync
echo "[3/5] Sincronizando skills desde Mac principal ($MAC_PRINCIPAL)..."

SKILLS_TO_SYNC=(
    "contenido-a-leccion"
    "presentacion-html"
    "crear-cuestionario"
    "sesion-interactiva"
    "cmd-crear-h5p"
    "quality-check"
    "obsidian-markdown"
    "informe-alumnos"
    "agregador-informes"
    "dataviz-educativa"
    "excalidraw-illustrations"
)

for skill in "${SKILLS_TO_SYNC[@]}"; do
    echo "  Sincronizando $skill..."
    rsync -av --delete \
        "$MAC_PRINCIPAL:~/.dotfiles/ai/skills/$skill/" \
        "$SKILLS_DIR/$skill/" \
        2>/dev/null || echo "  WARN: No se pudo sincronizar $skill (verificar SSH)"
done

# writing-clearly tiene nombre diferente en origen
echo "  Sincronizando writing-clearly..."
rsync -av --delete \
    "$MAC_PRINCIPAL:~/.dotfiles/ai/skills/writing-clearly-and-concisely/" \
    "$SKILLS_DIR/writing-clearly/" \
    2>/dev/null || echo "  WARN: No se pudo sincronizar writing-clearly (verificar SSH)"

# 4. Instalar dependencias Python
echo "[4/5] Instalando dependencias Python..."
pip3 install --user matplotlib python-pptx 2>/dev/null || echo "  WARN: pip3 install falló, verificar manualmente"

# Setup del entorno H5P
if [ -f "$SKILLS_DIR/cmd-crear-h5p/scripts/setup_environment.py" ]; then
    echo "  Configurando entorno H5P..."
    cd "$SKILLS_DIR/cmd-crear-h5p/scripts" && python3 setup_environment.py
fi

# 5. Verificar GEMINI_API_KEY
echo "[5/5] Verificando entorno..."
if [ -z "${GEMINI_API_KEY:-}" ]; then
    echo "  WARN: GEMINI_API_KEY no está configurada (necesaria para excalidraw-illustrations)"
    echo "  Añádela a ~/.openclaw/gateway-env o al entorno de OpenClaw"
else
    echo "  GEMINI_API_KEY: OK"
fi

# Resumen
echo ""
echo "=== Setup completado ==="
echo "Skills instalados en: $SKILLS_DIR"
echo "Output se guardará en: $OUTPUT_DIR"
echo ""
echo "Skills disponibles:"
ls -1 "$SKILLS_DIR" | while read -r d; do
    if [ -f "$SKILLS_DIR/$d/SKILL.md" ]; then
        echo "  OK  $d"
    elif [ -d "$SKILLS_DIR/$d" ]; then
        echo "  --  $d (sin SKILL.md)"
    fi
done
echo ""
echo "Siguiente paso: añadir las instrucciones al CLAUDE.md de Cora"
echo "  Ver: $SKILLS_DIR/adri-style/OPENCLAW.md"
