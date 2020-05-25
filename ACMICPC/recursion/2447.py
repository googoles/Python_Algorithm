
star = ['***','* *','***']
n = int(input())
count = 0

def stars(n):
    arr = []
    for i in range(3*len(n)):
        if i // len(n) == 1:
            arr.append(n[i % len(n)] + " "*len(n) + n[i%len(n)])
        else:
            arr.append(n[i%len(n)] * 3)
    return arr

while n != 3:
    n = int(n/3)
    count += 1

for i in range(count):
    star = stars(star)
for i in star:
    print(i)


