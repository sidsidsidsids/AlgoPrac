import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]

grids = 0
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

V = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == "." and not V[i][j]:
            grids += 1
            V[i][j] = 1
            Q = [(i, j)]
            while Q:
                y, x = Q.pop()
                for n in range(4):
                    ny = y + dy[n]
                    nx = x + dx[n]
                    if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == "." and not V[ny][nx]:
                        Q.append((ny, nx))
                        V[ny][nx] = 1

answer = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == ".":
            arr[i][j] = "@"
            V = [[0] * N for _ in range(N)]
            spaces = 0
            for r in range(N):
                for c in range(N):
                    if spaces > grids:
                        break
                    if arr[r][c] == "." and not V[r][c]:
                        spaces += 1
                        V[r][c] = 1
                        Q = [(r, c)]
                        while Q:
                            y, x = Q.pop()
                            for n in range(4):
                                ny = y + dy[n]
                                nx = x + dx[n]
                                if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == "." and not V[ny][nx]:
                                    Q.append((ny, nx))
                                    V[ny][nx] = 1
                if spaces > grids:
                    break
            if spaces > grids:
                answer += 1
            arr[i][j] = "."

print(answer)