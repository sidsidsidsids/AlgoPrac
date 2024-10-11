import sys

dp = [[0] * 10 for _ in range(64)]
answer = [0] * 64
for j in range(10):
    dp[0][j] = 1
answer[0] = sum(dp[0])

for i in range(1, 64):
    dp[i][0] = answer[i-1]
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
    answer[i] = sum(dp[i])

P = int(sys.stdin.readline().rstrip('\n'))
for _ in range(P):
    print(answer[int(sys.stdin.readline().rstrip('\n')) - 1])