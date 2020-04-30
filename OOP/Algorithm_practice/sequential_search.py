# 순차탐색
# 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법

from random import *
rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1,100))

def sequencial_search(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
    return -1

print(sequencial_search(rand_data_list,25))