import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

engine = """
<script>
// DZIVISA V26 - 100 TACTICS ENGINE - CATCHES ALL WORLD SCAMS
const SCAM_100 = [
  {k:["pin","send"], s:100, r:"PIN request=100% SCAM - EcoCash NEVER asks PIN"},
  {k:["otp","send"], s:100, r:"OTP request=100% SCAM"},
  {k:["password","send"], s:100, r:"Password request=100% SCAM"},
  {k:["yemahara"], s:100, r:"YEMAHARA=100% SCAM"},
  {k:["kumbira"], s:100, r:"Kumbira hama=100% SCAM"},
  {k:["kumbira shamwari"], s:100, r:"Kumbira shamwari=SCAM"},
  {k:["*121*"], s:100, r:"Airtime code *121*=SCAM"},
  {k:["*123*"], s:100, r:"Data code *123*=SCAM"},
  {k:["*151*"], s:100, r:"EcoCash code trick=SCAM"},
  {k:["mom","new number","send"], s:100, r:"Mom new number scam"},
  {k:["baba","tumira"], s:100, r:"Baba emergency scam"},
  {k:["amai","tumira"], s:100, r:"Amai emergency scam"},
  {k:["child","accident","send"], s:100, r:"Child accident scam"},
  {k:["muchipatara","tumira"], s:100, r:"Hospital trick scam"},
  {k:["ndabirwa","tumira"], s:100, r:"Ndabirwa trick"},
  {k:["ndiri muchipatara"], s:100, r:"Fake hospital scam"},
  {k:["double","ecocash"], s:100, r:"Double money=SCAM"},
  {k:["2x","back"], s:100, r:"2x back=SCAM"},
  {k:["uwane 2x"], s:100, r:"Uwane 2x=SCAM"},
  {k:["won","pin"], s:100, r:"Won+PIN=SCAM"},
  {k:["congratulations","pin"], s:100, r:"Congrats+PIN=SCAM"},
  {k:["congratulations","click"], s:100, r:"Congrats+link=SCAM"},
  {k:["prize","fee"], s:100, r:"Prize+fee=SCAM"},
  {k:["lottery","fee"], s:100, r:"Lottery fee=SCAM"},
  {k:["bit.ly"], s:90, r:"bit.ly link=90% SCAM"},
  {k:["rbz","release"], s:100, r:"RBZ release fee=SCAM"},
  {k:["rbz","send"], s:100, r:"RBZ trick=SCAM"},
  {k:["job","registration fee"], s:100, r:"Job fee=SCAM"},
  {k:["job","send money"], s:100, r:"Job money=SCAM"},
  {k:["un job","pay"], s:100, r:"UN job fee=SCAM"},
  {k:["ngo","pin"], s:100, r:"NGO+PIN=SCAM"},
  {k:["ngo cash"], s:100, r:"NGO cash=SCAM"},
  {k:["whatsapp","delete","click"], s:100, r:"WhatsApp delete scam"},
  {k:["whatsapp-verify"], s:100, r:"Fake WhatsApp link=SCAM"},
  {k:["account blocked","pin"], s:100, r:"Account blocked+PIN=SCAM"},
  {k:["line will be blocked"], s:100, r:"Line blocked=SCAM"},
  {k:["suspicious activity","send"], s:100, r:"Suspicious+send=SCAM"},
  {k:["verify","pin"], s:100, r:"Verify+PIN=SCAM"},
  {k:["handling fee"], s:100, r:"Handling fee=SCAM"},
  {k:["processing fee"], s:100, r:"Processing fee=SCAM"},
  {k:["release fee"], s:100, r:"Release fee=SCAM"},
  {k:["customs fee"], s:100, r:"Customs fee=SCAM"},
  {k:["secret loan"], s:100, r:"Secret loan=SCAM"},
  {k:["instant loan","fee"], s:100, r:"Loan fee=SCAM"},
  {k:["get $500 instantly"], s:100, r:"Instant $500=SCAM"},
  {k:["invest","double"], s:95, r:"Invest double=SCAM"},
  {k:["10x","return"], s:95, r:"10x return=SCAM"},
  {k:["forex","double"], s:95, r:"Forex double=SCAM"},
  {k:["crypto","double"], s:95, r:"Crypto double=SCAM"},
  {k:["romance","ticket"], s:90, r:"Romance ticket=SCAM"},
  {k:["inheritance"], s:95, r:"Inheritance=SCAM"},
  {k:["overpayment"], s:90, r:"Overpayment=SCAM"},
  {k:["wrong transfer","send back"], s:90, r:"Wrong transfer trick"},
  {k:["tuma mari"], s:85, r:"Tuma mari - verify!"},
  {k:["tumira","$"], s:80, r:"Tumira $ - verify!"},
  {k:["send money now"], s:85, r:"Send money now=check"},
  {k:["pay now","claim"], s:90, r:"Pay now to claim=SCAM"},
  {k:["free netone"], s:100, r:"Free NetOne=SCAM"},
  {k:["free econet","data"], s:100, r:"Free Econet=SCAM"},
  {k:["free telecel"], s:100, r:"Free Telecel=SCAM"},
  {k:["click","claim"], s:85, r:"Click to claim=SCAM"},
  {k:["system upgrade","pin"], s:100, r:"System upgrade PIN=SCAM"},
  {k:["ecocash upgrade"], s:90, r:"EcoCash upgrade trick"},
  {k:["ecocash blocked"], s:90, r:"EcoCash blocked trick"},
  {k:["send to 1144"], s:100, r:"Send to 1144=SCAM"},
  {k:["send to 12345"], s:100, r:"Send to shortcode=SCAM"},
  {k:["tender fee"], s:95, r:"Tender fee=SCAM"},
  {k:["gold deal"], s:90, r:"Gold deal=SCAM"},
  {k:["fuel cheap","send"], s:90, r:"Cheap fuel=SCAM"},
  {k:["hospital bill","ecocash"], s:100, r:"Hospital bill scam"},
  {k:["police bail"], s:100, r:"Police bail scam"},
  {k:["arrested","send money"], s:100, r:"Arrested scam"},
  {k:["kidnapped","send"], s:100, r:"Kidnapped scam"},
  {k:["send airtime"], s:80, r:"Send airtime verify"},
  {k:["100% guaranteed","double"], s:100, r:"100% guaranteed double=SCAM"},
  {k:["risk free","invest"], s:95, r:"Risk free invest=SCAM"},
  {k:["make money fast"], s:90, r:"Make money fast=SCAM"},
  {k:["work from home","fee"], s:90, r:"Work from home fee=SCAM"},
  {k:["pyramid"], s:95, r:"Pyramid=SCAM"},
  {k:["forward to 10"], s:100, r:"Chain forward=SCAM"},
  {k:["share to","groups","$"], s:100, r:"Share to groups $=SCAM"},
  {k:["tumira meseji","10"], s:100, r:"Tumira meseji kuvanhu 10=SCAM"},
  {k:["limited offer","send"], s:85, r:"Limited offer+send=SCAM"},
  {k:["act now","send"], s:85, r:"Act now+send=SCAM"},
  {k:["last chance","send"], s:85, r:"Last chance+send=SCAM"},
  {k:["you have been selected"], s:90, r:"You selected=SCAM bait"},
  {k:["dear customer","pin"], s:100, r:"Dear customer+PIN=SCAM"},
  {k:["dear beneficiary"], s:90, r:"Dear beneficiary=SCAM"},
  {k:["atm card blocked"], s:100, r:"ATM blocked=SCAM"},
  {k:["visa blocked","pin"], s:100, r:"VISA blocked+PIN=SCAM"},
  {k:["account hacked","send"], s:100, r:"Hacked+send=SCAM"},
  {k:["reset password","click"], s:80, r:"Reset link check domain!"},
  {k:["confirm identity","pin"], s:100, r:"Confirm identity+PIN=SCAM"},
  {k:["kyc","pin"], s:100, r:"KYC+PIN=SCAM"},
  {k:["zimra refund","pin"], s:100, r:"ZIMRA+PIN=SCAM"},
  {k:["zesa token","fee"], s:90, r:"ZESA token fee=SCAM"},
  {k:["transfer confirmation","password"], s:100, r:"Transfer+password=SCAM"},
];

function SCAN_100(msg){
  if(!msg || msg.trim().length<2) return {score:0, reasons:"Empty", tactic:"None"};
  var lower = msg.toLowerCase();
  var best = {score:0, reasons:"SAFE - No scam found", tactic:"SAFE"};
  // Check protection link - make it SAFE
  if(lower.includes("dzivisa-v12.surge.sh") && lower.includes("protected inside")) return {score:10, reasons:"Your own app link - SAFE", tactic:"SAFE"};

  for(var i=0;i<SCAM_100.length;i++){
    var rule = SCAM_100[i];
    var match = true;
    for(var j=0;j<rule.k.length;j++){
      if(!lower.includes(rule.k[j])){ match=false; break; }
    }
    if(match && rule.s > best.score){
      best = {score:rule.s, reasons:rule.r, tactic:rule.k.join("+")};
      if(best.score===100) break;
    }
  }
  // Extra: short message with $ + send = suspicious
  if(best.score<80 && lower.includes("send") && lower.includes("$") && msg.length<150){
    best = {score:85, reasons:"Short send $ message - VERIFY CALLER!", tactic:"send+$"};
  }
  return best;
}
window.SCAN_100 = SCAN_100;
window.scanMessage = function(msg){
  var r = SCAN_100(msg);
  return {score:r.score, reasons:r.reasons};
};
console.log("DZIVISA V26 - 100 TACTICS LOADED!");
</script>
"""

# Remove old engines
import re
h = re.sub(r'<script>.*?dzivisaScanREAL.*?</script>', '', h, flags=re.DOTALL)
h = re.sub(r'<script>.*?SCAN_100.*?</script>', '', h, flags=re.DOTALL)

h = h.replace('</body>', engine + '</body>')
p.write_text(h, encoding='utf-8')
print("100 TACTICS ADDED!")
