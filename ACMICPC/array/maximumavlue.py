import sys
# numbers = list(map(int, sys.stdin.readline().split()))
maxn = 0
maxi = 0
for i in range(9):
    a = int(sys.stdin.readline())
    if a > maxn:
        maxn = a
        maxi = i+1
    # else:
    #     maxn = numbers[i]
    #     maxi = i
print(maxn)
print(maxi)