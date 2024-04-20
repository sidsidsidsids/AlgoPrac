N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
maxima = 100 * N + 1
dp = [[[maxima, maxima, maxima] for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if n == 0:
            for k in range(3):
                dp[n][m][k] = arr[n][m]
        elif n == 1:
            for k in range(3):
                if m == 0:
                    if k == 0:
                        dp[n][m][k] = arr[0][m+1] + arr[n][m]
                    elif k == 1:
                        dp[n][m][k] = arr[0][m] + arr[n][m]
                elif m == M-1:
                    if k == 1:
                        dp[n][m][k] = arr[0][m] + arr[n][m]
                    elif k == 2:
                        dp[n][m][k] = arr[0][m - 1] + arr[n][m]
                else:
                    if k == 0:
                        dp[n][m][k] = arr[0][m + 1] + arr[n][m]
                    elif k == 1:
                        dp[n][m][k] = arr[0][m] + arr[n][m]
                    elif k == 2:
                        dp[n][m][k] = arr[0][m - 1] + arr[n][m]
        else:
            for k in range(3):
                if k == 0:
                    if m == M-1:
                        pass
                    else:
                        dp[n][m][0] = min(dp[n][m][0], min(dp[n-1][m+1][1], dp[n-1][m+1][2]) + arr[n][m])
                elif k == 1:
                    dp[n][m][1] = min(dp[n][m][1], min(dp[n-1][m][0], dp[n-1][m][2]) + arr[n][m])
                elif k == 2:
                    if m == 0:
                        pass
                    else:
                        dp[n][m][2] = min(dp[n][m][2], min(dp[n-1][m-1][0], dp[n-1][m-1][1]) + arr[n][m])

answer = maxima
for d in dp[N-1]:
    answer = min(answer, min(d))
print(answer)