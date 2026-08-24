function doScan() {
  const input = document.getElementById('msgBar');
  const resultBox = document.getElementById('result');
  if (!input ||!resultBox) return;
  const text = input.value.trim();
  if (!text) { resultBox.innerHTML='<div style="color:orange">Paste message first</div>'; return; }

  const findings = (typeof dzivisaScan === 'function')? dzivisaScan(text) : [];
  resultBox.innerHTML = "";

  let spoken = false;
  findings.forEach(f=>{
    let c = f.risk==="CRITICAL"?"#ff3333":f.risk==="HIGH"?"#ff9900":"#00ff88";
    let bg = f.risk==="CRITICAL"?"#2a0808":f.risk==="HIGH"?"#2a1a08":"#0a1a0a";
    resultBox.innerHTML+=`<div style="background:${bg};border:2px solid ${c};padding:12px;border-radius:10px;margin-bottom:8px;color:#e0e0e0"><b style="color:${c}">[${f.risk}] ${f.title}</b><br><small>${f.advice}</small></div>`;

    if (!spoken && (f.risk==="CRITICAL" || f.risk==="HIGH")) {
      speakDzivisa(f.title + ". " + f.advice);
      spoken=true;
    }
  });

  if (typeof addToHistory==='function') try{addToHistory(text, findings)}catch(e){}
}

function speakDzivisa(t){
  if(!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(t);
  u.rate=0.9; u.pitch=1;
  const voices = window.speechSynthesis.getVoices();
  const v = voices.find(x=>x.lang.includes('en-ZA')||x.lang.includes('en-GB')) || voices[0];
  if(v) u.voice=v;
  window.speechSynthesis.speak(u);
}

function speakMsg(){
  const i=document.getElementById('msgBar');
  if(i&&i.value.trim()) speakDzivisa(i.value);
}
console.log("🔊 Audio shield active");
