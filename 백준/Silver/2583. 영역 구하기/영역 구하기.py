from collections import deque

def DFS(y,x):
    Q = deque()
    Q.append([y,x])
    V[y][x] = 1
    value = 1
    while Q:
        elems = Q.pop()
        a, b = elems[0], elems[1]
        for ny, nx in [[a-1,b], [a+1,b], [a,b+1], [a,b-1]]:
            if 0 <= ny < M and 0 <= nx < N:
                if not grid[ny][nx] and not V[ny][nx]:
                    Q.append([ny,nx])
                    V[ny][nx] = 1
                    value += 1
    return value

M, N, K = map(int,input().split())
grid = [[0 for _ in range(N)] for _ in range(M)]
V = [[0 for _ in range(N)] for _ in range(M)]
result = []

for k in range(K):
    sn, sm, fn, fm = map(int,input().split())
    for y in range(sm, fm):
        for x in range(sn, fn):
            grid[y][x] = 1

for i in range(M):
    for j in range(N):
        if not grid[i][j] and not V[i][j]:
            cal = DFS(i,j)
            result.append(cal)

result = sorted(result, reverse=False)
print(len(result))
print(*result)

