import sys

H, N = map(int, sys.stdin.readline().strip().split())
records = []
for _ in range(N):
    records.append(tuple(map(int, sys.stdin.readline().strip().split())))

dp = [-1] * (H+1)
dp[0] = 100001
for h, s in records:
    for n in range(H, h-1, -1):
        if dp[n-h] != -1:
            dp[n] = max(dp[n], min(dp[n-h], s))
print(dp[H])