#!/bin/bash
echo "🛡️ DZIVISA PRODUCTION DEPLOYMENT & TESTING SUITE"
echo "-----------------------------------------------"

# 1. Check for Regex Loop Bugs
echo -n "🔍 Auditing Core Engine short-circuits... "
RETURNS=$(grep -c "return \[x\]" engine.js)
if [ "$RETURNS" -ne 2 ]; then
    echo "❌ ERROR: engine.js missing 2 early returns! Loop bug danger."
    exit 1
fi
echo "✅ PASS ($RETURNS returns)"

# 2. Check Database Rule Size
echo -n "📊 Verifying database signature counts... "
RULES=$(grep -c "pattern:" database.js)
if [ "$RULES" -lt 600 ]; then
    echo "❌ ERROR: database.js dropped below 600 rules! Found only $RULES."
    exit 1
fi
echo "✅ PASS ($RULES rules, $(ls -lh database.js | awk '{print $5}'))"

# 3. Check Cache Manifest Integrity
echo -n "📁 Auditing Service Worker asset sync... "
MISSING=0

# Clean explicit array tracking list
FILES=(
  "index.html"
  "manifest.json"
  "database.js"
  "engine.js"
  "runner.js"
  "code-engine.js"
  "override.js"
  "langs/dictionary.js"
  "plugins/loader.js"
  "plugins/power-ui.js"
  "plugins/reporter.js"
  "plugins/viral.js"
)

for f in "${FILES[@]}"; do
    if [ ! -f "$f" ]; then
        echo -e "\n❌ MISSING FILE FROM DISK: $f"
        MISSING=$((MISSING + 1))
    fi
done

if [ "$MISSING" -gt 0 ]; then
    echo "❌ DEPLOY ABORTED: Missing cache components."
    exit 1
fi
echo "✅ PASS (All cache files present on disk)"

# 4. Trigger Surge CDN Sync
echo "🚀 Compiling deployment to dzivisa-v12.surge.sh..."
surge --project . --domain dzivisa-v12.surge.sh
