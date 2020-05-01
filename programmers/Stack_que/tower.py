import sys


def solution(heights):
    answer = [0] * len(heights)
    while heights:
        right = heights.pop()
        for index in range(len(heights)-1, -1, -1):
            # print(len(heights)-1)
            print(index)
            if heights[index] > right:
                answer[len(heights)] = index + 1
                break
    return answer

    # if  # 제일 낮은거에서 한단계 높은거 ㄱ
    # 몇번째 탑이 수신하냐를 출력


heights = list(map(int, sys.stdin.readline().split(",")))
# 2이상 100이하
print(solution(heights))  # 신호수신 없으면 0
# 모든탑의 높이는 1이상 100이하
