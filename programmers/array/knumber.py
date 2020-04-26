def solution(array,commands):
    answer = []
    for com in commands:
        # print(com)
        new_list = array[com[0]-1:com[1]]
        new_list.sort()
        answer.append(new_list[com[-1]-1])
        # new_list = []
    return answer

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1,5,2,6,3,7,4]
print(solution(array,commands))


# return [5,6,3]