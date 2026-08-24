import pathlib
p=pathlib.Path("index.html")
t=p.read_text()
# Perfect no-complain palette
t=t.replace("#00E5FF","#4DD0E1").replace("#00B8D4","#26C6DA")
t=t.replace("background:#000","background:#121212")
t=t.replace("#000;color:#fff","#121212;color:#E0E0E0")
t=t.replace("color:#fff","color:#E0E0E0")
t=t.replace("filter:drop-shadow(0 0 20px rgba(0,229,255,0.6))","filter:drop-shadow(0 0 12px rgba(77,208,225,0.3))")
t=t.replace("box-shadow:0 4px 15px rgba(0,229,255,0.4)","box-shadow:0 2px 8px rgba(0,0,0,0.4)")
p.write_text(t)
print("✅ NO-COMPLAIN AQUA APPLIED: #4DD0E1 soft, #121212 bg, #E0E0E0 text")
