N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]

answer = 1
Q = []
Q.append((0,0))
dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
while Q:
    y, x = Q.pop()
    k = int(board[y][x])
    v = dp[y][x]
    if v > N*M+1:
        answer = -1
        break
    dy = (0, k, 0, -k)
    dx = (k, 0, -k, 0)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny <= N-1 and 0 <= nx <= M-1:
            nv = dp[ny][nx]
            if board[ny][nx] != 'H' and v >= nv:
                dp[ny][nx] = v + 1
                answer = max(v + 1, answer)
                Q.append((ny, nx))
    if answer == -1:
        break

print(answer)