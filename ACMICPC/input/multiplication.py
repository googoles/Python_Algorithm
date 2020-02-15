import sys
a,b = list(map(int, sys.stdin.readline().split()))
print(a*(int(b/1)-10*int(b/10)))
print(a*(int(b/10)-10*int(b/100)))
print(a*int(b/100))
print(a*b)