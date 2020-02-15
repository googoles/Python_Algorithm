import sys
n = int(sys.stdin.readline())
x = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if numbers[i] < x:
        print(numbers[i])
