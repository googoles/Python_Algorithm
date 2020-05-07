from itertools import combinations


# def solution(relation):
#     def checkCandidate(colList, rows):
#         tmp = [tuple([item[idx] for idx in colList]) for item in relation]
#         if len(set(tmp)) != rows:
#             return False
#         else:
#             return True
#
#     '''
#
#     유일성 검증을 위해서는 각 속성을 조합Combination을 이용하여 n을 속성의 총 갯수, m을 선정해야하는
#     속성의 갯수라고 했을 때, nC1 부터 nCm까지의 튜플(Tuple)이 필요했습니다.
#      저는 checkCandidate(colLst, rows)라는 함수를 만들어 [tuple([item[idx]
#       for idx in colLst]) for item in relation]을 이용해 조합을 통해
#        만들어진 각각의 tuple에 해당하는 속성을 가진 tmp라는 새로운 배열을 만듭니다.
#        다시 집합 자료형으로 바꿔주어 중복이 있는 지 확인하여, 중복이 있다면 후보에서 탈락하고,
#        중복이 없이 relation의 행의 갯수와 같다면 후보에 넣어줍니다.
#        이렇게 하면 첫 번째 조건인 유일성에 대한 검증은 마무리됩니다.
#
# 출처: https://geonlee.tistory.com/66?category=313022 [빠리의 택시 운전사]
#
#     '''
#
#     rows = len(relation)
#     cols = len(relation[0])
#     col_List = range(cols)
#     lst = []
#     for leng in range(1, cols + 1):
#         comb = combinations(col_List, leng)
#         for n1 in list(comb):
#             if checkCandidate(n1, rows):
#                 lst.append(set(n1))
#     for el1 in lst[:]:
#         for el2 in lst[:]:
#             if el1 == el1 & el2:
#                 lst.remove(el2)
#
#     return len(lst)
def solution(relation):

    answer = 0

    all = list()

    uniqIdx = []

    if len(relation) > 0:
        size_col = len(relation[0])
        size_row = len(relation)

        for i in range(1, size_col+1):
            all.extend([set(k) for k in combinations([i for j in range(size_col)], i)])



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))