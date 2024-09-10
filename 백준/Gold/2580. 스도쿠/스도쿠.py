import sys

grid = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(9)]

def fill(n):
    if n == cnt:
        for g in grid:
            print(*g)
        exit()
    for v in range(1, 10):
        y, x = target[n]
        if check(y, x, v):
            grid[y][x] = v
            fill(n + 1)
            grid[y][x] = 0
    return

def check(i: int, j: int, n: int):
    l = [0] * 10
    l[n] = 1
    for x in range(9):
        v = grid[i][x]
        if not v:
            pass
        else:
            if l[v]:
                return False
            else:
                l[v] = 1

    l = [0] * 10
    l[n] = 1
    for y in range(9):
        v = grid[y][j]
        if not v:
            pass
        else:
            if l[v]:
                return False
            else:
                l[v] = 1

    l = [0] * 10
    l[n] = 1
    v3i = i // 3
    v3j = j // 3
    for y in range(3 * v3i, 3 * v3i + 3):
        for x in range(3 * v3j, 3 * v3j + 3):
            v = grid[y][x]
            if not v:
                pass
            else:
                if l[v]:
                    return False
                else:
                    l[v] = 1

    return True

target = []
for i in range(9):
    for j in range(9):
        if not grid[i][j]:
            target.append((i, j))
cnt = len(target)

fill(0)