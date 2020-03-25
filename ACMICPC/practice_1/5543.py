a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
b = [a,b,c]
b.sort()
bev = [d,e]
bev.sort()
print(b[0]+bev[0]-50)

import sys
a,b,c,d,e = list(map(int, sys.stdin.readline().split(' ')))

