import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
grid = [list(map(int,input().rstrip())) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
for n in range(N):
    for m in range(M):
        if grid[n][m] == 0:
            grid[n][m] = -1
            cnt = 1
            Q = deque()
            Q.append((n, m))
            adj = set()
            while Q:
                elem = Q.popleft()
                y, x = elem[0], elem[1]
                for nidx in range(4):
                    ny = y + di[nidx]
                    nx = x + dj[nidx]
                    if 0 <= ny < N and 0 <= nx < M:
                        if grid[ny][nx] == 0:
                            grid[ny][nx] = -1
                            Q.append((ny, nx))
                            cnt += 1
                        elif grid[ny][nx] > 0:
                            adj.add((ny, nx))
            while adj:
                elem = adj.pop()
                cy, cx = elem[0], elem[1]
                grid[cy][cx] += cnt % 10

for n in range(N):
    for m in range(M):
        if grid[n][m] < 0:
            print(0, end="")
        else:
            print(grid[n][m] % 10, end="")
    print("")