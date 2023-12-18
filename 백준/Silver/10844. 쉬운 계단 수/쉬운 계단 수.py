dp = [[0] * 10 for _ in range(100)]
for j in range(1, 10):
    dp[0][j] = 1

for i in range(1, 100):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # dp[i][j] %= 1000000000

print(sum(dp[int(input()) - 1]) % 1000000000)