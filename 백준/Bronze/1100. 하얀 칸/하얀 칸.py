import sys

board = [sys.stdin.readline().strip() for _ in range(8)]
flag = False
answer = 0
for i in range(8):
    for j in range(8):
        flag = not flag
        if flag and board[i][j] == 'F':
            answer += 1
    flag = not flag
print(answer)