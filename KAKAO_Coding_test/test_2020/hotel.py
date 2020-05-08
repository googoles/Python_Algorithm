import sys
sys.setrecursionlimit(1500)

# 방찾기

def find_empty_room(x, rooms):

    # 현재 방번호 x에 배정받지 않은경우

    if x not in rooms:
        # 현재 방번호 기준, 다음 빈 방 좌표 저작
        rooms[x] = x+1
        return x # 방번호 반환

    # 재귀함수로 배정안된 방 나올때까지 함수 실행
    p = find_empty_room(rooms[x], rooms)
    rooms[x] = p + 1
    return p

def solution(k, room_number):
    # 해당번호기준, 번호보다 값이 크면서 빈 방의 좌표를 저장하는 dict

    rooms = dict()
    answer = []

    for each_room in room_number:
        empty_room = find_empty_room(each_room, rooms)
        answer.append(empty_room)
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k,room_number))