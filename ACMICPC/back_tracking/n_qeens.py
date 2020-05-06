
count = 0

def nqueen(sol, n):
    global count

    if len(sol) == n:
        count += 1
        return 0
    candidate = list(range(n))

    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        distance = len(sol) - i
        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)
        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)
    if candidate != []:
        for i in candidate:
            sol.append(i)
            nqueen(sol,n)
    else:
        return 0


num = int(input())
for i in range(num):
    nqueen([i],num)
print(count)
