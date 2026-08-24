# DZIVISA 100 TACTICS TESTER - Termux

SCAM_100 = [
  ("EcoCash: Send your PIN 1234 to unlock", "PIN request"),
  ("Your OTP is 1234, send to 071xxx to verify", "OTP request"),
  ("Send your password to secure account", "Password request"),
  ("YEMAHARA $50 click here!", "YEMAHARA"),
  ("Kumbira hama *121*077...*50#", "Kumbira hama"),
  ("Kumbira shamwari uwane data", "Kumbira shamwari"),
  ("Dial *121*077123*50# free airtime", "Airtime code *121*"),
  ("Dial *123*077...*10GB#", "Data code *123*"),
  ("Dial *151*...", "EcoCash code trick"),
  ("Hi it's Mom. New number. Please send $100", "Mom new number"),
  ("Ndini baba vako, tumira $50 nekukurumidza", "Baba emergency"),
  ("Ndini amai vako tumira $30", "Amai emergency"),
  ("Your child has accident send $150 urgently!", "Child accident"),
  ("Ndiri muchipatara tumira mari", "Muchipatara trick"),
  ("Ndabirwa tumira $20 ndokudzorera", "Ndabirwa trick"),
  ("Ndiri muchipatara help", "Fake hospital"),
  ("Double your EcoCash 2x back now!", "Double money"),
  ("Tuma $10 uwane 2x back", "2x back"),
  ("Uwane 2x mari yako", "Uwane 2x"),
  ("You won $5000 send PIN to claim", "Won+PIN"),
  ("CONGRATULATIONS you won! PIN required", "Congrats+PIN"),
  ("CONGRATULATIONS click bit.ly/win5000", "Congrats+link"),
  ("You won prize pay fee $20", "Prize+fee"),
  ("Lottery won pay fee", "Lottery fee"),
  ("Click bit.ly/win5000", "bit.ly link"),
  ("RBZ your $10k ready pay release fee", "RBZ release fee"),
  ("I am from RBZ send $100", "RBZ trick"),
  ("Job Offer: Pay $20 registration fee UN job", "Job fee"),
  ("Pay $20 get job send money", "Job money"),
  ("UN job pay $20 registration", "UN job fee"),
  ("NGO cash send ID + PIN", "NGO+PIN"),
  ("NGO cash $300 selected", "NGO cash"),
  ("Your WhatsApp will be deleted click here", "WhatsApp delete"),
  ("Go to whatsapp-verify.com enter PIN", "Fake WhatsApp link"),
  ("EcoCash account blocked send PIN 1234", "Account blocked+PIN"),
  ("Your Econet line will be blocked today", "Line blocked"),
  ("Suspicious activity send password to secure", "Suspicious+send"),
  ("Verify your account PIN required", "Verify+PIN"),
  ("Pay handling fee $50 to claim car", "Handling fee"),
  ("Pay processing fee $20 loan", "Processing fee"),
  ("Pay release fee $100 RBZ", "Release fee"),
  ("Pay customs fee $30 parcel", "Customs fee"),
  ("Secret loan Get $500 instantly!", "Secret loan"),
  ("Instant loan pay fee $20", "Loan fee"),
  ("Get $500 instantly just send fee", "Instant $500"),
  ("Invest $100 double in 7 days", "Invest double"),
  ("10x return invest now", "10x return"),
  ("Forex double your money", "Forex double"),
  ("Crypto double in 24h", "Crypto double"),
  ("I love you send ticket money", "Romance ticket"),
  ("You inheritance $1M send fee", "Inheritance"),
  ("I overpaid send back difference", "Overpayment"),
  ("Wrong transfer sent $100 send back $50", "Wrong transfer"),
  ("Tuma mari ku 077...", "Tuma mari"),
  ("Tumira $50 ku 077...", "Tumira $"),
  ("Send money now to 077...", "Send money now"),
  ("Pay now to claim your prize", "Pay now to claim"),
  ("Free NetOne data 10GB", "Free NetOne"),
  ("Free Econet data YEMAHARA", "Free Econet"),
  ("Free Telecel airtime", "Free Telecel"),
  ("Click to claim your $1000", "Click to claim"),
  ("EcoCash system upgrade PIN to 1144", "System upgrade PIN"),
  ("EcoCash upgrade required", "EcoCash upgrade"),
  ("EcoCash blocked send PIN", "EcoCash blocked"),
  ("Send to 1144 to avoid block", "Send to 1144"),
  ("Send to 12345 to verify", "Send to shortcode"),
  ("Pay tender fee $50 to get tender", "Tender fee"),
  ("Gold deal cheap send $200", "Gold deal"),
  ("Fuel cheap $1 per litre send money", "Cheap fuel"),
  ("Hospital bill $150 send EcoCash 077...", "Hospital bill"),
  ("Police bail $100 needed send now", "Police bail"),
  ("Arrested send money for bail", "Arrested scam"),
  ("Kidnapped send $500 ransom", "Kidnapped scam"),
  ("Send airtime $10 to 077...", "Send airtime"),
  ("100% guaranteed double money", "100% guaranteed double"),
  ("Risk free invest get rich", "Risk free invest"),
  ("Make money fast $1000 per day", "Make money fast"),
  ("Work from home pay $20 fee", "Work from home fee"),
  ("Pyramid scheme invest", "Pyramid"),
  ("Forward to 10 people get $100", "Forward to 10"),
  ("Share to 5 groups get $100 EcoCash", "Share to groups"),
  ("Tumira meseji iyi kuvanhu 10 uwane $100", "Tumira meseji 10"),
  ("Limited offer send now", "Limited offer+send"),
  ("Act now send $20", "Act now+send"),
  ("Last chance send money today", "Last chance+send"),
  ("You have been selected for $300", "You selected"),
  ("Dear customer send your PIN", "Dear customer+PIN"),
  ("Dear beneficiary you won $10k", "Dear beneficiary"),
  ("ATM card blocked send PIN", "ATM blocked"),
  ("VISA blocked send PIN to verify", "VISA blocked+PIN"),
  ("Your account hacked send password", "Hacked+send"),
  ("Reset password click here", "Reset link"),
  ("Confirm identity send PIN", "Confirm identity+PIN"),
  ("KYC update send PIN", "KYC+PIN"),
  ("ZIMRA refund send PIN to claim", "ZIMRA+PIN"),
  ("ZESA token pay fee", "ZESA token fee"),
  ("Transfer Confirmation $1 reply password", "Transfer+password"),
]

