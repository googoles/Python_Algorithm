# data_list = [4,1,2,5,7]
# left = list()
# right = list()
# pivot = data_list[0]
#
# for index in range(1,5):
#     if data_list[index] < pivot:
#         left.append(data_list[index])
#     else:
#         right.append(data_list[index])
#
# print(left,pivot,right)

import random
data_list = random.sample(range(100),10)

# left = list()
# right = list()
# pivot = data_list[0]
#
# for index in range(1,len(data_list)):
#     if data_list[index] < pivot:
#         left.append(data_list[index])
#     else:
#         right.append(data_list[index])
#
# print(left,pivot,right)
# print(pivot)
# print(left)
# print(right)

# data_list = [4,3,2]
# left = list()
# right = list()
# pivot = data_list[0]
#
# for index in range(1,len(data_list)):
#     if data_list[index] < pivot:
#         left.append(data_list[index])
#     else:
#         right.append(data_list[index])
#
# print(left,pivot,right)

def quick_sort(data_list):

    if len(data_list) <= 1:
        return data_list

    pivot = data_list[0]
    left = list()
    right = list()
    for index in range(1,len(data_list)):
        if data_list[index] < pivot:
            left.append(data_list[index])
        else:
            right.append(data_list[index])
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(data_list))

# list comprehension

def q_s(data_list):
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[0]
    left= list()
    right = list()
    left = [data for data in data_list[1:] if data <= pivot]
    right = [data for data in data_list[1:] if data > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
print(q_s(data_list))