
def solution(s): # PS1

    length = []
    result = ''
    if len(s) == 1:
        return 1

    for cut in range(1, len(s)//2 + 1):
        count = 1
        temp = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == temp:
                count += 1

            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[i:i+cut]
                count = 1

        if count == 1:
            count = ''
        result += str(count) + temp
        length.append(len(result))
        result = '' # 초기화

    return min(length)

def zip(s):
    count = 0
    next = ''
    result = ''
    for i in s:
        if next != i:
            next = i
            if count: # True
                result += str(count)
            result += i
            count = 1
        else:
            count += 1
    if count:
        result += str(count)
    return count
s1 = 'aabbaccc'
s2 = "ababcdcdababcdcd"
s3 = "abcabcdede"
s4 = "abcabcabcabcdededededede"
s5 = "xababcdcdababcdcd"
print(solution(s1))
print(solution(s2))

print(zip(s1))
print(zip(s2))

