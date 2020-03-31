n = int(input())
s = list(input())
a = 0
for i in range(n):
    s[i] = int(s[i])
    a += s[i]
print(a)