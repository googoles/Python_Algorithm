

def solution(record):
    answer = []
    userData = dict()
    chatLog = []
    enterMsg = "%s님이 들어왔습니다."
    exitMsg = "%s님이 나갔습니다."

    for info in record:
        infolist = info.split(' ')
        if infolist[0] == 'Enter':
            userData[infolist[1]] = infolist[2]
            chatLog.append([enterMsg,infolist[1]])
        elif infolist[0] == 'Leave':
            chatLog.append([exitMsg,infolist[1]])
        elif infolist[0] == 'Change':
            userData[infolist[1]] = infolist[2]
    for log in chatLog:
        answer.append(log[0] % userData[log[1]])
    return answer