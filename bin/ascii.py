

def rtext(txt):
    for t in txt:
        yield t

for r in rtext("killercodes"):
    asci = ord(r)
    hcod = hex(ord(r))
    ncode = chr(int(hcod.replace("0x",""),16))
    print(r,ord(r),hcod,hcod.replace("0x",""),ncode)
