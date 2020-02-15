#완주하지못한 선수

# def solution(participant, completion):
#     answer = ''
#     return answer

def solution(participant,completion):
    # p_list = list(map(str, input().split(",")))
    # c_list = list(map(str, input().split(",")))
    participant.sort()
    completion.sort()
    completion.append("")
    answer = ''
    for i in range(len(participant)):
        if participant[i] in completion and participant[i] == completion[i]:
            pass
        else:
            answer = participant[i]
            print(answer)
            break
    return answer
    # print(answer)

participant = list(map(str, input().split(",")))
completion = list(map(str, input().split(",")))
solution(participant, completion)


    # def solution(participant, completion):
    #     participant = list(map(str, input().split(",")))
    #     completion = list(map(str, input().split(",")))
    #     participant.sort()
    #     completion.sort()
    #     completion.append("")
    #     answer = ''
    #     for i in range(len(participant)):
    #         if participant[i] in completion and participant[i] == completion[i]:
    #             pass
    #
    #         else:
    #             participant[i] = answer
    #             print("%d" % answer)
    #             break
    #     return answer

    # if p_list[i] in c_list:
    #     pass
    # else:
    #     p_list[i] = ans
    #     break
# print(a)

# rev = p_list - c_list
