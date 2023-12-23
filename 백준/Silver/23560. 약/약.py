N = int(input())
dp = [0] * 15
dp[0] = 2
for i in range(1,15):
    dp[i] = dp[i-1] * 3
print(dp[N-1])