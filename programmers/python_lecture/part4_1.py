# def solution(mylist):
#     # new_list = [[],[],[]]
#     #
#     # for i in range(3):
#     #     for j in range(3):
#     #         new_list[i].append(mylist[j][i])
#
#
#     new_list = list(map(list,zip(*mylist)))
#     answer = new_list
#
#
#     return answer
#
#
# print(solution([[1,2,3],[4,5,6],[7,8,9]]))

def solution(mylist):
    answer = list(map(len,mylist))
    return answer

print(solution([[1],[2]]))