N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dp[0][0] = arr[0][0]
for m in range(1, M):
    dp[0][m] = dp[0][m-1] + arr[0][m]

for n in range(1, N):
    left = [0] * M
    for m in range(M):
        if m == 0:
            left[m] = dp[n-1][m] + arr[n][m]
        else:
            left[m] = max(left[m - 1], dp[n - 1][m]) + arr[n][m]
    right = [0] * M
    for m in range(M-1,-1,-1):
        if m == M-1:
            right[m] = dp[n - 1][m] + arr[n][m]
        else:
            right[m] = max(right[m + 1], dp[n - 1][m]) + arr[n][m]
    for m in range(M):
        dp[n][m] = max(left[m], right[m])

print(dp[-1][-1])
