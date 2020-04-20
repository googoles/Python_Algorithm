


# 6, 12, 18
 # a + i칸 i칸 판별을 어떻게 # 1 7 19 37
#6*0, 6*1, 6*2, 6*3....
n = int(input())
v0 = 1
gap = 6
ro = 1
if n == 1:
    print(1)
else:
    while True:
        v0 += gap
        ro += 1
        if n <= v0:
            print(ro)
            break
        gap += 6
# if a == b and n != 1:
#     print(a+1)
# elif n == 1:
#     print(1)
# elif a == 0:
#     print(2)
# else:
#     print(b+1)
