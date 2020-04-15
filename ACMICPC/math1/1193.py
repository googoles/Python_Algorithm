#find number

x = int(input())
if x == 1:
    print(1+'/'+1)
sum = 1
cnt = 0
num = 1
while 1:
    sum += 1
    cnt += num
    if cnt >= x:
        break
    num += 1
n = 1 # 분자
d = 1 # 분모
if sum % 2:
    n = sum -1
else:
    d = sum -1
while 1:
    if cnt == x:
        break

    if sum%2:
        d += 1
        n -= 1
    else:
        n += 1
        d -= 1
    cnt -= 1
print('{}/{}'.format(n,d))

# 1, 3 ,6 ,10, 15 # a2-a1 = 1, a3-a2 = 3, a4-a3 = 4, a5-a4 = 5
# 2, 5, 9, 14, # b2-b1 = 2, b3-b2 = 4 b4-b3 = 5
# 4, 8, 13 # c2-c1 = 4 c3-c2 = 5 ,6
# 7, 12
# 11
# [i][j] => 0,0 = 1 0,1 = 2, 1,0 = 3, 1,1 =
# 14가 나오면 2/4
# 세로는 분자가 증가하고 가로는 분모가 증가
# 대각선마다 합이 같다. 1,3,6,10,15 => 1,2,3,4,5,
# 10~15까지는 5행, 16~21까지는 6행