N, M = map(int,input().split())
memory = list(map(int,input().split()))
cost = list(map(int,input().split()))

max_time = 100 * N
dp = [[0] * N for _ in range(max_time+1)]

if memory[0] >= M:
    ans = cost[0]
else:
    ans = max_time

for t in range(max_time+1):
    if cost[0] <= t:
        dp[t][0] = memory[0]
    else:
        pass

for n in range(1, N):
    for t in range(max_time+1):
        if cost[n] <= t:
            dp[t][n] = max(dp[t][n-1], dp[t-cost[n]][n-1] + memory[n])
        else:
            dp[t][n] = dp[t][n-1]
        if dp[t][n] >= M:
            if t < ans:
                ans = t
            break
print(ans)