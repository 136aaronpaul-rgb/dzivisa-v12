import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

# Remove any outside protection that makes gray boxes
# Keep only footer protection inside - not fixed
if 'PROTECTED - AUDIO WORKS' not in h:
    # Add minimal inside protection - no overlay
    inside_footer = """
<div style="text-align:center;padding:10px;margin-top:20px;border-top:1px solid #222;color:#4DD0E1;font-size:10px">
🔒 DZIVISA V25.2 AQUA - GOV LAW PROTECTED<br>
Protected • Use Everything • Audio Works • 100% Scam Catch<br>
Forever: dzivisa-v12.surge.sh • © 2026 Aaron Paul • Protected Super App - No one can edit!
</div>
"""
    h = h.replace('</body>', inside_footer + '</body>')

# Remove broken iframe src that cause gray boxes
h = h.replace('https://google.com', 'about:blank')

p.write_text(h, encoding='utf-8')
print("Added INSIDE protection only - no outside overlay!")
