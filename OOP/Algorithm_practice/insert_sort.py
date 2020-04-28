
# def insert_sort(data_list):

# swapped = False
# data_list = [9,3,2,5]
# while True:
#
#     for index in range(1,len(data_list)):
#
#         if data_list[index-1] > data_list[index]:
#
#             data_list[index-1], data_list[index] = data_list[index], data_list[index-1]
#
#             swapped = True
#         else:
#             break
#
#     # return data_list
# #
# # data_list = [9,3,2,5]
# print(data_list)

# def insertion_sort(data_list):
#     for stand in range(len(data_list)):
#         key = data_list[stand]
#         for num in range(stand, 0, -1):
#             if key < data_list[num - 1]:
#                 data_list[num - 1], data_list[num] = data_list[num], data_list[num - 1]
#             else:
#                 break
#     return data_list

from random import *

rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1,100))

def insertion_sort(data_list):

    for stand in range(len(data_list)):
        key = data_list[stand]
        for num in range(stand,0,-1):
            if key < data_list[num-1]:
                data_list[num-1], data_list[num] = data_list[num], data_list[num-1]
            else:
                break
    return data_list

insertion_sort(rand_data_list)
print(rand_data_list)
