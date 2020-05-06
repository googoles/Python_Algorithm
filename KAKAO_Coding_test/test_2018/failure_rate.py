from collections import *

# def solution(N, stages):
#     '''
#     스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
#     :param stages:
#     :return:
#     '''

#
N = 5
stages = [2,1,2,6,2,4,3,3]

def solution(N, stages):

    participants = len(stages)
    did_pass = []

    for _ in range(1,N+1):
        did_pass.append(stages.count(_))

    rate_dict = dict()
    for i in range(N):
        if i == 0:
            rate = did_pass[i]/(len(stages))
        else:

            rate = did_pass[i]/(len(stages)-sum(did_pass[:i]))

        rate_dict[i+1] = rate

    answer = []
    for y,v in sorted(rate_dict.items(), key=lambda rate_dict:rate_dict[1], reverse = True):
        # print(y)
        answer.append(y)

    return answer

print(solution(N,stages))
# print(did_pass)



#     for i in range(N):
#         #count
#
#
#
# print(solution(stages))