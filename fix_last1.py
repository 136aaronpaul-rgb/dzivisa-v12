import pathlib
p=pathlib.Path("index.html")
h=p.read_text(encoding='utf-8')
h=h.replace('"overpayment"', '"overpaid","overpayment","send back difference","send back"')
p.write_text(h,encoding='utf-8')
print("FIXED LAST 1!")
