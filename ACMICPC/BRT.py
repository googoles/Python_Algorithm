#BRT Calculator

# brt_income = 4000000000 #BRT's monthly income
# print("Type your monthly income")
# your_income = float(input())  # Your monthly income
# result = your_income/brt_income #calculate
# print("%g BRT" % result)


# n = int(input())
# days =  [ "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일" ]
# print(('오늘은 {}이고, {}일 후에는 {}입니다.').format(days[0],n,days[n%7]))
# n = input()
# sum = 0
# for i in str(n):
#     sum += int(i)
# print(sum)
start_day = 2 # tues
last_day = 31
print('\tS\tM\tT\tW\tT\tF\tS')
for vacant_day in range(start_day):
    print('\t', end='')
for i in range(1,last_day+1):
    if i % 7 != (7-start_day):
        print('\t%d' %i, end='')
    elif i % 7 == (7-start_day):
        print('\t%d\n' %i)







# def sum_digit(number):
#     result = 0  # result값을 사용하기위해 초기화
#     for i in str(number):  # str(변수) 글자를 문자형으로 변환
#         result = result + int(i)  # 문자형으로 각자 나눈 숫자를 더하기 위하여 정수형으로 변환하여 덧셈
#     return result  # 계산이 끝났으니 result값
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : {}".format(sum_digit(123)));