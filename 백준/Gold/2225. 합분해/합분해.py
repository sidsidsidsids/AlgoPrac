N, K = map(int,input().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]
for k in range(1,K + 1):
    if k:
        dp[k][0] = 1
        dp[k][1] = k
for n in range(2, N + 1):
    for k in range(1, K + 1):
        dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000
print(dp[-1][-1])
