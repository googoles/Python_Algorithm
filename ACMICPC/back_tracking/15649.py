n,m = map(int,input().split())

count = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]

def seq(index,n,m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in range(1,n+1):
        if count[i]==1:
            continue
        result[index] = i
        count[i] = 1
        seq(index+1,n,m)
        count[i] = 0

print(seq(0,n,m))

