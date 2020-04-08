import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(n):
    cnt_1 = 1
    for j in range(1,numbers[i]):
        if numbers[i]%j == 0:
            cnt_1 += 1
    if cnt_1 == 2:
        cnt += 1
        cnt_1 = 0
print(cnt)

# print(numbers)