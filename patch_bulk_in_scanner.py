import pathlib
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8', errors='ignore')

# Make your existing scanner handle multi-line paste
js = """
<script>
// MAKE SCANNER BULK - paste many lines at once
let oldScan = window.SCAN_100 || window.scanMessage;
let msgBar = document.querySelector('textarea, input[placeholder*="Paste"]');
if(msgBar){
  msgBar.placeholder = "Paste 1 or 100 messages - one per line - YEMAHARA = 100% SCAM";
  let btn = document.querySelector('#scanBtn') || document.querySelector('button');
  // If paste has \\n, scan all
  msgBar.addEventListener('paste', (e)=>{
    setTimeout(()=>{
      let txt = msgBar.value;
      if(txt.includes('\\n') && txt.split('\\n').length>2){
        let msgs = txt.split('\\n');
        let resDiv = document.querySelector('#result') || document.createElement('div');
        resDiv.innerHTML = `<b style='color:gold'>BULK SCAN ${msgs.length} MSGS:</b><br>`;
        let caught=0;
        msgs.forEach((m,i)=>{
          if(m.trim().length<3) return;
          let r = SCAN_100(m);
          if(r.score>=80) caught++;
          resDiv.innerHTML += `${i+1}. ${r.score>=80?'🚨':'✅'} ${r.score}% ${m.substring(0,40)}<br>`;
        });
        resDiv.innerHTML += `<br><b style='color:gold; font-size:18px'>RESULT: ${caught}/${msgs.length} = ${Math.round(caught*100/msgs.length)}%</b>`;
      }
    },100);
  });
}
</script>
"""

h = h.replace('</body>', js + '</body>')
p.write_text(h, encoding='utf-8')
print("BULK PASTE ENABLED IN YOUR MSG BAR!")
