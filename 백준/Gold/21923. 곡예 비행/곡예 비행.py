import sys

N, M = map(int,sys.stdin.readline().rstrip('\n').split())
grid = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

fly_up = [[0] * M for _ in range(N)]
fly_down = [[0] * M for _ in range(N)]
fly_up[N-1][0] = grid[N-1][0]
fly_down[N-1][M-1] = grid[N-1][M-1]

for m in range(1, M):
    fly_up[N-1][m] = fly_up[N-1][m-1] + grid[N-1][m]
    fly_down[N-1][M-1-m] = fly_down[N-1][M-m] + grid[N-1][M-1-m]
for n in range(N-2, -1, -1):
    fly_up[n][0] = fly_up[n+1][0] + grid[n][0]
    fly_down[n][M-1] = fly_down[n+1][M-1] + grid[n][M-1]

for n in range(N-2, -1 ,-1):
    for m in range(1, M):
        fly_up[n][m] = max(fly_up[n+1][m], fly_up[n][m-1]) + grid[n][m]
        fly_down[n][M-1-m] = max(fly_down[n+1][M-1-m], fly_down[n][M-m]) + grid[n][M-1-m]

answer = -sys.maxsize
for n in range(N):
    for m in range(M):
        answer = max(answer, fly_up[n][m] + fly_down[n][m])

print(answer)