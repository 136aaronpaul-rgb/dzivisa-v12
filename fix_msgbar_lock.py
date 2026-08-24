import pathlib, re
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8', errors='ignore')

# 1. Find and fix the LOCK code that blocks #msgBar paste
# The lock disables all inputs - we exempt msgBar

# Remove any onpaste blockers
h = h.replace('onpaste="return false"', '')
h = h.replace("onpaste='return false'", '')

# Fix CSS that blocks user-select
h = h.replace('user-select: none', 'user-select: text')
h = h.replace('user-select:none', 'user-select:text')
h = h.replace('-webkit-user-select: none', '-webkit-user-select: text')

# 2. Add small JS at end to FORCE msgBar always editable and pasteable
fix_js = """
<script>
// FIX ORIGINAL msgBar to ALWAYS allow paste - no change to look!
(function(){
  function unlockMsgBar(){
    let bar = document.getElementById('msgBar');
    if(!bar) return;
    bar.removeAttribute('readonly');
    bar.removeAttribute('disabled');
    bar.style.userSelect='text';
    bar.style.webkitUserSelect='text';
    bar.style.pointerEvents='auto';
    // Allow paste
    bar.addEventListener('paste', function(e){
      e.stopPropagation();
      // let paste happen
      setTimeout(()=>{ 
        if(bar.value) { 
          let btn = document.querySelector('button[onclick*="doScan"]');
          if(btn) {/* auto scan after paste */ }
        }
      }, 300);
    }, true);
    // Allow long press
    bar.addEventListener('contextmenu', function(e){ e.stopPropagation(); }, true);
  }
  setInterval(unlockMsgBar, 500);
  document.addEventListener('DOMContentLoaded', unlockMsgBar);
  setTimeout(unlockMsgBar, 100);
  setTimeout(unlockMsgBar, 2000);
  setTimeout(unlockMsgBar, 3000);
})();
</script>
"""

# Insert before </body>
if '</body>' in h:
    h = h.replace('</body>', fix_js + '</body>')
else:
    h = h + fix_js

p.write_text(h, encoding='utf-8')
print("ORIGINAL msgBar UNLOCKED FOR PASTE - same look!")
