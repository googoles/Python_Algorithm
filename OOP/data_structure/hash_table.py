'''
1. It is the data structure that store Value in Key
 1) It is going to be fast because using key to receive values
 2) Python's Dictionary type
 3) Don't have to create Hash - You have to use Dictionary type

2. Must know these
 1) Hash : 임의 값을 고정 길이로 변환
 2) Hash Table : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
 3) Hashing Function : Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
 4) Hash Value or Hash Address :  Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고,
  이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
 5) Slot : 한 개의 데이터를 저장할 수 있는 공간

'''

# hash_table = list([i for i in range(10)])
# print(hash_table)
#
# def hash_func(key):
#     return key % 5

# data1 = "Andy"
# data2 = 'Dave'
# data3 = 'Trump'
# data4 = 'Anthor'
#
# print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
# print (ord(data1[0]), hash_func(ord(data1[0])))
# print (ord(data1[0]), ord(data4[0]))

# def storage_data(data, value):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     hash_table[hash_address] = value
#
# storage_data('Andy', '01055553333')
# storage_data('Dave', '01044443333')
# storage_data('Trump', '01022223333')
#
# def get_data(data):
#     key = ord(data[0])
#     hash_address = hash_func(key)
#     return hash_table[hash_address]
#
# print(get_data('Andy'))
#
# hash_table = list([0 for i in range(8)])
#
#
# def get_key(data):
#     return hash(data)
#
#
# def hash_function(key):
#     return key % 8
#
#
# def save_data(data, value):
#     hash_address = hash_function(get_key(data))
#     hash_table[hash_address] = value
#
#
# def read_data(data):
#     hash_address = hash_function(get_key(data))
#     return hash_table[hash_address]
#
# save_data('Dave', '0102030200')
# save_data('Andy', '01033232200')
# print(read_data('Dave'))
# print(hash_table)

"""
6.1. Chaining 기법

개방 해슁 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법
"""
#
# hash_table = list([0 for i in range(8)])
#
# def get_key(data):
#     return hash(data)
#
# def hash_function(key):
#     return key % 8
#
# def save_data(data,value):
#     index_key = get_key(data)
#     hash_address = hash_function(index_key)
#     if hash_table[hash_address] != 0:
#         for index in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][index][0] == index_key:
#                 hash_table[hash_address][index][1] = value
#                 return
#             hash_table[hash_address].append([index_key, value])
#     else:
#         hash_table[hash_address] = [[index_key, value]]
#
# def read_data(data):
#     index_key = get_key(data)
#     hash_address = hash_function(index_key)
#
#     if hash_table[hash_address] != 0:
#         for index in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][index][0] == index_key:
#                 return hash_table[hash_address][index][1]
#         return None
#     else:
#         return None
#
# # print(hash('Dave') % 8)
# save_data('Dd', '1201023010')
# save_data('Data', '3301023010')
# read_data('Dd')
# print(hash_table)

"""
6.2. Linear Probing 기법

폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
저장공간 활용도를 높이기 위한 기법

"""

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key,value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] == value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None
print (hash('dk') % 8)
print (hash('da') % 8)
print (hash('dc') % 8)