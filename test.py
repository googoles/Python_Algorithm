# print("Hello world from outside")
#
# while True:
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 곱하기")
#     print("4. 나누기")
#     print("5. 프로그램 종료")
#     menu = int(input("원하는 기능을 입력하세요: "))
#
#     if menu <= 5:
#         if (menu == 5):
#             print('프로그램을 종료합니다.')
#             break
#         numberA = int(input('첫 번째 정수를 입력하세요: '))
#         numberB = int(input('두 번째 정수를 입력하세요: '))
#         if (menu == 1):
#             print('%d와 %d를 더하기 연산한 결과는 %d입니다.' % (numberA,numberB,numberA + numberB))
#         elif (menu == 2):
#             print('%d에서 %d를 빼기 연산한 결과는 %d입니다.' % (numberA,numberB,numberA - numberB))
#         elif (menu == 3):
#             print('%d와 %d를 곱하기 연산한 결과는 %d입니다.' % (numberA,numberB,numberA * numberB))
#         elif (menu == 4):
#             if (numberB == 0):
#                 print('연산이 불가합니다.')
#
#                 continue
#             print('%d를 %d로 나누기 연산한 결과는 %d입니다.' % (numberA,numberB,numberA / numberB))
#     else:
#         print('잘못된 번호입니다.')

a = 'spam'
b = 'ni!'

# a
print(b.upper().rstrip('!'))
# b
print(b+a+b)
#c
c = a.capitalize()
d = b.capitalize()
print(c+' '+d+' '+c+' '+d+' '+c+' '+d)
#d
print(a)
#e
print([a.rstrip('am'),a[3]])
#f
print(a.rstrip('am')+a[3]+'\n')
print("[\"%s\",\"%s\"]" % (a[0:2],a[3]))
# def test(a):
#     print(a)
#
# a = ["spam\'"]
# test(a)