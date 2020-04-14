# 정수 배열과 정수 S가 주어졌을 때, 원소의 합이 S와 같은 가장 긴 부분 배열을 구하시오.
# 부분 배열은 배열 내의 연속된 원소들의 집합입니다.
# Input: [5, 6, -5, 5, 3, 5, 3, -2, 0], S = 8
# Output: [-5, 5, 3, 5]

n = list(map(int,input().split(",")))
s = int(input())
tot = []
for i in range(len(n)):
    sum = 0
    cnt = []
    for j in range(len(n)):
        sum += n[j]
        cnt.append(n[j])
        print(cnt)
        if sum == s:
            # print(sum)
            tot.append(cnt)
            break
        # else:
            # print('Not same as s')
    del n[0]
print(tot[0])


# print(sum)


# 일단 Input elements 을 더해서 S와 합이 되는 부분을 만들자 반복은 계속하고 합이 되는 부분은 저장한다.
# 양 끝을 pop 시켜버리면 어떨까
