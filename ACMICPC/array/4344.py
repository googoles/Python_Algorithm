# 4344 평균은 넘겠지

#test case C
# N, N명의 점수

n = int(input())
for i in range(n):
    scores = []
    tot = 0
    avg = 0
    avg_pass = []
    percentage = 0
    numberofperson = int(input())
    for j in range(numberofperson):
        sco = int(input())
        scores.append(sco)
        tot += sco
    avg = tot / len(scores)
    for k in range(len(scores)):
        if scores[k] > avg:
            avg_pass.append(1)
    percentage = len(avg_pass) / len(scores)

    print(round(percentage*100, 3), end = "%")

# print("%3f%%" % percentage*100)
    # print(avg)

