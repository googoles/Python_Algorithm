# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     can_pass = list()
#     while truck_weights:
#
#         while sum(can_pass) < weight:
#             can_pass.append(truck_weights.pop(0))
#         print(can_pass)
#         for index in range(0, len(truck_weights) + 1):
#             if can_pass <= weight:
#                 answer += bridge_length
#
#                 continue
#     return answer

#
def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    n = len(truck_weights)
    passing_weight = [0] * n
    passed = []
    passing = []

    i = 0
    j = -1
    while len(passed) < n:
        if len(truck_weights) > 0 and sum(passing) + truck_weights[-1] <= weight:
            passing.append(truck_weights.pop())
            j += 1
        passing_weight[:j + 1] = [passing_weight[z] + 1 for z in range(j + 1)]

        if passing_weight[i] == bridge_length:
            passed.append(passing[0])
            passing = passing[1:]
            i += 1
    answer = passing_weight[0] + 1
    return answer


def solution(bridge_length,weight,truck):
    answer = 0
    queue = [0] * bridge_length
    sec = 0
    while queue:
        sec += 1
        queue.pop()
        if truck:
            if sum(queue) + truck[0] <= weight:
                queue.append(truck.pop(0))
            else:
                queue.append(0)
    answer = sec
    return answer




bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# print(truck_weights.pop(0))
print('{} second'.format(solution(bridge_length, weight, truck_weights)))
# return 8

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# print('{} second'.format(solution(bridge_length,weight,truck_weights)))
# # return 101
#
#
# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
# print('{} second'.format(solution(bridge_length,weight,truck_weights)))
# # return 110
#
