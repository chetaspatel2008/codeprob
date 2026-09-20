n = int(input())
txt = input()
 
ha = "A" in txt or "a" in txt
hb = "B" in txt or "b" in txt
hc = "C" in txt or "c" in txt
hd = "D" in txt or "d" in txt
he = "E" in txt or "e" in txt
hf = "F" in txt or "f" in txt
hg = "G" in txt or "g" in txt
hh = "H" in txt or "h" in txt
hi = "I" in txt or "i" in txt
hj = "J" in txt or "j" in txt
hk = "K" in txt or "k" in txt
hl = "L" in txt or "l" in txt
hm = "M" in txt or "m" in txt
hn = "N" in txt or "n" in txt
ho = "O" in txt or "o" in txt
hp = "P" in txt or "p" in txt
hq = "Q" in txt or "q" in txt
hr = "R" in txt or "r" in txt
hs = "S" in txt or "s" in txt
ht = "T" in txt or "t" in txt
hu = "U" in txt or "u" in txt
hv = "V" in txt or "v" in txt
hw = "W" in txt or "w" in txt
hx = "X" in txt or "x" in txt
hy = "Y" in txt or "y" in txt
hz = "Z" in txt or "z" in txt
 
if n == len(txt):
    if (ha) and (hb) and (hc) and (hd) and (he) and (hf) and (hg) and (hh) and (hi) and (hj) and (hk) and (hl) and (hm) and (hn) and (ho) and (hp) and (hq) and (hr) and (hs) and (ht) and (hu) and (hv) and (hw) and (hx) and (hy) and (hz) :
        print("YES")
    else:
        print("NO")