function dzivisaScan(text) {
  if (!text || !text.trim()) {
    return [{
      risk: "INFO",
      title: "Empty",
      advice: "Paste message",
      analytics: ""
    }];
  }

  const lower = text.toLowerCase().replace(/\s+/g, " ").trim();

  let extractedCash =
    text.match(/(?:\$|zig|usd|rtgs)\s*\d+[\d,.]*|\d+[\d,.]*\s*(?:\$|zig|usd|rtgs|mari|pin)/i);

  let extractedPhones =
    text.match(/(?:077|078|071|\+263)\s*\d+[\d\s-]{5,}/g);

  let analyticsContext = "";

  if (extractedCash) {
    analyticsContext += `💰 TARGET: ${extractedCash[0].toUpperCase()} `;
  }

  if (extractedPhones) {
    analyticsContext += `📱 SOURCE: ${extractedPhones.join(", ")}`;
  }

  if (!analyticsContext) {
    analyticsContext = "⚖️ NO RAW VECTOR EXPLOITS EXTRACTED";
  }

  const hasEcoCash = /\becocash\b/i.test(lower);
  const hasPin = /\bpin\b/i.test(lower);
  const hasOtp = /\botp\b|\bone[- ]time password\b/i.test(lower);

  const asksToSend =
    /\bsend\b|\btumira\b|\bshare\b|\bforward\b|\bgive\b|\bprovide\b/i.test(lower);

  if (hasEcoCash && hasPin && asksToSend) {
    return [{
      risk: "CRITICAL",
      title: "EcoCash PIN Request",
      advice: "Dzivisa: Usatumira mari kana kugovera PIN yako.",
      analytics: analyticsContext
    }];
  }

  if (hasEcoCash && hasOtp && asksToSend) {
    return [{
      risk: "CRITICAL",
      title: "EcoCash OTP Request",
      advice: "Dzivisa: Usagovera OTP yako.",
      analytics: analyticsContext
    }];
  }

  if (
    /\bwhatsapp\b/i.test(lower) &&
    /\bverification\b|\bverify\b/i.test(lower) &&
    /\bcode\b|\botp\b/i.test(lower) &&
    asksToSend
  ) {
    return [{
      risk: "CRITICAL",
      title: "WhatsApp Verification Code Scam",
      advice: "Never share a WhatsApp verification code.",
      analytics: analyticsContext
    }];
  }

  if (typeof ZIM_FRAUD_DB !== "undefined") {

    for (const x of ZIM_FRAUD_DB) {
      if (
        x.risk === "CRITICAL" &&
        x.pattern instanceof RegExp &&
        x.pattern.test(text)
      ) {
        return [{
          ...x,
          analytics: analyticsContext
        }];
      }
    }

    for (const x of ZIM_FRAUD_DB) {
      if (
        x.pattern instanceof RegExp &&
        x.pattern.test(text)
      ) {
        return [{
          ...x,
          analytics: analyticsContext
        }];
      }
    }
  }

  return [{
    risk: "SAFE",
    title: "Safe",
    advice: "No fraud found",
    analytics: analyticsContext
  }];
}
