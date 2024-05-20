import sys
N, M = map(int,sys.stdin.readline().rstrip('\n').split())
arr = [list(map(int,sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
answer = 0
for n in range(N):
    if arr[n][0]:
        dp[n][0] = 1
        answer = 1
for m in range(M):
    if arr[0][m]:
        dp[0][m] = 1
        answer = 1
for n in range(1, N):
    for m in range(1, M):
        if not arr[n][m]:
            dp[n][m] = 0
        else:
            l, lt, t = dp[n][m-1], dp[n-1][m-1], dp[n-1][m]
            if not l or not lt or not t:
                dp[n][m] = 1
            else:
                dp[n][m] = min(l, lt, t) + 1
            answer = max(answer, dp[n][m])
print(answer ** 2)
