
s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# [2, 1, 3, 4]
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# [2, 1, 3, 4]
s3 = "{{20,111},{111}}"
# [111, 20]
s4 = "{{123}}"
# [123]
def solution(s):
    answer = []

    string = s[1:len(s)-1].replace("},",'}-').split('-') # 문자열을 분리시켜준다.
    string = sorted([item[1:len(item)-1] for item in string], key=lambda item : len(item)) # item의 개수 대로 정렬한 후 집합생성

    for item in string: # string 순회
        for dit in item.split(','): # ,로나눈후 하나씩 비교
            if int(dit) not in answer: # answer에 없다면
                answer.append(int(dit)) # answer 에 추가시켜준다.

    print(string)


    return answer

print(solution(s1))
print(solution(s2))
print(solution(s3))





