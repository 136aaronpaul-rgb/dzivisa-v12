import pathlib
p=pathlib.Path("index.html")
txt=p.read_text()

# Backup already done, but make second
p.write_text(txt)  # keep

old_code = """let cont=document.getElementById('sectionsContainer');
let hg='';
for(let g=1;g<=50;g++){let start=(g-1)*20+1;let end=g*20;let btns='';for(let s=start;s<=end;s++){btns+='<button class="opt-btn" onclick="openSection('+s+','+g+')">S'+s+'</button>';}hg+='<div class="group-box"><div style="display:flex;justify-content:space-between"><h3 style="color:#FFD700;font-size:13px">📦 GROUP '+g+' - Sec '+start+' to '+end+' - USE ONLY</h3><span style="background:#FFD700;color:#000;padding:3px 8px;border-radius:12px;font-size:10px;font-weight:900">🔒 USE NO EDIT</span></div><div class="sec-grid">'+btns+'</div></div>';}
cont.innerHTML=hg;"""

new_code = """let cont=document.getElementById('sectionsContainer');
let menuHtml='<div id="groupMenuList" style="padding:10px"><h3 style="color:#FFD700;text-align:center;margin:12px 0;font-size:14px">📦 ALL GROUPS - TAP TO OPEN (Like SET) - USE ONLY</h3>';
let pagesHtml='';
for(let g=1;g<=50;g++){
  let start=(g-1)*20+1; let end=g*20;
  menuHtml+='<button onclick="openGroupPage('+g+')" style="display:block;width:100%;margin:7px 0;padding:14px;background:linear-gradient(145deg,#111,#000);border:2px solid #FFD700;color:#FFD700;border-radius:12px;font-weight:900;text-align:left">📦 GROUP '+g+' - Sec '+start+' to '+end+' - USE ONLY <span style="float:right;background:#FFD700;color:#000;padding:3px 10px;border-radius:10px;font-size:10px">🔒 OPEN</span></button>';
  let btns=''; for(let s=start;s<=end;s++){btns+='<button class="opt-btn" onclick="openSection('+s+','+g+')">S'+s+'</button>';}
  pagesHtml+='<div id="groupPage'+g+'" class="group-page" style="display:none;padding:10px"><button onclick="goHomeGroups()" style="background:#FFD700;color:#000;border:none;padding:10px 16px;border-radius:10px;font-weight:900;margin-bottom:12px">⬅ BACK TO GROUPS</button><div class="group-box"><div style="display:flex;justify-content:space-between;align-items:center"><h3 style="color:#FFD700;font-size:14px">📦 GROUP '+g+' - Sec '+start+' to '+end+' - USE ONLY</h3><span style="background:#FFD700;color:#000;padding:4px 10px;border-radius:12px;font-size:10px;font-weight:900">🔒 USE NO EDIT</span></div><div class="sec-grid">'+btns+'</div></div><div style="text-align:center;margin-top:14px;color:#FFD700;font-size:11px;font-weight:700">🔒 LOCKED • USE ONLY • NO EDIT • dzivisa-v12.surge.sh • Protected by Aaron Paul</div></div>';
}
cont.innerHTML=menuHtml+'</div>'+pagesHtml;
window.openGroupPage=function(g){
  let menu=document.getElementById('groupMenuList');
  if(menu) menu.style.display='none';
  document.querySelectorAll('.group-page').forEach(p=>p.style.display='none');
  document.getElementById('groupPage'+g).style.display='block';
  window.scrollTo(0,0);
}
window.goHomeGroups=function(){
  document.querySelectorAll('.group-page').forEach(p=>p.style.display='none');
  let menu=document.getElementById('groupMenuList');
  if(menu) menu.style.display='block';
  window.scrollTo(0,0);
}
"""

if old_code in txt:
    txt = txt.replace(old_code, new_code)
    p.write_text(txt)
    print("✅ FIXED! Groups now have pages like SET")
else:
    print("⚠️ Old code not found - maybe already fixed or different spacing")
    # try fuzzy
    import re
    pattern = r"let cont=document\.getElementById\('sectionsContainer'\);.*?cont\.innerHTML=hg;"
    if re.search(pattern, txt, re.DOTALL):
        txt = re.sub(pattern, new_code, txt, flags=re.DOTALL)
        p.write_text(txt)
        print("✅ FIXED with fuzzy match!")
    else:
        print("❌ Could not find - send me sed -n '250,256p' again")
