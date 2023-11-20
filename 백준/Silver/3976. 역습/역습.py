import sys
t = int(sys.stdin.readline())
for tc in range(t):
    n, l1, l2, s1, s2 = map(int,sys.stdin.readline().split())
    firstPass = list(map(int,sys.stdin.readline().split()))
    firstDribble = list(map(int,sys.stdin.readline().split()))
    secondPass = list(map(int, sys.stdin.readline().split()))
    secondDribble = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = l1
    dp[1][0] = l2
    for idx in range(1,n):
        dp[0][idx] = min(dp[0][idx-1] + firstDribble[idx-1], dp[1][idx-1] + secondPass[idx-1])
        dp[1][idx] = min(dp[1][idx-1] + secondDribble[idx-1], dp[0][idx-1] + firstPass[idx-1])
    print(min(dp[0][n-1] + s1, dp[1][n-1] + s2))

