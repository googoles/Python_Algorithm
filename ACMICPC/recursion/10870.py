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