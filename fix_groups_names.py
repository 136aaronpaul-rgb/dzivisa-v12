import pathlib, re
p = pathlib.Path("index.html")
html = p.read_text(encoding='utf-8', errors='ignore')

# Replace old group names with recognizable Zim names
replacements = {
    'Group 1': '🇿🇼 MUTEMO - Zimbabwe Traffic Laws',
    'Group 2': '🇿🇼 Family Law - Kodzero Dzemhuri ZW',
    'Group 3': '📱 EcoCash & Scam Protection',
    'Group 4': '⚖️ Labour Law - Basa ZW',
    'Group 5': '🏠 Land Law - Munda ZW',
    'International': '🌍 Diaspora Laws - USA/UK/SA',
    'General Law': '🇿🇼 Zimbabwe Main Laws',
}

for old, new in replacements.items():
    if old in html:
        html = html.replace(old, new)
        print(f"Fixed: {old} -> {new}")

p.write_text(html, encoding='utf-8')
print("Groups renamed - recognizable now!")
