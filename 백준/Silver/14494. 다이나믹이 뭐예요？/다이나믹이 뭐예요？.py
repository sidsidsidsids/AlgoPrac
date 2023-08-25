n, m = map(int,input().split())
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        ni = i+1
        nj = j+1
        if 0 <= nj < m:
            dp[i][nj] += dp[i][j]
        if 0 <= ni < n:
            dp[ni][j] += dp[i][j]
        if 0 <= nj < m and 0 <= ni < n:
            dp[ni][nj] += dp[i][j]
print(dp[n-1][m-1] % 1000000007)