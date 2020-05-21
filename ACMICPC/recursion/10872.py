import sys
sys.setrecursionlimit(10**6)
n = int(input())
def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fac(n-1)
print(fac(n))
