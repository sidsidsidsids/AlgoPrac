dp = [1] * 10002
for n in range(2,10002):
    dp[n] += dp[n-2]
for n in range(3,10002):
    dp[n] += dp[n-3]
T = int(input())
for _ in range(T):
    print(dp[int(input())])