N = list(input())
I = len(N)
dp = [[0] * I for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 0
for i in range(1, I):
    s = int(N[i])
    d = int(N[i-1] + N[i])

    if s == 0:
        dp[0][i] = 0
    else:
        dp[0][i] = dp[0][i-1] + dp[1][i-1]

    if N[i-1] == '0':
        pass
    elif d <= 34:
        dp[1][i] = dp[0][i-1]
    else:
        pass

print(dp[0][I-1] + dp[1][I-1])
