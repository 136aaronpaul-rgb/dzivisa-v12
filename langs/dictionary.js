const DZIVISA_LOCALES = {
  "sn": { flag:"🇿🇼", name:"Shona", uiScan: "🚨 SCAN + AUDIO", uiClear: "🗑 TSVAGURUDZA", alert: "🚨 CHENJEDZO", advice: "Usatumira PIN kana mari. Fona munhu wacho.", safe: "✅ Kwakachengeteka", speed: "Nguva" },
  "nd": { flag:"🇿🇼", name:"Ndebele", uiScan: "🚨 HLOLA + AUDIO", uiClear: "🗑 SUSA YONKE", alert: "🚨 LINYELIWE", advice: "Ungathumeli i-PIN loba imali. Fona lowomuntu.", safe: "✅ Kulungile", speed: "Isikhathi" },
  "en": { flag:"🇬🇧", name:"English", uiScan: "🚨 SCAN + AUDIO", uiClear: "🗑 CLEAR", alert: "🚨 CRITICAL THREAT", advice: "Do not send PIN or money. Voice verify.", safe: "✅ Secure", speed: "Latency" },
  "zu": { flag:"🇿🇦", name:"Zulu", uiScan: "🚨 Skena", uiClear: "🗑 Susa", alert: "🚨 SIVIKELO", advice: "Ungathumeli i-PIN noma imali.", safe: "✅ Kuphephile", speed: "Isikhathi" },
  "xh": { flag:"🇿🇦", name:"Xhosa", uiScan: "🚨 Skena", uiClear: "🗑 Susa", alert: "🚨 ISILUMKISO", advice: "Ungathumeli PIN okanye imali.", safe: "✅ Khuselekile", speed: "Ixesha" },
  "af": { flag:"🇿🇦", name:"Afrikaans", uiScan: "🚨 SKANDEER", uiClear: "🗑 MAAK SKOON", alert: "🚨 KRITIEKE BEDREIGING", advice: "Moenie PIN of geld stuur nie.", safe: "✅ Veilig", speed: "Latensie" },
  "sw": { flag:"🇹🇿", name:"Swahili", uiScan: "🚨 TAHADHARI", uiClear: "🗑 SAFISHA", alert: "🚨 TAHADHARI KUU", advice: "Usitume PIN au pesa.", safe: "✅ Salama", speed: "Muda" },
  "pt": { flag:"🇵🇹", name:"Portuguese", uiScan: "🚨 ESCANEAR", uiClear: "🗑 LIMPAR", alert: "🚨 AMEAÇA CRÍTICA", advice: "Não envie PIN ou dinheiro.", safe: "✅ Seguro", speed: "Latência" },
  "fr": { flag:"🇫🇷", name:"Français", uiScan: "🚨 ANALYSER", uiClear: "🗑 EFFACER", alert: "🚨 MENACE CRITIQUE", advice: "N'envoyez pas de PIN ni d'argent.", safe: "✅ Sûr", speed: "Latence" },
  "es": { flag:"🇪🇸", name:"Español", uiScan: "🚨 ESCANEAR", uiClear: "🗑 LIMPIAR", alert: "🚨 ALERTA CRÍTICA", advice: "No envíes PIN ni dinero.", safe: "✅ Seguro", speed: "Latencia" },
  "zh": { flag:"🇨🇳", name:"中文", uiScan: "🚨 扫描", uiClear: "🗑 清除", alert: "🚨 严重威胁", advice: "不要发送密码或钱款。", safe: "✅ 安全", speed: "延迟" },
  "ar": { flag:"🇸🇦", name:"العربية", uiScan: "🚨 فحص", uiClear: "🗑 مسح", alert: "🚨 تهديد خطير", advice: "لا ترسل الرقم السري أو الأموال.", safe: "✅ آمن", speed: "استجابة" },
  "hi": { flag:"🇮🇳", name:"हिन्दी", uiScan: "🚨 स्कैन", uiClear: "🗑 साफ", alert: "🚨 खतरा", advice: "पिन या पैसे न भेजें।", safe: "✅ सुरक्षित", speed: "विलंब" },
  "de": { flag:"🇩🇪", name:"Deutsch", uiScan: "🚨 SCANNEN", uiClear: "🗑 LÖSCHEN", alert: "🚨 KRITISCH", advice: "Senden Sie keine PIN oder Geld.", safe: "✅ Sicher", speed: "Latenz" },
  "ny": { flag:"🇲🇼", name:"Chichewa", uiScan: "🚨 JAMBULANI", uiClear: "🗑 CHOTSANI", alert: "🚨 NGOZI", advice: "Musatumize PIN kapena ndalama.", safe: "✅ Otetezeka", speed: "Nthawi" },
  "st": { flag:"🇱🇸", name:"Sesotho", uiScan: "🚨 HLahloba", uiClear: "🗑 Hlakola", alert: "🚨 KOTSI", advice: "Se romele PIN kapa chelete.", safe: "✅ Sireletsehile", speed: "Nako" },
  "tn": { flag:"🇧🇼", name:"Setswana", uiScan: "🚨 SEKASEKA", uiClear: "🗑 HLAKOLA", alert: "🚨 KOTSI", advice: "Se romele PIN kgotsa madi.", safe: "✅ Sireletsegile", speed: "Nako" },
  "ts": { flag:"🇿🇦", name:"Tsonga", uiScan: "🚨 KAMBELA", uiClear: "🗑 SUSA", alert: "🚨 NGOZI", advice: "U nga rhumeli PIN kumbe mali.", safe: "✅ Sirhelelekile", speed: "Nkarhi" }
};
// Fill to 65 with proper flags
const extra = [
  ["yo","🇳🇬","Yoruba"],["ig","🇳🇬","Igbo"],["ha","🇳🇬","Hausa"],["am","🇪🇹","Amharic"],["so","🇸🇴","Somali"],
  ["om","🇪🇹","Oromo"],["rw","🇷🇼","Kinyarwanda"],["lg","🇺🇬","Luganda"],["ak","🇬🇭","Akan"],["tw","🇬🇭","Twi"],
  ["wo","🇸🇳","Wolof"],["bm","🇲🇱","Bambara"],["it","🇮🇹","Italiano"],["nl","🇳🇱","Nederlands"],["tr","🇹🇷","Türkçe"],
  ["pl","🇵🇱","Polski"],["uk","🇺🇦","Українська"],["ro","🇷🇴","Română"],["el","🇬🇷","Ελληνικά"],["cs","🇨🇿","Čeština"],
  ["sv","🇸🇪","Svenska"],["hu","🇭🇺","Magyar"],["bg","🇧🇬","Български"],["hr","🇭🇷","Hrvatski"],["da","🇩🇰","Dansk"],
  ["fi","🇫🇮","Suomi"],["sk","🇸🇰","Slovenčina"],["no","🇳🇴","Norsk"],["lt","🇱🇹","Lietuvių"],["lv","🇱🇻","Latviešu"],
  ["et","🇪🇪","Eesti"],["sl","🇸🇮","Slovenščina"],["ga","🇮🇪","Gaeilge"],["mt","🇲🇹","Malti"],["cy","🏴󠁧󠁢󠁷󠁬󠁳󠁿","Cymraeg"],
  ["bn","🇧🇩","বাংলা"],["ur","🇵🇰","اردو"],["pa","🇮🇳","ਪੰਜਾਬੀ"],["jv","🇮🇩","Jawa"],["vi","🇻🇳","Tiếng Việt"],
  ["te","🇮🇳","తెలుగు"],["mr","🇮🇳","मराठी"],["ta","🇮🇳","தமிழ்"],["fa","🇮🇷","فارسی"],["ps","🇦🇫","پښتو"],
  ["ml","🇮🇳","മലയാളം"],["kn","🇮🇳","ಕನ್ನಡ"],["th","🇹🇭","ไทย"],["he","🇮🇱","עברית"],["ja","🇯🇵","日本語"],
  ["ko","🇰🇷","한국어"],["ru","🇷🇺","Русский"]
];
extra.forEach(([code,flag,name])=>{
  if(!DZIVISA_LOCALES[code]) DZIVISA_LOCALES[code] = { flag, name, uiScan: DZIVISA_LOCALES["en"].uiScan, uiClear: DZIVISA_LOCALES["en"].uiClear, alert: DZIVISA_LOCALES["en"].alert, advice: DZIVISA_LOCALES["en"].advice, safe: DZIVISA_LOCALES["en"].safe, speed: DZIVISA_LOCALES["en"].speed };
});
console.log("DZIVISA 65 langs loaded:", Object.keys(DZIVISA_LOCALES).length);
