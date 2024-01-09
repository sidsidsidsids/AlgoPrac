T, W = map(int,input().split())
arr = [0] * T
for t in range(T):
    arr[t] = int(input())
if T == 1:
    ans = 1
else:
    dp = [[[0] * T for _ in range(2)] for _ in range(W + 1)]
    dp[0][0][0] = 1 if arr[0] == 1 else 0
    dp[1][1][0] = 1 if arr[0] == 2 else 0
    ans = 0

    for i in range(1, T):
        for w in range(W + 1):
            if w == 0:
                if arr[i] == 1:
                    dp[w][0][i] = dp[w][0][i-1] + 1
                else:
                    dp[w][0][i] = dp[w][0][i-1]
            else:
                if arr[i] == 1:
                    dp[w][0][i] = max(dp[w-1][1][i-1], dp[w][0][i-1]) + 1
                    dp[w][1][i] = max(dp[w-1][0][i-1], dp[w][1][i-1])
                else:
                    dp[w][0][i] = max(dp[w-1][1][i-1], dp[w][0][i-1])
                    dp[w][1][i] = max(dp[w-1][0][i-1], dp[w][1][i-1]) + 1
            if i == T-1:
                ans = max(dp[w][0][i], dp[w][1][i], ans)
print(ans)