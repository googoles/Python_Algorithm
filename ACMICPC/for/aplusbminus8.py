import sys
t = int(sys.stdin.readline())
for i in range(t):
    a,b  = list(map(int, sys.stdin.readline().split()))
    print("Case #%d: %d + %d = %d" % (i+1,a,b,a+b))
