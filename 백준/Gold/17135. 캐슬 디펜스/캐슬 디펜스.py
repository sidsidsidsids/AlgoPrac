from itertools import combinations
from collections import deque

N, M, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

answer = 0
cases = [m for m in range(M)]
archers = tuple(combinations(cases, 3))
dy = (0, -1, 0)
dx = (-1, 0, 1)
for case in archers:
    grid = []
    for i in range(N):
        line = []
        for j in range(M):
            line.append(arr[i][j])
        grid.append(line)
    location = []
    kill = 0
    for idx in case:
        location.append((N, idx))

    for _ in range(N):
        target = set()
        for k in range(3):
            Q = deque()
            Q.append(location[k])
            cnt = 1
            d = 1
            V = set()
            flag = False
            while Q:
                y, x = Q.popleft()
                cnt -= 1
                for i in range(3):
                    if 0 <= y + dy[i] <= N-1 and 0 <= x + dx[i] <= M-1 and (y+dy[i],x+dx[i]) not in V:
                        if grid[y+dy[i]][x+dx[i]] == 1:
                            target.add((y+dy[i], x+dx[i]))
                            flag = True
                            break
                        V.add((y+dy[i], x+dx[i]))
                        Q.append((y+dy[i], x+dx[i]))
                if flag:
                    break
                if cnt == 0:
                    d += 1
                    if d > D:
                        break
                    cnt = len(Q)

        for y, x in target:
            grid[y][x] = 0
            kill += 1

        for n in range(N-1, -1, -1):
            for m in range(M):
                if n == N-1:
                    grid[n][m] = 0
                else:
                    if grid[n][m]:
                        grid[n][m] = 0
                        grid[n+1][m] = 1

    answer = max(kill, answer)
print(answer)



