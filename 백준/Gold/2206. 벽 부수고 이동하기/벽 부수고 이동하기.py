import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
graph = [list(input()) for _ in range(N)]

Q = deque()
visit = [[[-1] * M for _ in range(N)] for _ in range(2)]
Q.append((0, 0, 0))
visit[0][0][0] = 1
dist = 2
L = 1
while Q:
    d, y, x = Q.popleft()
    if y == N-1 and x == M-1:
        break
    L -= 1
    if d == 0:
        for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y,x-1)]:
            if 0 <= ny < N and 0 <= nx < M \
                    and visit[1][ny][nx] == -1 and graph[ny][nx] == '1':
                visit[1][ny][nx] = dist
                Q.append((1, ny, nx))
    for ny, nx in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]:
        if 0 <= ny < N and 0 <= nx < M \
                and visit[d][ny][nx] == -1 and graph[ny][nx] == '0':
            visit[d][ny][nx] = dist
            Q.append((d, ny, nx))
    if L == 0:
        L = len(Q)
        dist += 1
print(max(visit[1][N-1][M-1], visit[0][N-1][M-1]))