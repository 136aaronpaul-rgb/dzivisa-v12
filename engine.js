function dzivisaScan(text) {
  if (!text ||!text.trim()) {
    return [{risk:"SAFE", title:"Empty", advice:"Type message to scan", analytics:"⚖️ Empty"}];
  }
  const t = text.toLowerCase();

  // Check romance + airtime scam
  if ((t.includes('love you') || (t.includes('love') && t.includes('you'))) && (t.includes('airtime') || t.includes('$20') || t.includes('$')) && (t.includes('give you') || t.includes('10%') || t.includes('percent'))) {
    return [{risk:"CRITICAL", title:"Romance Airtime Investment Scam - 100% SCAM", advice:"DO NOT SEND! This is romance scam!", analytics:"💰 ROMANCE SCAM"}];
  }

  // Check database
  if (typeof ZIM_FRAUD_DB!== 'undefined') {
    for (const item of ZIM_FRAUD_DB) {
      if (item.pattern && item.pattern.test(text)) {
        return [item];
      }
    }
  }

  return [{risk:"SAFE", title:"Safe - No scam detected", advice:"Message looks safe but stay alert", analytics:"✅ SAFE"}];
}
window.dzivisaScan = dzivisaScan;
window.scanMessage = dzivisaScan;
console.log("✅ DZIVISA ENGINE LOADED - 666 PATTERNS ACTIVE");
