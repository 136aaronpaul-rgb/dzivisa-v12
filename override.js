// V25.2 AQUA - FULL WORKING ENGINE - FIXED
console.log("🔒 V25.2 AQUA FULL WORKING");

if (typeof ZIM_FRAUD_DB!== 'undefined') {
  window.ZIM_FRAUD_DB = ZIM_FRAUD_DB;
  window.vectors = ZIM_FRAUD_DB;
  console.log("✅ Database loaded:", ZIM_FRAUD_DB.length, "patterns");
}

function fixApp() {
  // Fix scan button
  const scanBtn = document.querySelector('[onclick*="scan"]') || document.getElementById('scanBtn') || document.querySelector('button');
  const input = document.querySelector('textarea') || document.querySelector('input[type="text"]') || document.getElementById('msgInput');
  const result = document.getElementById('result') || document.querySelector('.result') || document.getElementById('output');

  if (scanBtn && input) {
    scanBtn.onclick = function() {
      const text = input.value;
      console.log("Scanning:", text);
      const res = window.dzivisaScan(text);
      if (result) {
        result.innerHTML = `<div style="padding:12px;border:2px solid ${res[0].risk==='CRITICAL'?'red':'#4DD0E1'};border-radius:10px;margin:10px 0">
          <b style="color:${res[0].risk==='CRITICAL'?'red':'#4DD0E1'}">${res[0].risk}: ${res[0].title}</b><br>
          <div style="margin:8px 0">${res[0].advice}</div>
          <small>${res[0].analytics}</small>
        </div>`;
        result.style.display = 'block';
      } else {
        alert(res[0].risk + ": " + res[0].title + "\n" + res[0].advice);
      }
    };
    console.log("✅ Scan button FIXED");
  }

  // Fix moving bar
  const ticker = document.getElementById('tickerText');
  if (ticker) {
    ticker.style.whiteSpace = 'nowrap';
    ticker.style.animation = 'scroll-left 25s linear infinite';
  }
}

setInterval(fixApp, 800);
setTimeout(fixApp, 1000);

window.dzivisaScan = window.dzivisaScan || function(t) {
  if(typeof ZIM_FRAUD_DB!== 'undefined') {
    for(const x of ZIM_FRAUD_DB) {
      if(x.pattern && x.pattern.test(t)) return [x];
    }
  }
  return [{risk:"SAFE", title:"Safe", advice:"No scam", analytics:"✅"}];
};
window.scanMessage = window.dzivisaScan;
