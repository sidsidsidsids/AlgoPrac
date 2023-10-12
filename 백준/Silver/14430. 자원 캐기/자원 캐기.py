N, M = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for m in range(M):
    if m == 0:
        dp[0][m] = area[0][0]
    else:
        dp[0][m] = dp[0][m-1] + area[0][m]

for n in range(N):
    if n == 0:
        dp[n][0] = area[0][0]
    else:
        dp[n][0] = dp[n-1][0] + area[n][0]

for n in range(1,N):
    for m in range(1, M):
        dp[n][m] = max(dp[n-1][m]+area[n][m], dp[n][m-1]+area[n][m])

print(dp[N-1][M-1])