n, k = map(int,input().split())
dp = [k+1] * (k+1)
coin = [0] * n
for N in range(n):
    v = int(input())
    coin[N] = v
dp[0] = 0
for i in range(1, k+1):
    for c in coin:
        if i - c >= 0:
            dp[i] = min(dp[i], 1+dp[i - c])

print(dp[-1] if dp[-1] != k+1 else -1)