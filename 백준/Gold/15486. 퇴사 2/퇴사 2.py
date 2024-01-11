import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N+1)
ans = 0
for n in range(1, N+1):
    day, profit = map(int,input().split())
    if n + (day - 1) < N+1:
        dp[n + (day - 1)] = max(dp[n - 1] + profit, dp[n + (day-1)])
    dp[n] = max(dp[n-1],dp[n])
    if dp[n] > ans:
        ans = dp[n]
print(ans)