import pathlib
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8',errors='ignore')
code="""
<script id="SAFE_ZW">
(function(){
const ZW={1:'🇿🇼 MUTEMO - Zimbabwe Constitution',2:'🚗 Traffic Laws ZW - Mitemo Yemugwagwa',3:'👨‍👩‍👧 Family Law ZW',4:'🏠 Land Law ZW - Munda',5:'⚖️ Criminal Law ZW',6:'💼 Labour Law ZW',7:'💰 EcoCash Protection',8:'👮 Police Rights ZW',9:'🌍 World Laws - Diaspora',10:'📱 Cyber Law ZW'};
function nice(g){if(ZW[g])return ZW[g];let b=((g-1)%10)+1;let pt=Math.floor((g-1)/10)+1;return ZW[b]+' (Part '+pt+')';}
function rename(){document.querySelectorAll('#groupMenuList button').forEach((btn,i)=>{let g=i+1;let s=(g-1)*100+1;let e=g*100;if(btn.innerText.includes('MUTEMO'))return;btn.innerHTML='📦 '+nice(g)+'<br><small style="opacity:0.7;font-size:11px">'+s+' to '+e+' laws - All World + ZW</small> <span style="float:right;background:#4DD0E1;color:#000;padding:3px 10px;border-radius:10px;font-size:10px">🔒 OPEN</span>';});}
setInterval(rename,1000);
})();
</script>
<style id="SAFE_MSG">.msg-bar{ min-height:60px!important; padding:16px!important; font-size:16px!important; }</style>
"""
if 'SAFE_ZW' not in h:
    h=h.replace('</body>',code+'</body>')
    p.write_text(h,encoding='utf-8')
    print("SAFE FIX DONE - Groups NOT deleted!")
