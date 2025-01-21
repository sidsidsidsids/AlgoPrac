import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0] * N for _ in range(N)]
for n in range(N):
    dp[n][n] = 1
    for k in range(n):
        if arr[k] == arr[n]:
            if k == n-1:
                dp[k][n] = 1
            elif dp[k+1][n-1]:
                dp[k][n] = 1
answer = []
M = int(sys.stdin.readline().strip())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().strip().split())
    S -= 1
    E -= 1
    answer.append(str(dp[S][E]))
print("\n".join(answer))