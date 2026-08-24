import pathlib, time
# 1. Update sw.js version to force refresh
p = pathlib.Path("sw.js")
if p.exists():
    txt = p.read_text(encoding='utf-8', errors='ignore')
    # Change cache version
    txt = txt.replace('dzivisa-v12', f'dzivisa-v12-{int(time.time())}')
    txt = txt.replace('CACHE_NAME', f'CACHE_NAME_V{int(time.time())}')
    # If no cache name, add timestamp comment
    if 'CACHE_NAME' not in txt:
        txt = f"// VERSION {int(time.time())}\n" + txt
    p.write_text(txt, encoding='utf-8')
    print("sw.js updated - cache busted!")

# 2. Update manifest version
m = pathlib.Path("manifest.json")
if m.exists():
    t = m.read_text()
    import json
    try:
        j = json.loads(t)
        j['version'] = str(int(time.time()))
        m.write_text(json.dumps(j, indent=2))
        print("manifest updated!")
    except:
        pass

# 3. Update index.html - add version meta
idx = pathlib.Path("index.html")
html = idx.read_text(encoding='utf-8', errors='ignore')
if '<meta name="dzivisa-version"' not in html:
    html = html.replace('<head>', f'<head>\n<meta name="dzivisa-version" content="{int(time.time())}">')
    idx.write_text(html, encoding='utf-8')

print("DONE - cache busted!")
