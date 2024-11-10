import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
dp = [[] for _ in range(M)]
arr = list(sys.stdin.readline().rstrip('\n'))
dp[0] = arr[0]
for m in range(1, M):
    dp[m] = dp[m-1] + arr[m]
for n in range(1, N):
    arr = list(sys.stdin.readline().rstrip('\n'))
    dp[0] = dp[0] + arr[0]
    for m in range(1, M):
        dp[m] = min(dp[m], dp[m-1]) + arr[m]
print(dp[M-1])