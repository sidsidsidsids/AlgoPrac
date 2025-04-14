import sys

grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]

m = -1
y = int
x = int
for i in range(9):
    for j in range(9):
        if m < grid[i][j]:
            m = grid[i][j]
            y = i + 1
            x = j + 1
print(m)
print(y, x)