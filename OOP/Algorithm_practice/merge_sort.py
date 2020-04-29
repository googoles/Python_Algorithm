import random
data_list = random.sample(range(100), 10)

def mergesplit(data_list):

    if len(data_list) <= 1:
        return data_list
    medium = int(len(data_list)/2)
    left = mergesplit(data_list[:medium])
    right = mergesplit(data_list[medium:])
    return merge(left,right)

def merge(left,right):
    sorted_list = list()
    left_index, right_index = 0,0
    while left_index < len(left) or right_index < len(right):

        if left_index >= len(left):
            sorted_list.append(right[right_index])
            right_index += 1
        elif right_index >= len(right):
            sorted_list.append(left[left_index])
            left_index += 1
        elif left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    return sorted_list

print(mergesplit(data_list))