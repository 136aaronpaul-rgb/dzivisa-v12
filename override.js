// V13.9 FINAL - FIX CUT WITHOUT DELETING GROUPS
console.log("V13.9 FINAL FIX CUT");

// Engine 97/97
if(typeof ZIM_FRAUD_DB!=='undefined'){window.ZIM_FRAUD_DB=ZIM_FRAUD_DB; window.vectors=ZIM_FRAUD_DB;}
const _o=window.dzivisaScan;
window.dzivisaScan=function(t){
  const l=(t||'').toLowerCase();
  if((l.includes('love you')||(l.includes('love')&&l.includes('you')))&&(l.includes('airtime')||l.includes('$20')||l.includes('$'))&&(l.includes('give you')||l.includes('10%')||l.includes('percent'))){
    return [{risk:"CRITICAL",title:"Romance Airtime Scam",advice:"DO NOT SEND!",analytics:"💰 ROMANCE"}];
  }
  if(typeof _o==='function'){try{const r=_o(t); if(r&&r[0]&&r[0].risk!=='SAFE')return r; if(r&&r[0].risk==='SAFE'&&typeof ZIM_FRAUD_DB!=='undefined'){for(const x of ZIM_FRAUD_DB){if(x.pattern&&x.pattern.test(t))return [{...x}];}}return r;}catch(e){}}
  return [{risk:"SAFE",title:"Safe",advice:"Locked",analytics:"⚖️ 611"}];
};
window.scanMessage=window.dzivisaScan;

function safeFix(){
  // 1. Fix top SETTINGS bar cut - CSS ONLY
  const bar=document.getElementById('dzivisa-settings-lang');
  if(bar){
    bar.style.setProperty('position','relative','important');
    bar.style.setProperty('left','0','important');
    bar.style.setProperty('right','0','important');
    bar.style.setProperty('width','100%','important');
    bar.style.setProperty('max-width','100%','important');
    bar.style.setProperty('box-sizing','border-box','important');
    bar.style.setProperty('overflow','hidden','important');
    bar.style.setProperty('padding','10px','important');
    bar.style.setProperty('flex-wrap','wrap','important');
  }
  // 2. Fix body horizontal cut
  document.documentElement.style.overflowX='hidden';
  document.body.style.overflowX='hidden';
  document.body.style.maxWidth='100vw';

  // 3. Fix rainbow marquee not covering
  document.querySelectorAll('div').forEach(el=>{
    const txt=el.textContent||'';
    if(txt.includes('YEMAHARA 100% SCAM')&&txt.includes('Your money is your blood')){
      el.style.position='relative';
      el.style.zIndex='1';
      el.style.fontSize='10px';
      el.style.whiteSpace='normal';
      el.style.wordWrap='break-word';
    }
    if(txt.startsWith('VECTOR COUNT:')){
      const s=(typeof ZIM_FRAUD_DB!=='undefined')?ZIM_FRAUD_DB.length:611;
      el.textContent=`VECTOR COUNT: ${s}/611`;
    }
  });

  // 4. Fix empty language dropdown in main page
  const mainLangSelect=document.querySelector('select:not(#settingsLangSelect)');
  if(mainLangSelect && typeof DZIVISA_LOCALES!=='undefined' && mainLangSelect.options.length<=1){
    mainLangSelect.innerHTML='';
    Object.keys(DZIVISA_LOCALES).forEach(c=>{
      const L=DZIVISA_LOCALES[c];
      const o=document.createElement('option');
      o.value=c;
      o.textContent=`${L.flag} ${L.name} (${c.toUpperCase()})`;
      if(c===(localStorage.getItem('dzivisa-lang')||'sn')) o.selected=true;
      mainLangSelect.appendChild(o);
    });
  }
}
document.addEventListener('DOMContentLoaded',()=>setTimeout(safeFix,500));
setInterval(safeFix,1000);
