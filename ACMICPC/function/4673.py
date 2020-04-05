num = set(range(1,10001)) # 배열생성
gen_num = set() #생성하고싶은 배열
for i in range(1,10001): # 10000까지 반복
    for j in str(i):
        i += int(j)
    gen_num.add(i)
self_num = num - gen_num
for k in sorted(self_num):
    print(k)
