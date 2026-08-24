import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

lock_code = """<script>
// 🔒 LOCK - Aaron Paulos ©2026 - GOV LAW PROTECTED
document.addEventListener('contextmenu', e=>e.preventDefault());
document.addEventListener('keydown', e=>{
  if(e.key=='F12' || (e.ctrlKey && e.shiftKey && e.key=='I') || (e.ctrlKey && e.key.toLowerCase()=='u')){
    e.preventDefault();
    alert('🔒 Protected by Aaron Paulos ©2026\\nEmail: 136aaronpaul@gmail.com\\nNO COPY - NO EDIT');
    return false;
  }
});
setInterval(()=>{
  if(!document.getElementById('owner-wm')){
    let d=document.createElement('div');
    d.id='owner-wm';
    d.style.cssText='position:fixed;bottom:0;right:0;z-index:99999;background:#000;color:gold;font-size:9px;padding:4px 8px;border-radius:6px 0 0 0;border:1px solid gold';
    d.innerText='🔒 ©2026 AARON PAULOS | 136aaronpaul@gmail.com | PROTECTED';
    document.body.appendChild(d);
  }
},1500);
</script>
"""

if '<head>' in h:
    h = h.replace('<head>', '<head>\n' + lock_code)
    p.write_text(h, encoding='utf-8')
    print("LOCK ADDED - Owner watermark + No right click + No F12!")
else:
    print("No head tag found")
