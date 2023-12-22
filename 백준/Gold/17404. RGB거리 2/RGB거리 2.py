N = int(input())
cost = [ list(map(int,input().split())) for _ in range(N) ]
dp = [[1001] * 3 for _ in range(N)]
answer = 1000 * N
for s in range(3):
    for e in range(3):
        if s == e:
            continue
        else:
            for i in range(N):
                for j in range(3):
                    if i == 0:
                        if j == s:
                            dp[i][j] = cost[i][j]
                        else:
                            dp[i][j] = 1001
                    elif i == N-1:
                        if j == s:
                            dp[i][j] = 1001 * N
                        else:
                            if j == 0:
                                dp[i][j] = cost[i][j] + min(dp[i - 1][1], dp[i - 1][2])
                            elif j == 1:
                                dp[i][j] = cost[i][j] + min(dp[i - 1][0], dp[i - 1][2])
                            elif j == 2:
                                dp[i][j] = cost[i][j] + min(dp[i - 1][0], dp[i - 1][1])
                    else:
                        if j == 0:
                            dp[i][j] = cost[i][j] + min(dp[i-1][1], dp[i-1][2])
                        elif j == 1:
                            dp[i][j] = cost[i][j] + min(dp[i-1][0], dp[i-1][2])
                        elif j == 2:
                            dp[i][j] = cost[i][j] + min(dp[i-1][0], dp[i-1][1])
            value = min(dp[-1])
            if answer > value:
                answer = value
print(answer)