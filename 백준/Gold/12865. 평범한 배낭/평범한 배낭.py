N, K = map(int, input().split())
stuff = [[0, 0] for _ in range(N)]

for n in range(N):
    weight, value = map(int, input().split())
    stuff[n] = [weight, value]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = stuff[i - 1]
    for w in range(1, K + 1):
        if weight <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])