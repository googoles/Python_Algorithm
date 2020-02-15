#mail0707

numlist = list(map(int, input().split(",")))
n = int(input())
# n = n+1
numlist.sort()
numlist.reverse()
# print(numlist)
print(numlist[n-1])