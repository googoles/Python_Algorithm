n = int(input())

def fib(a, b, count):
    if(n == 0):
        print(a)
    elif(n == 1):
        print(b)
    else:
        c = a + b

        if(count == n):
            return print(c)

        return fib(b, c, count + 1)
fib(0, 1, 2)

# import math
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
#
# dx = x2-x1
# dy = y2-y1
#
# d = math.sqrt(dx**2 + dy ** 2)
#
# print("거리 %d" %d)
# print("학번 이름")