import sys
N = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int,sys.stdin.readline().rstrip('\n').split()))
ans = arr[N-1]
dp = [[0] * (N-1) for _ in range(21)]
dp[arr[0]][0] = 1

for j in range(N-2):
    for i in range(21):
        if dp[i][j]:
            plus = i + arr[j + 1]
            if plus <= 20:
                dp[plus][j + 1] += dp[i][j]
            minus = i - arr[j + 1]
            if minus >= 0:
                dp[minus][j + 1] += dp[i][j]

print(dp[arr[N-1]][N-2])