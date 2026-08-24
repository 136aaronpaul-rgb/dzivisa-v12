import pathlib
p = pathlib.Path("index.html")
html = p.read_text(encoding='utf-8', errors='ignore')

# This is the REAL fix - maps GROUP numbers to REAL LAW NAMES people recognize
new_js = """
let GROUP_NAMES = {
1: '🇿🇼 MUTEMO - Zimbabwe Constitution & Rights',
2: '🚗 Traffic Laws ZW - Mitemo Yemugwagwa',
3: '👨‍👩‍👧 Family Law ZW - Kodzero Dzemhuri',
4: '🏠 Land & Property Law ZW - Munda',
5: '⚖️ Criminal Law ZW - Mhosva',
6: '💼 Labour Law ZW - Mutemo WeBasa',
7: '💰 Money, EcoCash & Fraud Protection',
8: '👮 Police, Arrest & Your Rights ZW',
9: '🌍 Diaspora Laws - SA, UK, USA, Botswana',
10: '📱 Cyber Law ZW - Ch 12:07 Scam Protection'
};
// Extend for more groups - repeats pattern
function getGroupName(g){
  if(GROUP_NAMES[g]) return GROUP_NAMES[g];
  let base = ((g-1)%10)+1;
  let batch = Math.floor((g-1)/10)+1;
  return GROUP_NAMES[base] + ' - Part '+batch;
}
"""

# Inject after let menuHtml
if 'GROUP_NAMES' not in html:
    html = html.replace("let menuHtml='<div id=\"groupMenuList\"", new_js + "\nlet menuHtml='<div id=\"groupMenuList\"")

# Replace GROUP display
html = html.replace(
    "📦 GROUP '+g+' • '+start+' to '+end+'",
    "' + getGroupName(g) + ' <br><small style=\"opacity:0.7;font-size:11px\">'+start+' to '+end+' laws</small>'"
)

# Also fix header inside group page
html = html.replace(
    "📦 GROUP '+g+' • '+start+' to '+end+'</h3>",
    "' + getGroupName(g) + '</h3>"
)

html = html.replace(
    "Section '+s+' - Group '+g+' - Protected",
    "' + getGroupName(g) + ' - Section '+s"
)

p.write_text(html, encoding='utf-8')
print("Groups now RECOGNIZABLE!")
