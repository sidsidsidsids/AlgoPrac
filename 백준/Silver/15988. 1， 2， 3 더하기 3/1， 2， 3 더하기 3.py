N = int(input())
ans = []
dp = [0] * 1000000
dp[0] = 1
dp[1] = 2
dp[2] = 4
for n in range(3,1000000):
    dp[n] = dp[n-1]%1000000009 + dp[n-2]%1000000009 + dp[n-3]%1000000009

for _ in range(N):
    ans.append(dp[int(input())-1]%1000000009)

for a in ans:
    print(a)