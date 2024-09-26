import sys

N, M = map(int,sys.stdin.readline().rstrip('\n').split())
diff = abs(N - M)
if diff == 0:
    print(1)
else:
    dp = [[1] for _ in range(diff)]
    for i in range(1, diff):
        T = 1
        for e in dp[i-1][1:]:
            dp[i].append(dp[i][-1] + e)
            T += e
        dp[i].append(T)
    print(sum(dp[diff-1]))