function dzivisaScan(text){
  if(!text.trim()) return [{risk:"INFO",title:"Empty",advice:"Paste message", analytics:""}];
  
  // 1. ADVANCED HEURISTIC ANALYSIS (Extracts Currency & Fraud Target Phone Profiles)
  let extractedCash = text.match(/(?:\$|zig|usd|rtgs)\s*\d+[\d,.]*|\d+[\d,.]*\s*(?:\$|zig|usd|rtgs|mari|pin)/i);
  let extractedPhones = text.match(/(?:077|078|071|\+263)\s*\d+[\d\s-]{5,}/g);
  
  let analyticsContext = "";
  if (extractedCash) {
    analyticsContext += `💰 TARGET: ${extractedCash.toUpperCase()} `;
  }
  if (extractedPhones) {
    analyticsContext += `📱 SOURCE: ${extractedPhones.join(', ')}`;
  }
  if (!analyticsContext) {
    analyticsContext = "⚖️ NO RAW VECTOR EXPLOITS EXTRACTED";
  }

  // 2. Scan for CRITICAL rules first (PINs, OTPs, Link Phishing)
  for(let x of ZIM_FRAUD_DB) {
    if(x.risk === "CRITICAL" && x.pattern.test(text)) {
      x.analytics = analyticsContext;
      return [x];
    }
  }
  
  // 3. Scan for HIGH rules if no critical signatures matched
  for(let x of ZIM_FRAUD_DB) {
    if(x.pattern.test(text)) {
      x.analytics = analyticsContext;
      return [x];
    }
  }
  
  return [{risk:"SAFE",title:"Safe",advice:"No fraud found", analytics: analyticsContext}];
}
