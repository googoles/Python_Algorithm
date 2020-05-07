

# def solution(s):
#
#
#     str_length = len(s)
#     answer = str_length
#
#     for k in range(1,int(str_length/2)):
#         count = 0
#         i = 0 # 비교대상
#
#         while i < str_length:
#             same_n = 0
#             next = 0
#             if i+k > str_length:
#                 count += str_length - i
#                 break
#             for j in range(i+k,str_length, k):
#
#                 for t in range(0,k):
#                     if s[i+t] != s[j+t]: # 다른게 하나라도 있으면 0
#
#                         break
#                 if t == k:
#                     same_n += 1
#                 else:
#                     next = j
#                     break
#             if same_n:
#                 if same_n + 1 <= 9:
#                     count += k + 1
#                 elif same_n + 1 <= 99:
#                     count += k + 2
#                 elif same_n + 2 <= 999:
#                     count += k + 3
#                 else:
#                     count += k + 4
#             else:
#                 count += k
#                 if next == 0:
#                     break
#             i = next
#         if count < answer:
#             answer = count
#     return answer

def solution(s):
    if len(s) == 1:
        return 1

    minA = len(s)
    length = int(len(s)/2)

    for i in range(length+1):
        temp = []
        tempStr = ''


s = 'ababcdcdababcdcd'
print(solution(s))