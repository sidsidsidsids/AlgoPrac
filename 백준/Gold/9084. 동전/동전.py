T = int(input())
ans = [0] * T
for t in range(T):
    N = int(input())
    coin = list(map(int,input().split()))
    goal = int(input())
    dp = [0] * (goal + 1)
    dp[0] = 1
    for c in coin:
        for i in range(goal + 1):
            if i >= c:
                dp[i] += dp[i-c]
    ans[t] = dp[goal]
for a in ans:
    print(a)