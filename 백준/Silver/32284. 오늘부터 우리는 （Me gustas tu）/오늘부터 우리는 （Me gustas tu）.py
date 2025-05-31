N, M = map(int, input().split())
a, b = map(int, input().split())

grid = [[0] * M for _ in range(N)]
for i in range(M):
    if i <= b:
        grid[a][i] = "E"
    else:
        grid[a][i] = "W"

for i in range(N):
    if i == a:
        continue
    for j in range(M):
        if i < a:
            grid[i][j] = "S"
        else:
            grid[i][j] = "N"

for elems in grid:
    A = ""
    for elem in elems:
        A += elem
    print(A)