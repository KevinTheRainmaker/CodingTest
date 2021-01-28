def solution(board):
    max = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                continue
            if max == 0:
                max = 1
            if i == 0 or j == 0:
                continue

            board[i][j] = min(board[i-1][j], board[i-1][j-1], bpard[i][j-1])+1

            if board[i][j] > max:
                max = board[i][j]

    answer = max ** 2
    return answer
