N = int(input())

dp = [[0] * 2 for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 2

for n in range(2, N+1):
    dp[n][0] = (dp[n-1][0] + dp[n-1][1]) % 9901
    dp[n][1] = (dp[n-1][0] * 2 + dp[n-1][1]) % 9901

print(sum(dp[N]) % 9901)