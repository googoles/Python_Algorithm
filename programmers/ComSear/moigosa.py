# import operator
#
#
# def countAnswer(answers, x):
#     cnt = 0
#     score = 0
#     for i in range(len(answers)):
#         if cnt >= len(x):
#             cnt = 0
#
#         if answers[i] == x[cnt]:
#             score += 1
#             cnt += 1
#         else:
#             cnt += 1
#
#     return score
#
#
# def solution(answers):
#     answer = []
#
#     # ...1
#     s1 = [1, 2, 3, 4, 5]
#     s2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#
#     # ...2
#     s1Count = countAnswer(answers, s1)
#     s2Count = countAnswer(answers, s2)
#     s3Count = countAnswer(answers, s3)
#
#     # ...3
#     tmepDict = {1: s1Count, 2: s2Count, 3: s3Count}
#     sortedScore =
#     sorted(tmepDict.items(), key=operator.itemgetter(1), reverse=True)
#
#
# # ...4
#     highScore = 0
#     tempCount = 0
#     for key, value in sortedScore:
#         if tempCount == 0:
#             answer.append(key)
#             highScore = value
#             tempCount += 1
#         else:
#             if highScore == value:
#                 answer.append(key)
#
#     print(answer)
#     return answer


