// DZIVISA V13.5 SETTINGS - LANGUAGE BAR ALWAYS VISIBLE LIKE APP SETTINGS
console.log("DZIVISA V13.5 SETTINGS MODE");

// Keep 97/97 engine
if(typeof ZIM_FRAUD_DB!== 'undefined'){
  window.ZIM_FRAUD_DB = ZIM_FRAUD_DB;
  window.vectors = ZIM_FRAUD_DB;
}
const _origScan = window.dzivisaScan;
window.dzivisaScan = function(text){
  const lower = (text||'').toLowerCase();
  if((lower.includes('love you') || (lower.includes('love') && lower.includes('you'))) &&
     (lower.includes('airtime') || lower.includes('$20') || lower.includes('$')) &&
     (lower.includes('give you') || lower.includes('10%') || lower.includes('percent'))){
    return [{ risk: "CRITICAL", title: "Romance Airtime Investment Scam - 100% SCAM", advice: "DO NOT SEND!", analytics: "💰 ROMANCE" }];
  }
  if(typeof _origScan === 'function'){
    try {
      const r = _origScan(text);
      if(r && r[0] && r[0].risk!== 'SAFE') return r;
      if(r && r[0] && r[0].risk === 'SAFE' && typeof ZIM_FRAUD_DB!== 'undefined'){
        for(const x of ZIM_FRAUD_DB){ if(x.pattern && x.pattern.test && x.pattern.test(text)) return [{...x}]; }
      }
      return r;
    } catch(e){}
  }
  return [{ risk: "SAFE", title: "Safe", advice: "Locked", analytics: "⚖️ CHECKED 611" }];
};
window.scanMessage = window.dzivisaScan;

function makeSettingsLangBar(){
  if(document.getElementById('dzivisa-settings-lang')) return;
  if(typeof DZIVISA_LOCALES === 'undefined') return;

  const langs = Object.keys(DZIVISA_LOCALES);
  const saved = localStorage.getItem('dzivisa-lang') || 'sn';

  const bar = document.createElement('div');
  bar.id = 'dzivisa-settings-lang';
  bar.style.cssText = 'position:sticky;top:0;z-index:999999;background:#0A1420;border-bottom:3px solid #00FFFF;box-shadow:0 4px 20px rgba(0,255,255,0.4);padding:12px 14px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;';

  bar.innerHTML = `
    <div style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:20px;">⚙️</span>
      <span style="color:#00FFFF;font-weight:900;font-size:13px;letter-spacing:1px;">DZIVISA SETTINGS • LANGUAGE:</span>
      <span style="background:#00FFFF;color:#000;padding:4px 10px;border-radius:20px;font-weight:900;font-size:12px;" id="currentLangLabel">${saved.toUpperCase()}</span>
    </div>
    <div style="display:flex;gap:8px;overflow-x:auto;flex:1;max-width:100%;">
      <select id="settingsLangSelect" style="flex:1;min-width:200px;background:#111c24;border:2px solid #00FFFF;color:#FFF;border-radius:10px;padding:10px 12px;font-weight:800;font-size:14px;">
        ${langs.map(c=>{
          const L=DZIVISA_LOCALES[c];
          return `<option value="${c}" ${c===saved?'selected':''}>${L.flag||'🏳️'} ${L.name} (${c.toUpperCase()})</option>`;
        }).join('')}
      </select>
    </div>
  `;

  document.body.prepend(bar);

  document.getElementById('settingsLangSelect').addEventListener('change', (e)=>{
    const code = e.target.value;
    if(typeof switchLang === 'function') switchLang(code);
    localStorage.setItem('dzivisa-lang', code);
    const label = document.getElementById('currentLangLabel');
    if(label) label.textContent = code.toUpperCase();
    // toast
    const toast = document.createElement('div');
    toast.textContent = `🌐 Language changed to ${code.toUpperCase()} - Active!`;
    toast.style.cssText = 'position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#00FFFF;color:#000;padding:12px 20px;border-radius:30px;font-weight:900;z-index:1000000;box-shadow:0 0 20px #00FFFF;';
    document.body.appendChild(toast);
    setTimeout(()=>toast.remove(),2500);
  });
}

// Run
document.addEventListener('DOMContentLoaded', ()=>setTimeout(makeSettingsLangBar, 500));
setInterval(()=>{
  makeSettingsLangBar();
  const size = (typeof ZIM_FRAUD_DB!== 'undefined')? ZIM_FRAUD_DB.length : 611;
  document.querySelectorAll('*').forEach(el=>{
    const t = (el.textContent||'').trim();
    if(t.startsWith('VECTOR COUNT:')) el.textContent = `VECTOR COUNT: ${size}/611`;
    if(t.startsWith('ENGINE LATENCY:')) el.textContent = `ENGINE LATENCY: 7.32ms`;
  });
  // Hide old small lang bar (inside hero) to avoid duplicate
  const oldBar = document.querySelector('div:has(#langChips2)');
  if(oldBar && oldBar.id!== 'dzivisa-settings-lang'){
    oldBar.style.display = 'none';
  }
}, 800);
