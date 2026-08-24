import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

# Remove all floating gear popups and tooltips that come outside
import re

# CSS to keep everything INSIDE
fix = """
<style id="final-inside-fix">
/* Gear - move inside, not covering */
button[style*="gear"], .gear-btn, div[style*="⚙️"] {
  position: relative !important;
  float: right !important;
  top: auto !important;
  right: auto !important;
  margin: 5px !important;
  z-index: 10 !important;
}

/* Top locked bar - keep inside, no overflow */
div[style*="LOCKED"] {
  position: relative !important;
  width: 100% !important;
  max-width: 100vw !important;
  box-sizing: border-box !important;
  overflow: hidden !important;
  white-space: nowrap !important;
  text-overflow: ellipsis !important;
  font-size: 12px !important;
  padding: 6px !important;
}

/* Bottom domain popup - hide it, stays inside */
div[style*="dzivisa-v12.surge.sh"] {
  display: none !important;
}

/* SCAN + AUDIO row - keep inside */
div[style*="SCAN + AUDIO"] {
  display: flex !important;
  flex-wrap: nowrap !important;
  gap: 5px !important;
  width: 100% !important;
  overflow: hidden !important;
}
div[style*="SCAN + AUDIO"] button {
  flex: 1 !important;
  font-size: 11px !important;
  min-width: 0 !important;
}

/* SAFE buttons - hide extra duplicates, keep inside */
button:contains("SAFE") {
  max-width: 100% !important;
  box-sizing: border-box !important;
}

/* Bottom nav - keep inside, no popup */
div[style*="HOME"] {
  position: fixed !important;
  bottom: 0 !important;
  left: 0 !important;
  width: 100% !important;
  max-width: 100vw !important;
  box-sizing: border-box !important;
  z-index: 999 !important;
}

/* Remove any fixed outside elements */
#owner-wm, #owner-watermark, .protection-bar { display: none !important; }
</style>
"""

if 'final-inside-fix' not in h:
    h = h.replace('</head>', fix + '</head>')

# Hide the surge.sh tooltip
h = h.replace('dzivisa-v12.surge.sh', 'dzivisa-v12.surge.sh - Protected Inside')

p.write_text(h, encoding='utf-8')
print("FIXED - Everything INSIDE, no outside popups!")
