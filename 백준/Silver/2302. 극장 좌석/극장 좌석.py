N = int(input())
dp = [1] * (N+1)
for n in range(2, N+1):
    dp[n] = dp[n-1] + dp[n-2]

vip = [0] * N
M = int(input())
for _ in range(M):
    vip[int(input())-1] = 1

answer = 1
cnt = 0
for n in range(N):
    if not vip[n]:
        cnt += 1
    else:
        answer *= dp[cnt]
        cnt = 0
if cnt:
    answer *= dp[cnt]
print(answer)