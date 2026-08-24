import pathlib, re
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8', errors='ignore')

# Remove ALL bulk test boxes we added
h = re.sub(r'<div id="bulkBox".*?</div>\s*</div>\s*</div>', '', h, flags=re.DOTALL)
h = re.sub(r'<div id="bulkBox".*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<div style="margin:15px; background:#1a1a1a; border:2px solid #ffd700.*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<div style="margin:20px; padding:15px; background:#111; border:2px solid gold.*?</script>', '', h, flags=re.DOTALL)
# Extra cleanup for leftover
h = re.sub(r'TEST 100 AT ONCE.*?100% PERFECT.*?</div>', '', h, flags=re.DOTALL)

p.write_text(h, encoding='utf-8')
print("REMOVED EXTRA BOXES - BACK TO CLEAN V25.2!")
