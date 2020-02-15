import sys
t = int(sys.stdin.readline())
for i in range(1,t+1):
    for j in range(t,i,-1):
        print(" ", end = '')
    for k in range(0,i):
        print("*", end = '')
    print("\n")
