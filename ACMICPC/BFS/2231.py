# N 받아들임
# N 을 분해한다. (문자열로 변환 -> Int로 변환)
# N 값에 분해한 자리수 값을 더한다.

n = int(input())
low_case = 0


def div_nums(number):
    num_list = list(map(int, str(number)))  # 입력값 n을 문자열 str로 변환
    divided_nums = number + sum(num_list)  # 입력값에 나누어진 값을 더해준다.

    return divided_nums  # 반환!


while div_nums(low_case) != n:  # BFS니까 무차별 대입!!
    if low_case == n:  # div_nums에서 가져온 값이 n이랑 똑같다면 분해합이 아니라는것
        low_case = 0 # 0을 띄워준다.
        break
    else:
        low_case += 1 # 1씩 더하면서 고고

print(low_case)
