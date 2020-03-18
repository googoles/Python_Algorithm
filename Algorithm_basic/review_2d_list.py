#Practice Handling 2nd lists

kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score = [kor_score, math_score, eng_score] # 이 행렬은 5 x 3 행렬이 되었다.

print(midterm_score[0][2]) # test code 1행 3열의 있는 값 20이 출력된다.

# 사람별 평균을 구해보자.

avg_result = [0,0,0,0,0];

for i in range(0, len(kor_score)):
    avg_result[i] += kor_score[i]
    avg_result[i] += math_score[i]
    avg_result[i] += eng_score[i]
    avg_result[i] = (avg_result[i]/len(midterm_score))

# final_result = avg_result/3
print(avg_result)

# 위는 내 코드

student_score = [0,0,0,0,0]

j = 0

for subject in midterm_score:
    for score in subject:
        student_score[j] += score
        i += 1 # 학생 index 구분
    i = 0 # 인덱스 초기화
else:
    a,b,c,d,e = student_score
    student_score = [a/3,b/3,c/3,d/3,e/3]
    print(student_score)