import pathlib, re
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8', errors='ignore')

# Remove my broken bulk code stuck in scanner
h = re.sub(r'BULK SCAN 100 MSGS.*?</div>', '', h, flags=re.DOTALL)
h = re.sub(r'bulk.*?\n', '', h, flags=re.IGNORECASE)
h = re.sub(r'Bulk.*?\n', '', h, flags=re.IGNORECASE)

# Fix scanner placeholder back to normal
h = h.replace('BULK SCAN 100 MSGS', 'Paste ANY message - YEMAHARA = 100% SCAM')
h = h.replace('BULK SCAN', 'Paste message')

# Remove extra scripts I added
h = re.sub(r'<script>.*?BULK.*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<script>.*?bulk.*?</script>', '', h, flags=re.DOTALL)

p.write_text(h, encoding='utf-8')
print("BAR UNLOCKED!")
