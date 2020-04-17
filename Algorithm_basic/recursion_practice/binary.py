def print_binary(n):
    if n<2:
        print(n, end='')
    else:
        print_binary(n//2)
        print(n%2, end='')
print_binary(15)