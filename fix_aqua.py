import pathlib
p=pathlib.Path("index.html")
txt=p.read_text()

# Change gold to AQUA theme
replacements = {
    "#FFD700": "#00E5FF",  # Gold -> Bright Aqua
    "#FFA500": "#00B8D4",  # Orange -> Deep Aqua
    "#FFD700,#FFA500": "#00E5FF,#00B8D4",
    "#FFD700 0%,#fff 50%,#FFD700 100%": "#00E5FF 0%,#E0FFFF 50%,#00B8D4 100%",
    "border:2px solid #FFD700": "border:2px solid #00E5FF",
    "border:3px solid #FFD700": "border:3px solid #00E5FF",
    "border-left:4px solid #FFD700": "border-left:4px solid #00E5FF",
    "--gold:#FFD700": "--aqua:#00E5FF; --gold:#00E5FF",
}

for old, new in replacements.items():
    txt = txt.replace(old, new)

# Also update CSS var usage and keep AQUA soft
txt = txt.replace("color:#FFD700", "color:#00E5FF")
txt = txt.replace("background:#FFD700", "background:#00E5FF")
txt = txt.replace("background:linear-gradient(135deg,#FFD700,#FFA500)", "background:linear-gradient(135deg,#00E5FF,#00B8D4)")

# Make buttons more friendly - softer shadow
txt = txt.replace("rgba(255,215,0,0.4)", "rgba(0,229,255,0.4)")
txt = txt.replace("rgba(255,215,0,0.6)", "rgba(0,229,255,0.6)")
txt = txt.replace("#1a1500", "#001a1a")  # hero bg from brownish to aqua dark

p.write_text(txt)
print("✅ AQUA THEME APPLIED! #00E5FF = calm, trust, no hesitate")
