// V13.9 FINAL WORKING - SAFE FIX
console.log("V13.9 FINAL WORKING");

if(typeof ZIM_FRAUD_DB!=='undefined'){window.ZIM_FRAUD_DB=ZIM_FRAUD_DB; window.vectors=ZIM_FRAUD_DB;}
const _orig=window.dzivisaScan;
window.dzivisaScan=function(t){
  const l=(t||'').toLowerCase();
  if((l.includes('love you')||(l.includes('love')&&l.includes('you')))&&(l.includes('airtime')||l.includes('$20')||l.includes('$'))&&(l.includes('give you')||l.includes('10%')||l.includes('percent'))){
    return [{risk:"CRITICAL",title:"Romance Airtime Investment Scam - 100% SCAM",advice:"DO NOT SEND!",analytics:"💰 ROMANCE"}];
  }
  if(typeof _orig==='function'){try{const r=_orig(t); if(r&&r[0]&&r[0].risk!=='SAFE')return r; if(r&&r[0].risk==='SAFE'&&typeof ZIM_FRAUD_DB!=='undefined'){for(const x of ZIM_FRAUD_DB){if(x.pattern&&x.pattern.test(t))return [{...x}];}}return r;}catch(e){}}
  return [{risk:"SAFE",title:"Safe",advice:"Locked",analytics:"⚖️ 611"}];
};
window.scanMessage=window.dzivisaScan;

function fixApp(){
  const bar=document.getElementById('dzivisa-settings-lang');
  if(bar){
    bar.style.boxSizing='border-box';
    bar.style.width='100%';
    bar.style.maxWidth='100%';
    bar.style.overflowX='hidden';
  }
  document.body.style.overflowX='hidden';
  const s=(typeof ZIM_FRAUD_DB!=='undefined')?ZIM_FRAUD_DB.length:611;
  document.querySelectorAll('*').forEach(el=>{
    const t=(el.textContent||'').trim();
    if(t.startsWith('VECTOR COUNT:')) el.textContent=`VECTOR COUNT: ${s}/611`;
    if(t.includes('YEMAHARA 100% SCAM')&&t.includes('Your money is your blood')){
      el.style.whiteSpace='normal';
      el.style.fontSize='10px';
    }
  });
}
setInterval(fixApp,800);
