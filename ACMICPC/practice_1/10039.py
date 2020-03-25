a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


if a < 40:
    a = 40
if b < 40:
    b = 40
if c < 40:
    c = 40
if d < 40:
    d = 40
if e < 40:
    e = 40

score = [a,b,c,d,e]
avg = sum(score)/5

print(int(avg))