function dzivisaScan(text){
  if(!text.trim()) return [{risk:"INFO",title:"Empty",advice:"Paste message"}];
  
  // 1. Scan for CRITICAL rules first (PINs, OTPs, Link Phishing)
  for(let x of ZIM_FRAUD_DB) {
    if(x.risk === "CRITICAL" && x.pattern.test(text)) {
      return [x];
    }
  }
  
  // 2. Scan for HIGH rules if no critical signatures matched
  for(let x of ZIM_FRAUD_DB) {
    if(x.pattern.test(text)) {
      return [x];
    }
  }
  
  return [{risk:"SAFE",title:"Safe",advice:"No fraud found"}];
}
