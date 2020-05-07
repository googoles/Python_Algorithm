

def solution(record):
    answer = []
    userData = dict()
    c_log = []
    e_msg = "%s님이 들어왔습니다."
    q_msg = "%s님이 나갔습니다."

    for info in record:
        infolist = info.split(' ')
        if infolist[0] == 'Enter':
            userData[infolist[1]] = infolist[2]
            c_log.append([e_msg,infolist[1]])
        elif infolist[0] == 'Leave':
            c_log.append([q_msg,infolist[1]])
        elif infolist[0] == 'Change':
            userData[infolist[1]] = infolist[2]
    for log in c_log:
        answer.append(log[0] % userData[log[1]])
    return answer