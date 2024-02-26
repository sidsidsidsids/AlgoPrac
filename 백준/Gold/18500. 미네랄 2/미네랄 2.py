from collections import deque
R, C = map(int,input().split())
grid = [list(input()) for _ in range(R)]
N = int(input())
actions = list(map(int,input().split()))

def simulate(Y, X):
    global grid
    Q = deque()
    Q.append((Y, X))
    V = set()
    V.add((Y, X))
    drop = True
    if Y == R - 1:
        drop = False
    while Q:
        elems = Q.popleft()
        i, j = elems[0], elems[1]
        for ni, nj in [[i + 1, j], [i, j - 1], [i, j + 1], [i - 1, j]]:
            if 0 <= ni < R and 0 <= nj < C:
                if grid[ni][nj] == 'x' and (ni, nj) not in V:
                    if ni == R - 1:
                        drop = False
                        break
                    Q.append((ni, nj))
                    V.add((ni, nj))
        if not drop:
            break
    if drop:
        for elem in V:
            grid[elem[0]][elem[1]] = '.'
        value = 0
        for d in range(1, R):
            for elem in V:
                if elem[0] + d == R - 1:
                    value = d
                if grid[elem[0] + d][elem[1]] == 'x':
                    value = d - 1
                    break
            if value:
                break
        for elem in V:
            grid[elem[0] + value][elem[1]] = 'x'

    return drop, V

for n in range(N):
    r = R - actions[n]
    y = r
    x = -1
    if n % 2: # 짝수
        for c in range(C-1,-1,-1):
            if grid[r][c] == 'x':
                x = c
                break
    else:
        for c in range(0,C):
            if grid[r][c] == 'x':
                x = c
                break
    if x != -1:
        grid[y][x] = '.'
        cluster = set()
        for ay, ax in [[y-1,x],[y,x+1],[y,x-1],[y+1,x]]:
            if 0 <= ay < R and 0 <= ax < C and grid[ay][ax] == 'x' and (ay, ax) not in cluster:
                is_drop, result = simulate(ay, ax)
                if is_drop:
                    break
                else:
                    cluster.update(result)

for r in range(R):
    for c in range(C):
        print(grid[r][c], end='')
    print()
