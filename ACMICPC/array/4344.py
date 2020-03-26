# 4344 평균은 넘겠지

#test case C
# N, N명의 점수
# import sys
n = int(input())
for i in range(n):
    scores = []
    tot = 0
    avg = 0
    avg_pass = []
    percentage = 0
    Num_people = list(map(int,input().split()))
    for j in range(1, Num_people[0] + 1):
        scores.append(Num_people[j])
        tot += Num_people[j]
    avg = tot / Num_people[0]
    for k in range(len(scores)):
        if scores[k] > avg:
            avg_pass.append(1)
    percentage = len(avg_pass) / len(scores)
    print(round(percentage*100, 3), end = "%\n")



# n = int(input())
# for i in range(n):
#     scores = []
#     tot = 0
#     avg = 0
#     avg_pass = []
#     percentage = 0
#     numberofperson = int(input())
#     for j in range(1, numberofperson):
#         sco = int(input())
#         scores.append(sco)
#         tot += sco
#     avg = tot / len(scores)
#     for k in range(len(scores)):
#         if scores[k] > avg:
#             avg_pass.append(1)
#     percentage = len(avg_pass) / len(scores)
#     print(round(percentage*100, 3), end = "%")