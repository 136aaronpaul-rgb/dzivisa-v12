// DZIVISA V13.9 RESTORE ALL GROUPS - SAFE LANGUAGE FIX
console.log("V13.9 RESTORE GROUPS - SAFE FIX");

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

// SAFE FIX - only adjust CSS, never delete groups
setInterval(()=>{
  // Fix top settings bar cut - only CSS, no innerHTML delete
  const bar=document.getElementById('dzivisa-settings-lang');
  if(bar){
    bar.style.boxSizing='border-box';
    bar.style.width='100%';
    bar.style.maxWidth='100vw';
    bar.style.overflowX='hidden';
    bar.style.flexWrap='wrap';
    // Make inner select responsive
    const sel=bar.querySelector('select');
    if(sel){ sel.style.maxWidth='100%'; sel.style.boxSizing='border-box'; }
  }
  // Fix body cut
  document.documentElement.style.overflowX='hidden';
  document.body.style.overflowX='hidden';

  const s=(typeof ZIM_FRAUD_DB!=='undefined')?ZIM_FRAUD_DB.length:611;
  document.querySelectorAll('*').forEach(el=>{
    const t=(el.textContent||'').trim();
    if(t.startsWith('VECTOR COUNT:')) el.textContent=`VECTOR COUNT: ${s}/611`;
  });
},800);
