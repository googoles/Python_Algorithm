import heapq

def solution(scoville, k):
    heapq.heapify(scoville)

    i = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            i += 1
        else:
            return -1
    answer = i
    return answer



print(solution([1,2,3,9,10,12],7))