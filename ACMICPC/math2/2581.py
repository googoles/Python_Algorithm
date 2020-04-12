import sys
m = int(sys.stdin.readline()); n = int(sys.stdin.readline())
cnt = 0;cn_min = 0;real_cnt = 0
for i in range(m,n+1):
    cn = 1
    for j in range(1,i):
        if i%j == 0:
            cn += 1
    if cn == 2:
        cnt += i
        real_cnt += 1
        if real_cnt == 1:
            cn_min += i
        cn = 0
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(cn_min)
    # elif cn == 2:
    #     cnt += i
# print(sum(cnt),min(cnt)) if len(cnt) != 0 else print(-1)
# print(cnt,cn_min) if cnt != 0 else print(-1)

# if len(cnt) == 0:
#     print(-1)
# else:
#     print(sum(cnt),min(cnt))


