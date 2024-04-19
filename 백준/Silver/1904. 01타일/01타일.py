N = int(input())
dp = [1] * (N+1)
for n in range(2, N+1):
    dp[n] = (dp[n-1] + dp[n-2]) % 15746
print(dp[N])