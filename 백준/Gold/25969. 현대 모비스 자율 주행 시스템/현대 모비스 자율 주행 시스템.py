import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().rstrip('\n').split())
land = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
pattern = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(5)]

visit = [[[[0] * M for _ in range(N)] for _ in range(K + 1)] for _ in range(2)]

patterns = []
for i in range(5):
    for j in range(5):
        if not (i == 2 and j == 2) and pattern[i][j] == 1:
            patterns.append((i - 2, j - 2))

dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)
answer = -1
init = land[0][0]
dq = deque()
dq.append((0, 0, 0, 0))
visit[0][0][0][0] = 1
L = 1
step = 1
flag = False
while dq:
    y, x, k, c = dq.popleft()
    L -= 1

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            item = land[ny][nx]
            if item != 1:
                if ny == N - 1 and nx == M - 1 and c:
                    flag = True
                    break
                if (item == 2 or c) and not visit[1][k][ny][nx]:
                    dq.append((ny, nx, k, 1))
                    visit[1][k][ny][nx] = 1
                elif not item and not c and not visit[0][k][ny][nx]:
                    dq.append((ny, nx, k, c))
                    visit[0][k][ny][nx] = 1

    if k < K and not flag:
        for ky, kx in patterns:
            ny, nx = y + ky, x + kx
            if 0 <= ny < N and 0 <= nx < M:
                item = land[ny][nx]
                if item != 1:
                    if ny == N - 1 and nx == M - 1 and c:
                        flag = True
                        break
                    if (item == 2 or c) and not visit[1][k + 1][ny][nx]:
                        dq.append((ny, nx, k + 1, 1))
                        visit[1][k + 1][ny][nx] = 1
                    elif not item and not c and not visit[0][k + 1][ny][nx]:
                        dq.append((ny, nx, k + 1, c))
                        visit[0][k + 1][ny][nx] = 1
    if flag:
        answer = step
        break
    if L == 0:
        step += 1
        L = len(dq)

print(answer)