def fibo(n):

    if n == 0 or n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)

def fibo_list(n):
    for i in range(n):
        print(fibo(i), end=' ')

print(fibo(2))