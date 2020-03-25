import sys
a,b,c = list(map(int,sys.stdin.readline().split(' ')))
r = [a,b,c]
r.sort()
print(r[1])