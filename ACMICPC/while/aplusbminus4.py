import sys
while True:
    try:
        a,b = list(map(int, sys.stdin.readline().split()))

    except:
        break
    print(a+b)