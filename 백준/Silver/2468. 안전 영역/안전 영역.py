N = int(input())
grid = []
minima = 101
maxima = -1

for _ in range(N):
    arr = list(map(int,input().split()))
    minima = min(minima, min(arr))
    maxima = max(maxima, max(arr))
    grid.append(arr)

answer = 0
for rain in range(minima-1, maxima + 1):
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > rain and not visit[i][j]:
                cnt += 1
                visit[i][j] = 1
                Q = [(i, j)]
                while Q:
                    elem = Q.pop()
                    y, x = elem[0], elem[1]
                    for ny, nx in [(y-1,x),(y,x+1),(y+1,x),(y,x-1)]:
                        if 0 <= ny <= N-1 and 0 <= nx <= N-1 and grid[ny][nx] > rain and not visit[ny][nx]:
                            visit[ny][nx] = 1
                            Q.append((ny, nx))
    answer = max(cnt, answer)

print(answer)