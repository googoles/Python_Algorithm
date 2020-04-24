import sys


def solution(heights):
    answer = []
    new = heights.reverse()
    for i in range(len(heights)):
        # if  # 제일 낮은거에서 한단계 높은거 ㄱ
    return answer # 몇번째 탑이 수신하냐를 출력

heights = list(map(int, sys.stdin.readline.split(",")))
# 2이상 100이하
print(solution(heights))  # 신호수신 없으면 0
# 모든탑의 높이는 1이상 100이하
