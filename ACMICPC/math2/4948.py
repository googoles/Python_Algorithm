
while True:
    n = int(input())
    count = 0
    for i in range(n,2*n+1):

        for j in range(1,i):

            if (i % j == 0 and j == 1) or (i % j == 0 and j == i):





    print(count)
    count = 0



