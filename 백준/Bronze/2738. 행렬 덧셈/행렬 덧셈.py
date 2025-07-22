N, M = map(int, input().split())
grid0 = [[0] * M for _ in range(N)]
grid1 = [list(map(int, input().split())) for _ in range(N)]
grid2 = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    for m in range(M):
        grid0[n][m] = grid1[n][m] + grid2[n][m]
for g in grid0:
    print(*g)