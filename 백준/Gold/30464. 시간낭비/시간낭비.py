N = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * N for _ in range(3)]
dp[0][0] = 0

for i in range(N-1):
    if dp[0][i] == -1:
        continue
    ni = i + arr[i]
    if 0 <= ni < N:
        dp[0][ni] = max(dp[0][i] + 1, dp[0][ni])

for i in range(N-2, -1, -1):
    dp[1][i] = max(dp[0][i], dp[1][i])
    if dp[1][i] == -1:
        continue
    ni = i - arr[i]
    if 0 <= ni < N:
        dp[1][ni] = max(dp[1][i] + 1, dp[1][ni])

for i in range(N-1):
    dp[2][i] = max(dp[1][i], dp[2][i])
    if dp[2][i] == -1:
        continue
    ni = i + arr[i]
    if 0 <= ni < N:
        dp[2][ni] = max(dp[2][i] + 1, dp[2][ni])

print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))