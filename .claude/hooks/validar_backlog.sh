#!/usr/bin/env bash
# Hook Stop de solvershub-docs: valida el plan cuando el agente intenta cerrar.
# Si hay errores de frontmatter, enlaces, anclas o dependencias, los devuelve
# como feedback (exit 2) para que el agente no cierre con el plan roto.
set -euo pipefail

root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "$root"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 no está disponible; se omite la validación del plan." >&2
  exit 0
fi

if ! python3 -c "import yaml" >/dev/null 2>&1; then
  echo "Falta PyYAML (pip install pyyaml); se omite la validación del plan." >&2
  exit 0
fi

salida="$(python3 herramientas/regenerar.py --check 2>&1)" || {
  echo "El plan tiene inconsistencias. Corrige antes de cerrar:" >&2
  echo "$salida" >&2
  exit 2
}

echo "Plan OK · $salida"
