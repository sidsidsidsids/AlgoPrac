import sys

N, H = map(int, sys.stdin.readline().rstrip('\n').split())

suppliers = [() for _ in range(N)]
INF = sys.maxsize
MH = 0

for n in range(N):
    P, C = map(int, sys.stdin.readline().rstrip('\n').split())
    suppliers[n] = (P, C)
    MH = max(MH, P)

MH += H
dp = [[INF] * (MH + 1) for _ in range(N + 1)]
dp[0][0] = 0
for n in range(1, N+1):
    size, cost = suppliers[n-1]
    for h in range(MH+1):
        if h - size < 0:
            dp[n][h] = dp[n-1][h]
        else:
            dp[n][h] = min(dp[n-1][h], dp[n][h - size] + cost)

answer = INF
for h in range(H, MH):
    answer = min(dp[N][h], answer)
print(answer)