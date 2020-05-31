
a = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        a.pop()
    else:
        a.append(num)
print(sum(a))