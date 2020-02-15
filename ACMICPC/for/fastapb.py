import sys # sys.stdin.readline() 을 사용하면 연산속도가 빨라진다.
n = int(sys.stdin.readline())
for i in range(n):
    a,b  = list(map(int, sys.stdin.readline().split()))
    print(a+b)
