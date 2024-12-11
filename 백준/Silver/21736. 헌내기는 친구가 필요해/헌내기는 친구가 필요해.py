N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

Q = []
V = [[0] * M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if grid[n][m] == "I":
            Q = [(n, m)]
            V[n][m] = 1
            break
    if Q:
        break

answer = 0
while Q:
    y, x = Q.pop()
    for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
        if 0 <= ny < N and 0 <= nx < M and not V[ny][nx] and grid[ny][nx] != "X":
            if grid[ny][nx] == "P":
                answer += 1
            V[ny][nx] = 1
            Q.append((ny, nx))

print(answer if answer else "TT")