import sys
n = int(input())
scores = list(map(int,sys.stdin.readline().split()))
new_sc = 0
n_tot = 0
# 나머지 점수들을 최고점수 M으로 나누게된다
# sort() 해서 제일 큰 값 기준으로 나머지 값을 나눈다음 평균
scores.sort(reverse=True)
for num in scores:
    new_sc = (num/scores[0])*100
    n_tot += new_sc
print(n_tot/n)
