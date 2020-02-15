import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
print(numbers[0])
print(numbers[n-1])

