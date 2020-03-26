#8958
n = int(input()) # N번 반복
score = 0 # Score의 초기값
tot_score = 0 # 총 값의 초기값
for i in range(n): # n번 반복한다
    ans = str(input()) # n번만큼 String 값을 입력받는다
    for j in range(len(ans)): # String값의 길이만큼 하나씩 대조해본다
        if ans[j] == 'O': # O이 나온다면
            score += 1  # score에 1을 추가시켜주고
            tot_score += score # 총점에 score를 더한다.
        else:
            score = 0 # O가 아니라면 score를 초기화시킨다.
    print(tot_score) # 총점 출력
    tot_score = 0 # 총점 초기화
    score = 0 # score 초기화

# print(tot_score_list)
