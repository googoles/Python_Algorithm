#8958
n = int(input())
a = []
score = 0
tot_score = 0
for i in range(n):
    ans = str(input())
    print(ans[i])
    for j in range(len(ans)):
        #while을 써보기
        while ans[j] == "0":
            score += 1
        #     print(score)
        # print(score)
            # score count
    # ct = ans.count("O")
    # a.append(ct)

    # O가 반복되는 횟수만큼 SCORE가 증가함
    # 1 - 1 2 - 2 3 - 3 4 - 4
    # O 와 X를 비교했을때 O가 아니라면 count ㄴㄴ

# print(a)