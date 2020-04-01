# qr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'
t = int(input())
for i in range(t):
    a,b = input().split()
    te = ''
    for w in b:
        te += int(a)*w
    print(te)