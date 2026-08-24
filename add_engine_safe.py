import pathlib
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8', errors='ignore')

# Only add engine, DON'T touch scanner bar!
if "SCAN_100" not in h:
    engine = """<script>
const SCAM_100=[["pin","send"],["otp","send"],["password","send"],["yemahara"],["kumbira"],["*121*"],["*123*"],["*151*"],["mom","new number"],["baba","tumira"],["amai","tumira"],["child","accident"],["muchipatara"],["ndabirwa"],["double","ecocash"],["2x","back"],["won","pin"],["congratulations"],["prize","fee"],["lottery","fee"],["bit.ly"],["rbz"],["job","fee"],["ngo","pin"],["whatsapp","delete"],["account blocked"],["line will be blocked"],["suspicious activity"],["verify","pin"],["handling fee"],["processing fee"],["release fee"],["customs fee"],["secret loan"],["instant loan","fee"],["invest","double"],["10x","return"],["forex"],["crypto","double"],["inheritance"],["overpaid"],["send back"],["tuma mari"],["tumira"],["send money now"],["pay now","claim"],["free netone"],["free econet"],["free telecel"],["click","claim"],["system upgrade","pin"],["1144"],["12345"],["tender fee"],["gold deal"],["fuel cheap"],["hospital bill"],["police bail"],["arrested"],["kidnapped"],["send airtime"],["100% guaranteed"],["risk free"],["make money fast"],["work from home","fee"],["pyramid"],["forward to 10"],["share to","groups"],["tumira meseji"],["limited offer"],["act now"],["last chance"],["you have been selected"],["dear customer","pin"],["atm card blocked"],["visa blocked"],["account hacked"],["reset password"],["confirm identity"],["kyc","pin"],["zimra refund"],["transfer confirmation","password"]];
function SCAN_100(msg){let l=msg.toLowerCase();for(let rule of SCAM_100){if(rule.every(k=>l.includes(k)))return{score:100,reason:rule.join('+'),safe:false};} if((l.includes('send')||l.includes('tumira')||l.includes('tuma'))&&(l.includes('$')||l.includes('ecocash')||l.includes('money')))return{score:85,reason:'send+money',safe:false};if(l.includes('free')&&(l.includes('data')||l.includes('airtime')))return{score:95,reason:'free',safe:false};if(l.includes('fee')&&(l.includes('pay')||l.includes('send')))return{score:95,reason:'fee',safe:false};return{score:5,reason:'safe',safe:true};}
</script>"""
    h = h.replace('</head>', engine + '</head>')
    p.write_text(h, encoding='utf-8')
    print("Engine added safely - bar not touched!")
