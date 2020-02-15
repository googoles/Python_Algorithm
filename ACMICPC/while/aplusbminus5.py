import sys

while True:

    a,b = list(map(int, sys.stdin.readline().split()))
    if a == 0 or b == 0: break
    else:
        result = a+b
        print(result)