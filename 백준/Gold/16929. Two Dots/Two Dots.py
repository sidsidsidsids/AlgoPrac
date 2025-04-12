import sys

N, M = map(int, sys.stdin.readline().strip().split())
grid = [sys.stdin.readline().strip() for _ in range(N)]

visit = [[0] * M for _ in range(N)]
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
flag = False

for n in range(N):
    if flag:
        break
    for m in range(M):
        if flag:
            break
        if not visit[n][m]:
            visit[n][m] = 1
            target = grid[n][m]
            Q = [(n, m)]
            L = 0
            while Q:
                if flag:
                    break
                y, x = Q.pop()
                used = 0
                L += 1
                for d in range(4):
                    ny, nx = y+dy[d], x+dx[d]
                    if 0 <= ny < N and 0 <= nx < M:
                        if not visit[ny][nx] and grid[ny][nx] == target:
                            visit[ny][nx] = 1
                            Q.append((ny, nx))
                        elif visit[ny][nx] and grid[ny][nx] == target:
                            used += 1
                            if used >= 2 and L >= 4:
                                flag = True
                                break

print("Yes" if flag else "No")