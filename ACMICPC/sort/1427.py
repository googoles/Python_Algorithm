
n = input()
print(n)
b = []
for _ in range(len(n)):
    b.append(int(n[_]))
b.sort(reverse=True)
for _ in range(len(b)):
    print(b[_])
