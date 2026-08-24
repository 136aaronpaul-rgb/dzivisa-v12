import pathlib, re, datetime
p = pathlib.Path("index.html")
html = p.read_text(encoding='utf-8', errors='ignore')
backup = pathlib.Path(f"index.html.backup-{datetime.datetime.now().strftime('%Y%m%d-%H%M')}")
backup.write_text(html, encoding='utf-8')
print(f"Backup saved: {backup}")

css = """
<style id="dz-themes">
body[data-theme="facebook"]{background:#F0F2F5 !important}
body[data-theme="facebook"] .card{background:#fff !important;color:#000 !important;border:1px solid #ddd !important}
body[data-theme="facebook"] .nav-bar{background:#fff !important}
.theme-btn{padding:12px;border-radius:12px;width:100%;margin:6px 0;font-weight:bold;border:none}
</style>
"""

js = """
<script id="dz-theme-js">
function setTheme(t){document.body.setAttribute('data-theme',t);localStorage.setItem('dzivisa-theme',t);let e=document.getElementById('themeStatus');if(e)e.innerText='Current: '+t.toUpperCase()+' ✓';}
(function(){let s=localStorage.getItem('dzivisa-theme')||'aqua';document.body.setAttribute('data-theme',s);})();
</script>
"""

inject = """
<div class="card" style="padding:16px;margin:16px;border-radius:16px;background:#003845;border:1px solid #00E5FF">
<h3 style="color:#00E5FF;margin:0 0 12px 0">🎨 DESIGN - Facebook Style but DZIVISA</h3>
<button class="theme-btn" style="background:#00E5FF;color:#000" onclick="setTheme('aqua')">🌊 AQUA - Your Design</button>
<button class="theme-btn" style="background:#0866FF;color:#fff" onclick="setTheme('facebook')">🔵 LIGHT - Gogo Friendly</button>
<p id="themeStatus" style="color:#00E5FF;margin-top:10px">Current: AQUA</p>
</div>
"""

if '<style id="dz-themes">' not in html:
    html = html.replace('</head>', css + '</head>')
if '<script id="dz-theme-js">' not in html:
    html = html.replace('</body>', js + '</body>')

m = re.search(r'<div[^>]*id=["\']setPage["\'][^>]*>', html, re.IGNORECASE)
if m and 'DESIGN - Facebook Style' not in html:
    html = html[:m.end()] + inject + html[m.end():]

p.write_text(html, encoding='utf-8')
print("DONE! Now run: surge --domain dzivisa-v12.surge.sh")
