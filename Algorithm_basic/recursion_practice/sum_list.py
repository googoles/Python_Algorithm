def sum(n,li):
    if n<=0 or n>=len(li):
        return 0
    return li[n-1] + sum(n-1,li)

# li[n-1] + li[n-2]까지의 합

