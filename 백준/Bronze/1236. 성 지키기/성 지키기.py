N, M = map(int, input().split())
y, x = N, M
castle = [list(input()) for _ in range(N)]
for n in range(N):
    grid = castle[n]
    if grid.count("X"):
        y -= 1
for m in range(M):
    grid = []
    for n in range(N):
        grid.append(castle[n][m])
    if grid.count("X"):
        x -= 1
print(max(y, x))