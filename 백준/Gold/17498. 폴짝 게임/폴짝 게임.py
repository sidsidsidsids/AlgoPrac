import sys

N, M, D = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
INF = sys.maxsize
dp = [[-INF] * M for _ in range(N)]

for j in range(M):
    dp[0][j] = 0
    for k in range(max(0, j - D + 1), min(M, j + D)):
        dp[1][j] = max(dp[1][j], arr[0][k] * arr[1][j])

for y in range(2, N):
    for x in range(M):
        val = arr[y][x]
        for i in range(max(0, y - D), y):
            for j in range(max(0, x - D + 1), min(M, x + D)):
                if abs(y - i) + abs(x - j) <= D:
                    dp[y][x] = max(dp[y][x], dp[i][j] + arr[i][j] * val)

print(max(dp[N-1]))