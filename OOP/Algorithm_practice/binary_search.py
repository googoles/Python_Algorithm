# 이진탐색
# 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법
# 분할 정복 알고리즘 (Divide and Concuer)
# Divide: 문제를 하나 또는 둘 이상으로 나눈다.
# Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하다면 해결하고, 그렇지 않다면 다시 나눈다.
# 이진 탐색
# Divide: 리스트를 두개의 서브리스트로 나눈다
# Conquer
# 검색할 숫자(search) > 중간값이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
# 검색할 숫자(search) < 중간값 이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.
import random
import datetime

data_list = random.sample(range(100000), 10000)
data_list.sort()


def binary_search(data_list, search):
    print(data_list)

    if len(data_list) == 1:
        if data_list[0] == search:
            return True
        else:
            return False
    if len(data_list) == 0:
        return False
    medium = int(len(data_list) / 2)
    if search == data_list[medium]:
        return True
    if search > data_list[medium]:
        return binary_search(data_list[medium:], search)
    else:
        return binary_search(data_list[:medium], search)


print(binary_search(data_list, 34143))
print(datetime.datetime.now())
