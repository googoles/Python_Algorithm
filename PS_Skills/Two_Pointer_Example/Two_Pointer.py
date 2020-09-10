# Two Pointer Practice

def Tn(n):
    return n*(n-1)/2

def Pn(n):
    return n*(3*n-1)/2

def Hn(n):
    return n*(2*n-1)

tp = 286
pp = 166
hp = 144

while not (Tn(tp) == Pn(pp) and Pn(pp) == Hn(hp)):
    T = Tn(tp)
    P = Pn(pp)
    H = Hn(hp)

    if T <= P and T <= H:
        tp += 1
    elif P <= T and P <= H:
        pp += 1
    else:
        hp += 1

print(Tn(tp))
print(Pn(pp))
print(Hn(hp))
