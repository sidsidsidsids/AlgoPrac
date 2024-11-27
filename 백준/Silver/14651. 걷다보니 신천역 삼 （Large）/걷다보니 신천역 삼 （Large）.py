N = int(input())
dp = [[0, 0, 0] for _ in range(N + 2)]
dp[1][1] = 1
dp[1][2] = 1
for i in range(2, N+1):
    S = sum(dp[i-1]) % 1000000009
    dp[i][0] = S
    dp[i][1] = S
    dp[i][2] = S
print(dp[N][0])
