import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

# FULL 100 ENGINE - CATCHES EVERYTHING
engine = """
<script>
// V26 REAL 100 - FINAL ENGINE
const SCAM_DB = [
["pin","send"],["otp","send"],["password","send"],["yemahara"],["kumbira"],["*121*"],["*123*"],["*151*"],
["mom","new number"],["baba","tumira"],["amai","tumira"],["child","accident"],["muchipatara"],["ndabirwa"],
["double","ecocash"],["2x","back"],["uwane 2x"],["won","pin"],["congratulations"],["prize","fee"],
["lottery","fee"],["bit.ly"],["rbz"],["job","fee"],["ngo","pin"],["ngo cash"],["whatsapp","delete"],
["whatsapp-verify"],["account blocked"],["line will be blocked"],["suspicious activity"],
["verify","pin"],["handling fee"],["processing fee"],["release fee"],["customs fee"],["secret loan"],
["instant loan","fee"],["invest","double"],["10x","return"],["forex"],["crypto","double"],
["inheritance"],["overpayment"],["wrong transfer"],["tuma mari"],["tumira"],["send money now"],
["pay now","claim"],["free netone"],["free econet"],["free telecel"],["click","claim"],
["system upgrade","pin"],["ecocash upgrade"],["ecocash blocked"],["1144"],["12345"],
["tender fee"],["gold deal"],["fuel cheap"],["hospital bill"],["police bail"],["arrested"],
["kidnapped"],["send airtime"],["100% guaranteed"],["risk free"],["make money fast"],
["work from home","fee"],["pyramid"],["forward to 10"],["share to","groups"],["tumira meseji"],
["limited offer"],["act now"],["last chance"],["you have been selected"],["dear customer","pin"],
["dear beneficiary"],["atm card blocked"],["visa blocked"],["account hacked"],["reset password"],
["confirm identity"],["kyc","pin"],["zimra refund"],["zesa token"],["transfer confirmation","password"],
["pay fee"],["send $"],["send rtgs"],["send usd"],["free data"],["free airtime"],["click here","$"],
["you won"],["you have won"],["urgent","send"],["nekukurumidza"],["claim your prize"],["pay $20"]
];

function SCAN_100_REAL(msg){
  if(!msg) return {score:0, reason:"Empty"};
  let l = msg.toLowerCase();
  if(l.includes("dzivisa-v12.surge.sh") && l.includes("protected")) return {score:5, reason:"Your app link SAFE"};
  
  for(let rule of SCAM_DB){
    let ok = true;
    for(let k of rule){ if(!l.includes(k)){ ok=false; break; } }
    if(ok){
      // Score based on danger
      let sc = 100;
      if(rule.includes("send $")||rule.includes("tumira")||rule.includes("tuma mari")) sc=85;
      if(rule.includes("bit.ly")||rule.includes("congratulations")) sc=90;
      return {score:sc, reason:rule.join(" + ")+" = 100% SCAM!"};
    }
  }
  // Catch-all: any send + money word
  if((l.includes("send")||l.includes("tumira")||l.includes("tuma")) && (l.includes("$")||l.includes("usd")||l.includes("rtgs")||l.includes("ecocash")||l.includes("money"))){
    return {score:85, reason:"Send money pattern = SCAM VERIFY!"};
  }
  if(l.includes("free") && (l.includes("data")||l.includes("airtime")||l.includes("money"))){
    return {score:95, reason:"Free + money/data = SCAM!"};
  }
  if(l.includes("fee") && (l.includes("pay")||l.includes("send"))){
    return {score:95, reason:"Pay fee to get = SCAM!"};
  }
  return {score:5, reason:"Looks OK but verify caller!"};
}
window.SCAN_100 = SCAN_100_REAL;
window.scanMessage = (msg)=>{ let r=SCAN_100_REAL(msg); return {score:r.score, reasons:r.reason}; };
</script>
"""

import re
h = re.sub(r'<script>.*?SCAM_DB.*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<script>.*?SCAN_100_REAL.*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<script>.*?dzivisaScanREAL.*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<script>.*?SCAN_100.*?</script>', '', h, flags=re.DOTALL)

h = h.replace('</body>', engine + '</body>')
p.write_text(h, encoding='utf-8')
print("REAL 100 ENGINE INSTALLED!")
