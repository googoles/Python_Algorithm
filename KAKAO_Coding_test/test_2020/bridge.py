import copy

INF = 200000000

def solution(stones, k):
    left = 1; right = INF # 사람의 명수!!

    while left <= right:
        mid = (left + right) // 2
        tmp = copy.deepcopy(stones)

        for i in range(len(tmp)):
            tmp[i] -= mid

        count = 0
        check = False
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                count += 1
            else:
                count = 0

            if count >= k:
                check = True
                break

        if check is True:
            right = mid - 1
        else:
            left = mid + 1

    return left