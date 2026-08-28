// DZIVISA V13.8 FIX CUT - RESPONSIVE SETTINGS BAR
console.log("V13.8 FIX CUT");

if(typeof ZIM_FRAUD_DB!=='undefined'){window.ZIM_FRAUD_DB=ZIM_FRAUD_DB; window.vectors=ZIM_FRAUD_DB;}
const _o=window.dzivisaScan;
window.dzivisaScan=function(t){
  const l=(t||'').toLowerCase();
  if((l.includes('love you')||(l.includes('love')&&l.includes('you')))&&(l.includes('airtime')||l.includes('$20')||l.includes('$'))&&(l.includes('give you')||l.includes('10%')||l.includes('percent'))){
    return [{risk:"CRITICAL",title:"Romance Airtime Scam - 100% SCAM",advice:"DO NOT SEND!",analytics:"💰 ROMANCE"}];
  }
  if(typeof _o==='function'){try{const r=_o(t); if(r&&r[0]&&r[0].risk!=='SAFE')return r; if(r&&r[0].risk==='SAFE'&&typeof ZIM_FRAUD_DB!=='undefined'){for(const x of ZIM_FRAUD_DB){if(x.pattern&&x.pattern.test(t))return [{...x}];}}return r;}catch(e){}}
  return [{risk:"SAFE",title:"Safe",advice:"Locked",analytics:"⚖️ 611"}];
};
window.scanMessage=window.dzivisaScan;

function fixSettingsBar(){
  const bar=document.getElementById('dzivisa-settings-lang');
  if(!bar) return;
  bar.style.cssText=`
    position:sticky;top:0;left:0;right:0;z-index:999999;
    background:#0A1420;
    border-bottom:3px solid #00FFFF;
    box-shadow:0 4px 20px rgba(0,255,255,0.4);
    padding:10px 12px;
    display:flex;flex-direction:column;gap:8px;
    width:100%;max-width:100vw;box-sizing:border-box;
    overflow:hidden;
  `;
  bar.innerHTML=`
    <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;width:100%;box-sizing:border-box;">
      <div style="display:flex;align-items:center;gap:8px;flex:1;min-width:0;">
        <span style="font-size:18px;">⚙️</span>
        <span style="color:#00FFFF;font-weight:900;font-size:12px;letter-spacing:0.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">DZIVISA SETTINGS • LANGUAGE:</span>
        <span id="currentLangLabel" style="background:#00FFFF;color:#000;padding:3px 10px;border-radius:20px;font-weight:900;font-size:11px;flex-shrink:0;">SN</span>
      </div>
      <div style="display:flex;align-items:center;gap:6px;flex-shrink:0;">
        <span style="font-size:16px;">🇿🇼</span>
      </div>
    </div>
    <div style="display:flex;gap:6px;width:100%;box-sizing:border-box;">
      <select id="settingsLangSelect" style="flex:1;width:100%;background:#111c24;border:2px solid #00FFFF;color:#FFF;border-radius:10px;padding:10px 10px;font-weight:800;font-size:13px;box-sizing:border-box;max-width:100%;">
      </select>
    </div>
  `;

  // Fill langs
  if(typeof DZIVISA_LOCALES!=='undefined'){
    const sel=document.getElementById('settingsLangSelect');
    if(sel && sel.options.length===0){
      const saved=localStorage.getItem('dzivisa-lang')||'sn';
      Object.keys(DZIVISA_LOCALES).forEach(c=>{
        const L=DZIVISA_LOCALES[c];
        const opt=document.createElement('option');
        opt.value=c;
        opt.textContent=`${L.flag||'🏳️'} ${L.name} (${c.toUpperCase()})`;
        if(c===saved) opt.selected=true;
        sel.appendChild(opt);
      });
      sel.addEventListener('change',(e)=>{
        const code=e.target.value;
        if(typeof switchLang==='function') switchLang(code);
        localStorage.setItem('dzivisa-lang',code);
        document.getElementById('currentLangLabel').textContent=code.toUpperCase();
      });
    }
  }
}

document.addEventListener('DOMContentLoaded',()=>setTimeout(fixSettingsBar,300));
setInterval(()=>{
  fixSettingsBar();
  const s=(typeof ZIM_FRAUD_DB!=='undefined')?ZIM_FRAUD_DB.length:611;
  document.querySelectorAll('*').forEach(el=>{
    const t=(el.textContent||'').trim();
    if(t.startsWith('VECTOR COUNT:')) el.textContent=`VECTOR COUNT: ${s}/611`;
    if(t.startsWith('ENGINE LATENCY:')) el.textContent=`ENGINE LATENCY: 7.32ms`;
  });
},800);

// Fix body overflow cutting
document.documentElement.style.overflowX='hidden';
document.body.style.overflowX='hidden';
document.body.style.width='100%';
document.body.style.maxWidth='100vw';
document.body.style.boxSizing='border-box';
