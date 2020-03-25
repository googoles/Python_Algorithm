num = int(input())

# 1 하면 그냥 하나출력
# 2 하면 교차해서 출력 no blank and blank plus star
# 3 하면 교차교차 star blank star
# 1,3,5... 홀수 개
# 2,4,6... 교차
# 개수는 입력값 x2 1제외
for i in range(1,num+1):
    print('*'*i)

    # line 1 = print('*')
    # line 2 = print('*')
    # print(' ' + '*')
