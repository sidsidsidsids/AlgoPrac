N, K = map(int,input().split())
arr = [0] * N
for n in range(N):
    loc = list(map(int,input().split()))
    arr[n] = loc
dp = [[4001 * N] * N for _ in range(K+1)]
dist = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        dist[i][j] = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])

dp[0][0] = 0
for j in range(1, N):
    dp[0][j] = dp[0][j-1] + dist[j-1][j]

for i in range(1, K+1):
    dp[i][0] = 0
    dp[i][i] = dist[0][i]
    for j in range(1, N):
        for k in range(i,0,-1):
            if j-k-1 < 0:
                continue
            dp[i][j] = min(dp[i][j], dp[i-k][j-k-1] + dist[j-k-1][j], dp[i][j-1] + dist[j-1][j])

print(dp[-1][-1])