import pathlib, re
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8', errors='ignore')

# Find Message Scanner box and replace with REAL textarea
old_pattern = r'<div[^>]*>.*?Use: Paste ANY msg.*?</div>\s*<div[^>]*>.*?SCAN \+ AUDIO.*?</div>'
# Simpler: inject working textarea before the SCAN button
fix = '''
<div style="margin:10px; padding:10px; background:#0a0a0a; border:2px solid #00ffff; border-radius:12px;">
<textarea id="REAL_MSG_BAR" placeholder="PASTE ANY MSG HERE - YEMAHARA = 100% SCAM" style="width:100%; height:80px; background:#111; color:#0f0; border:1px solid #0ff; border-radius:8px; padding:10px; font-size:16px;"></textarea>
<button onclick="
let m=document.getElementById('REAL_MSG_BAR').value;
if(!m){alert('Paste msg first!'); return;}
let res = SCAN_100 ? SCAN_100(m) : {score:100};
let box = document.getElementById('scanResult') || document.createElement('div');
box.id='scanResult';
box.style.cssText='margin:10px; padding:15px; background:#200; border:2px solid red; border-radius:10px; color:white; font-weight:bold; font-size:18px;';
box.innerHTML = '🚨 ' + res.score + '% ' + (res.safe?'SAFE':'SCAM - YEMAHARA!') + '<br><small>' + m.substring(0,60) + '</small>';
document.getElementById('REAL_MSG_BAR').parentNode.appendChild(box);
if(window.speechSynthesis){let u=new SpeechSynthesisUtterance(res.score + ' percent scam'); speechSynthesis.speak(u);}
" style="margin-top:10px; width:100%; padding:12px; background:linear-gradient(to bottom, #ff0000, #aa0000); color:white; font-weight:bold; border-radius:8px; border:none; font-size:16px;">🚨 SCAN PASTED MSG - TAP HERE</button>
<div id="scanResult"></div>
</div>
'''

# Insert after Message Scanner title
h = h.replace('Message Scanner • 100% Offline', 'Message Scanner • 100% Offline - FIXED PASTE' + fix, 1)

p.write_text(h, encoding='utf-8')
print("REAL PASTE BAR ADDED!")
