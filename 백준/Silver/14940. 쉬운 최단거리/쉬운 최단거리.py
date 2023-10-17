from collections import deque

n, m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
bfs = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            bfs[i][j] = 'x'
        elif grid[i][j] == 2:
            sy = i
            sx = j

Q = deque()
Q.append([sy,sx])
checker = 1
while Q:
    elem = Q.popleft()
    y, x = elem[0], elem[1]
    for ny, nx in [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]:
        if 0 <= ny < n and 0 <= nx < m:
            if bfs[ny][nx] == 0:
                Q.append([ny,nx])
                bfs[ny][nx] = bfs[y][x] + 1

for i in range(n):
    for j in range(m):
        if i == sy and j == sx:
            print(0, end=" ")
        elif bfs[i][j] == 'x':
            print(0, end=" ")
        elif bfs[i][j] == 0:
            print(-1, end=" ")
        else:
            print(bfs[i][j], end=" ")
    print()


