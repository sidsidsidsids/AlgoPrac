N = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0] * (N+1)
dp[1] = cards[1]
for n in range(2,N+1):
    dp[n] = cards[n]
    for i in range(1, n):
        dp[n] = max(dp[n], dp[i]+cards[n-i])
print(dp[N])