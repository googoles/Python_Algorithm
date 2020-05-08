from collections import deque

def solution(board, moves):

    answer = 0
    moves = deque([move-1 for move in moves])

    print(moves)
    stack = []

    while moves:
        found = False
        j = moves.popleft()

        for i in range(len(board)):
            if board[i][j] > 0:
                found = True
                current = board[i][j]
                board[i][j] = 0
                break

        if stack and found:
            top = stack.pop()
            if current == top:
                answer += 2
            else:
                stack.append(top)
                stack.append(current)
        else:
            stack.append(current)

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))