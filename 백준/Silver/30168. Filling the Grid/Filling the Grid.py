import sys

MOD = 1000000007

H, W = map(int, sys.stdin.readline().strip().split())
R = list(map(int, sys.stdin.readline().strip().split()))
C = list(map(int, sys.stdin.readline().strip().split()))

grid = [[-1] * W for _ in range(H)]
valid = True

for i in range(H):
    for j in range(R[i]):
        grid[i][j] = 1
    if R[i] < W:
        grid[i][R[i]] = 0

for j in range(W):
    for i in range(C[j]):
        if grid[i][j] == 0:
            valid = False
        grid[i][j] = 1
    if C[j] < H:
        if grid[C[j]][j] == 1:
            valid = False
        grid[C[j]][j] = 0

if not valid:
    print(0)
else:
    free_cells = sum(row.count(-1) for row in grid)
    result = pow(2, free_cells, MOD)
    print(result)