import pathlib
p = pathlib.Path("index.html")
html = p.read_text(encoding='utf-8', errors='ignore')

# Make msg bar bigger - find and replace or add CSS
css_big = """
<style id="msg-big">
.msg-bar{ padding:18px 20px !important; font-size:16px !important; min-height:56px !important; border-radius:16px !important; }
.msg-bar input, .msg-bar textarea{ font-size:16px !important; padding:14px !important; }
</style>
"""

if 'id="msg-big"' not in html:
    html = html.replace('</head>', css_big + '</head>')

p.write_text(html, encoding='utf-8')
print("Msg bar BIGGER done!")
