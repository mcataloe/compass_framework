#!/usr/bin/env bash
set -euo pipefail

echo "Remaining STRIDE references:"
grep -RIn "STRIDE\|stride" . --exclude-dir=.git --exclude='*.zip' || true

echo
echo "Expected: legacy redirect stubs, historical changelog references, and migration docs may still mention STRIDE."
