# def solution(numbers):
#     answer = ''
#     return answer
from collections import deque

answer = ''
# numbers = [6,10,2]
numbers = [3, 30, 34, 5, 9]
# 제일 큰 수가되려면 첫자리가 제일 커야한다. # 리스트 분리 후 첫자리 찾기?
# a = str(numbers[0])

new_num_list = []
for num in numbers:
    a = str(num)
    new_num_list.append(int(a[0]))
numbers.sort(reverse=True)
new_num_list.sort(reverse=True) # 앞자리만 정렬된 리스트


old_num = deque(numbers)
new_num = deque(new_num_list)
print(new_num_list)
print(numbers)


for i in range(len(numbers)):
    # print(str(n))
    if new_num_list[i] >= new_num_list[i]:
        answer += str(new_num_list[i])
    elif new_num_list[i-1] == new_num_list[i]:
        answer += str(old_num.popleft())
    else:
        answer += str(numbers[i])


print(answer)

# print(type(a))
# for문 쓰자
# print(answer.join([str(max(b)),'b']))

