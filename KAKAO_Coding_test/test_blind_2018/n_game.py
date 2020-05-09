

def conv(number,base):
    T = '0123456789ABCDEF'

    i , j = divmod(number,base)

    if i == 0:
        return T[j]
    else:
        return conv(i,base) + T[j]

def solution(n,t,m,p):
    answer = ''
    temp = ''
    number = 0
    while True:
        temp += conv(number,n)

        number += 1

        if len(temp) > t*m:
            break

    for idx in range(p-1,len(temp),m):
        if t == len(answer):
            break
        answer += temp[idx]

    print(answer)
    return answer

solution(2,4,2,1) # '0111'
solution(16,16,2,1) # '02468ACE11111111'
solution(16,16,2,2) # '13579BDF01234567'
