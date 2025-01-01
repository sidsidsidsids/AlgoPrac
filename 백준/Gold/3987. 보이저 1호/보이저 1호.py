import sys
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
grid = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
si, sj = map(int, sys.stdin.readline().rstrip('\n').split())

si -= 1
sj -= 1

def turn(ti, tj, d):
    if grid[ti][tj] == "/":
        if d == 0:
            return ti, tj, 1
        elif d == 1:
            return ti, tj, 0
        elif d == 2:
            return ti, tj, 3
        elif d == 3:
            return ti, tj, 2
    elif grid[ti][tj] == "\\":
        if d == 0:
            return ti, tj, 3
        elif d == 1:
            return ti, tj, 2
        elif d == 2:
            return ti, tj, 1
        elif d == 3:
            return ti, tj, 0
    return "not block"

def move(i, j, d):
    if d == 0:
        return i-1, j, d
    elif d == 1:
        return i, j+1, d
    elif d == 2:
        return i+1, j, d
    elif d == 3:
        return i, j-1, d
    return "invalid input"

voyager = False
maxima = -1
direct = ''
Ds = ['U','R','D','L']
for s in range(4):
    if voyager:
        break
    i, j, d = si, sj, s
    time = 0
    while True:
        time += 1
        if time > (N * M * 2) + 1:
            voyager = True
            break
        ni, nj, nd = move(i, j, d)
        if 0 <= ni < N and 0 <= nj < M:
            if grid[ni][nj] == ".":
                i, j, d = ni, nj, nd
            elif grid[ni][nj] == "C":
                break
            else:
                i, j, d = turn(ni, nj, nd)
        else:
            break
    if voyager or time > maxima:
        maxima = time
        direct = Ds[s]
print(direct)
print("Voyager" if voyager else maxima)