import sys

N, M, T = map(int, sys.stdin.readline().rstrip('\n').split())
works = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
times = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

dp = [[[-1] * (T + 1) for _ in range(M)] for _ in range(N)]

dp[0][0][0] = 0

for n in range(N):
    for m in range(M):
        if n == 0 and m == 0:
            continue
        for t in range(1, T+1):
            bt = t - 1 - times[n][m]
            if n > 0 and t > 0:
                dp[n][m][t] = max(dp[n][m][t], dp[n-1][m][t-1])
                if bt >= 0 and dp[n-1][m][bt] != -1:
                    dp[n][m][t] = max(dp[n][m][t], dp[n-1][m][bt] + works[n][m])
            if m > 0 and t > 0:
                dp[n][m][t] = max(dp[n][m][t], dp[n][m-1][t-1])
                if bt >= 0 and dp[n][m-1][bt] != -1:
                    dp[n][m][t] = max(dp[n][m][t], dp[n][m-1][bt] + works[n][m])
            if n > 0 and m > 0 and t > 0:
                dp[n][m][t] = max(dp[n][m][t], dp[n-1][m-1][t-1])
                if bt >= 0 and dp[n-1][m-1][bt] != -1:
                    dp[n][m][t] = max(dp[n][m][t], dp[n-1][m-1][bt] + works[n][m])

print(max(dp[N-1][M-1]))