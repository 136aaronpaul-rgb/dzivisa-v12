import pathlib
p = pathlib.Path("index.html")
h = p.read_text(encoding='utf-8', errors='ignore')

code = '''
<script>
function dzivisaScanREAL(msg){
  if(!msg) return {score:0, reasons:"Empty"};
  var l = msg.toLowerCase();
  var s = 0; var r = [];
  if(l.includes("pin") && (l.includes("send")||l.includes("tuma"))){ s=100; r.push("PIN=100% SCAM!"); }
  if(l.includes("yemahara")||l.includes("kumbira")){ s=100; r.push("YEMAHARA=SCAM!"); }
  if((l.includes("urgent")||l.includes("nekukurumidza")) && l.includes("send")){ s=100; r.push("Urgent+send=SCAM!"); }
  if(l.includes("password")||l.includes("otp")){ s=100; r.push("Password OTP=SCAM!"); }
  if(l.includes("mom") && l.includes("new number") && l.includes("send")){ s=100; r.push("Family scam!"); }
  if(l.includes("baba") && l.includes("tumira")){ s=100; r.push("Baba scam!"); }
  if(l.includes("2x")||l.includes("double")&&l.includes("ecocash")){ s=100; r.push("Double money=SCAM!"); }
  if(l.includes("job")&&l.includes("fee")){ s=100; r.push("Job fee=SCAM!"); }
  if(l.includes("*121*")||l.includes("*123*")){ s=100; r.push("Airtime code=SCAM!"); }
  if(l.includes("send $")||l.includes("tumira")&&s<80){ s=80; r.push("Money request verify!"); }
  if(s==0){ s=5; r.push("Looks OK"); }
  return {score:s, reasons:r.join(" | ")};
}
window.scanMessage = dzivisaScanREAL;
</script>
'''

# add before </body>
h = h.replace('</body>', code + '</body>')
p.write_text(h, encoding='utf-8')
print("FIXED!")
