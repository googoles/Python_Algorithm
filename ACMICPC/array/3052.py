# a/b있을때 나머지
# for문을 이용해서 append를 사용해 list 생성


a = []
for i in range(10):
    b = int(input())
    c = b % 42 # 42로 나누기
    a.append(c) # 배열 확장

remove_dup = list(set(a)) # 중복제거
print(len(remove_dup)) # 숫자세서 보여주기