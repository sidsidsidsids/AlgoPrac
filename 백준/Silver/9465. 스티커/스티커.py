import sys

t = int(sys.stdin.readline())
result = []
for tc in range(t):
    n = int(sys.stdin.readline())
    dp = []
    first = list(map(int,sys.stdin.readline().split()))
    second = list(map(int,sys.stdin.readline().split()))
    for idx in range(n):
        dp.append([first[idx], second[idx]])

    for idx in range(1, n):
        if idx < 2:
            dp[idx][0] = dp[idx-1][1] + dp[idx][0]
            dp[idx][1] = dp[idx-1][0] + dp[idx][1]
        else:
            dp[idx][0] = max(dp[idx-1][1]+dp[idx][0],dp[idx-2][1]+dp[idx][0])
            dp[idx][1] = max(dp[idx - 1][0] + dp[idx][1], dp[idx - 2][0] + dp[idx][1])

    result.append(max(dp[n-1]))

for res in result:
    print(res)