function openPowerLab() {
  let box = document.getElementById('powerLab');
  if (box) box.remove();
  box = document.createElement('div');
  box.id = 'powerLab';
  box.innerHTML = `
  <div style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.95);z-index:99999;padding:20px;overflow:auto">
    <div style="display:flex;justify-content:space-between"><h2 style="color:#00ff88">⚡ DZIVISA POWER LAB v12</h2><button onclick="document.getElementById('powerLab').remove()" style="padding:8px 16px;background:#ff3333;color:white;border:none;border-radius:6px">✖ CLOSE</button></div>
    <select id="langSelect" style="padding:10px;width:100%;margin:10px 0;background:#222;color:#fff;border:1px solid #444;border-radius:6px"><option value="javascript">JavaScript</option><option value="python">Python</option></select>
    <textarea id="powerCode" style="width:100%;height:220px;background:#050505;color:#0f0;padding:12px;font-family:monospace"># Dzivisa example
text = "EcoCash OTP 1234"
triggers = ["ecocash","otp","pin"]
print("SCAM!" if any(t in text.lower() for t in triggers) else "Safe")
</textarea>
    <button onclick="executePower()" style="width:100%;padding:14px;background:#00ff88;color:#000;font-weight:bold;margin-top:10px;border:none;border-radius:8px">▶ RUN</button>
    <pre id="powerOutput" style="background:#000;color:#fff;padding:12px;min-height:100px;margin-top:10px"></pre>
  </div>`;
  document.body.appendChild(box);
}
async function executePower(){
  const code=document.getElementById('powerCode').value;
  const out=document.getElementById('powerOutput');
  out.textContent="Running...";
  const res=await runPowerCode(document.getElementById('langSelect').value, code);
  out.textContent=res.ok?res.result:"ERROR: "+res.error;
}
