
def fac(n):
    if n>1:
        return n*fac(n-1)
    elif n == 1:
        return n

# print(fac(3))

# def multiple(data):
#     return_value = 1
#     if data<= 1:
#         return data
#     else:
#         for index in range(1,data+1):
#             return_value = return_value * index
#         return return_value

# print(multiple(10))

# import random
# data = random.sample(range(100), 10)
#
# def sum_list(data):
#     sum_value = 0
#     if len(data) == 1:
#         return data[0]
#     for item in data:
#         sum_value += item
#     return sum_value
#
# print(sum_list(data))

# def recursive(string):
#     if len(string) <= 1:
#         return True
#
#     if string[0] == string[-1]:
#         return recursive(string[1:-1])
#     else:
#         return False

# def func(data):
#     print(data)
#     if data == 1:
#         return
#     if data % 2 != 0:
#         return func(3*data+1)
#     else:
#         return func(int(data/2))
#
# print(func(3))

def find(data):
    # 1,2,3 조합으로 나타내기
    # n을 만들 수 있는 경우의 수를 리턴하는 함수가 f(n)
    if data < 0:
        return 0
    if data == 0:
        return 1
    elif data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return find(data-1) + find(data-2) + find(data-3)
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
for i in range(n):
    print(find(a[i]))