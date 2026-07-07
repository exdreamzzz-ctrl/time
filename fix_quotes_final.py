import sys
sys.stdout.reconfigure(encoding="utf-8")
with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()
q = chr(39)
d = chr(45) * 2
old = q + q + d + q + q
new = q + d + q
if old in c:
    c = c.replace(old, new)
    print("Fixed ''--'' --> '--'")
else:
    print("''--'' NOT found")
    # Check what's there instead
    idx = c.find(chr(45)+chr(45))
    if idx >= 0:
        print("Found -- at", idx, ":", repr(c[idx-10:idx+20]))
with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Done")
