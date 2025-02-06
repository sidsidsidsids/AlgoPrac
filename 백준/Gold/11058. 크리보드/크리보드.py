import sys

N = int(sys.stdin.readline().strip())
dp = [0] * (N+1)
if N <= 3:
    print(N)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4, N+1):
        dp[i] = dp[i-1] + 1
        for j in range(2, N+1):
            if i - (j+1) <= 0:
                break
            dp[i] = max(dp[i - j] * (j-1), dp[i])
    print(dp[N])