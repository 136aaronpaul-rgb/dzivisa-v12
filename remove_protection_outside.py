import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

# Remove ALL outside protection watermarks
import re

# Remove divs with PROTECTED text outside
h = re.sub(r'<div[^>]*>.*?©2026 AARON PAULOS.*?PROTECTED.*?</div>', '', h, flags=re.IGNORECASE|re.DOTALL)
h = re.sub(r'<div[^>]*id="owner-wm"[^>]*>.*?</div>', '', h, flags=re.DOTALL)
h = re.sub(r'<div[^>]*id="owner-watermark"[^>]*>.*?</div>', '', h, flags=re.DOTALL)

# Remove the JS that creates watermark every 1.5 seconds
h = re.sub(r'setInterval\(\(\)=>\{[^}]*owner-wm[^}]*\},1500\);', '', h, flags=re.DOTALL)
h = re.sub(r'setInterval\(\(\)=>\{[^}]*owner-watermark[^}]*\},2000\);', '', h, flags=re.DOTALL)
h = re.sub(r'setInterval\(\(\)=>\{.*?owner.*?\},.*?\)\);', '', h, flags=re.DOTALL|re.IGNORECASE)

# Remove inline watermark creation
h = re.sub(r'if\(!document\.getElementById\(\'owner.*?\)\)\{.*?document\.body\.appendChild\(w\);\s*\}\s*\},?\s*\d+\)', '', h, flags=re.DOTALL)

# Add protection ONLY INSIDE footer - not outside - invisible but protected in code
# Keep protection in console only, not on screen
new_protection = """
<script>
// Protection INSIDE - not visible outside - only in code
console.log('🔒 ©2026 AARON PAULOS - Protected - GOV LAW');
document.addEventListener('contextmenu', e => e.preventDefault());
</script>
<style>
/* Hide any protection that tries to come outside */
#owner-wm, #owner-watermark, div[style*="PROTECTED"] { display: none !important; }
body { overflow-x: hidden !important; }
</style>
"""

if '</head>' in h:
    h = h.replace('</head>', new_protection + '</head>')

p.write_text(h, encoding='utf-8')
print("REMOVED - Protection will NOT come outside anymore!")
print("Protection only inside code now - not visible on screen")
