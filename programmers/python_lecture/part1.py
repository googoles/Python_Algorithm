def solution(mylist):

    newlist = list()
    for _ in range(len(mylist)):
        newlist.append(len(mylist[_]))

    answer = newlist

    return answer

print(solution([[1,2],[3,4],[5]]))