def test_scan(msg):
    l = msg.lower()
    score = 0
    reason = "SAFE"
    checks = [
        (["pin","send"],100,"PIN request"),
        (["yemahara"],100,"YEMAHARA"),
        (["kumbira"],100,"Kumbira"),
        (["*121*"],100,"*121* code"),
        (["mom","new number","send"],100,"Mom scam"),
        (["baba","tumira"],100,"Baba scam"),
        (["double","ecocash"],100,"Double EcoCash"),
        (["2x","back"],100,"2x back"),
        (["won","pin"],100,"Won+PIN"),
        (["congratulations"],90,"Congrats scam"),
        (["bit.ly"],90,"bit.ly link"),
        (["job","fee"],100,"Job fee"),
        (["hospital","send"],100,"Hospital scam"),
        (["send","$"],80,"Send $"),
        (["tumira"],80,"Tumira money"),
    ]
    for keys, s, r in checks:
        if all(k in l for k in keys):
            if s > score:
                score = s
                reason = r
    if score==0 and "send" in l and "$" in l:
        score=85
        reason="Send $ - verify!"
    return score, reason

print("🔥 DZIVISA 100 TACTICS TEST - TERMUX")
print("="*50)
passed = 0
failed = 0
for i, (msg, expected) in enumerate(SCAM_100, 1):
    score, reason = test_scan(msg)
    status = "✅ CATCH" if score>=80 else "❌ MISS"
    if score>=80: passed+=1
    else: failed+=1
    print(f"{i:3}. {status} {score}% - {expected:25} | {msg[:40]}")

print("="*50)
print(f"RESULTS: {passed} CAUGHT / {len(SCAM_100)}")
print(f"FAILED: {failed}")
if failed==0:
    print("🎉 100% SCAM CATCHER - ALL 100 WORKING!")
else:
    print("⚠️ Fix needed for missed scams")
