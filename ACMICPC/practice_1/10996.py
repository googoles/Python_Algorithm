

# 1 하면 그냥 하나출력
# 2 하면 교차해서 출력 no blank and blank plus star
# 3 하면 교차교차 star blank star
# 1,3,5... 홀수 개
# 2,4,6... 교차
# 개수는 입력값 x2 1제외
# if num == 1:
#     print('*')
# else:
# num = int(input())
# for i in range(num*2):
#     st = ''
#     for j in range(num):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 print("*")
#             else:
#                 print(' ')
#         else:
#             if j % 2 == 0:
#                 print(' ')
#             else:
#                 print('*')

n = int(input())

for i in range(n * 2):
    st = ''
    if i % 2 == 0:
        for j in range(n):
            if j % 2 == 0:
                st += '*'
            else:
                st += ' '
    else:
        for j in range(n):
            if j % 2 == 0:
                st += ' '
            else:
                st += '*'
    print(st)

    # print('')
    # line 1 = print('*')
    # line 2 = print('*')
    # print(' ' + '*')
