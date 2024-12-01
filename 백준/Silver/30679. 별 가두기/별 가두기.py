import sys
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
grid = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

answer = []
visit = [[[0] * M for _ in range(N)] for _ in range(4)]

def move(y, x, d, v):
    if d == 0:
        return y - v, x
    elif d == 1:
        return y, x + v
    elif d == 2:
        return y + v, x
    elif d == 3:
        return y, x - v

def turn(d):
    return (d + 1) % 4

for n in range(1, N+1):
    i = n - 1
    j = 0
    f = 1
    closed = False

    while True:
        ni, nj = move(i, j, f, grid[i][j])
        if ni < 0 or N-1 < ni or nj < 0 or M-1 < nj:
            break
        if visit[f][ni][nj] == n:
            closed = True
            break
        visit[f][ni][nj] = n
        f = turn(f)
        i = ni
        j = nj

    if closed:
        answer.append(n)

if answer:
    print(len(answer))
    print(*answer)
else:
    print(0)