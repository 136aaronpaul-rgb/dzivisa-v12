function generateViralAlert(text,title,risk){
  let c=document.getElementById('viral-share-container'); if(!c) return;
  let msg=`🚨 DZIVISA ALERT 🚨\n⚠️ ${title}\nRisk: ${risk}\n\nScam: "${text}"\n\nScan FREE: https://dzivisa-v12.surge.sh`;
  c.innerHTML=`<button onclick="window.open('https://wa.me/?text=${encodeURIComponent(msg)}','_blank')" style="width:100%;padding:16px;background:#25D366;color:white;border:none;border-radius:12px;font-weight:900;margin-top:10px">📢 SHARE TO WHATSAPP</button>`;
}
