from collections import deque
N = int(input())
dp = [0] * (N+1)
cur = deque()
cur.append(N)
while True:
    elem = cur.popleft()
    if elem == 1:
        break
    if not elem % 3 and not dp[elem // 3]:
        dp[elem // 3] = dp[elem] + 1
        cur.append(elem // 3)
    if not elem % 2 and not dp[elem // 2]:
        dp[elem // 2] = dp[elem] + 1
        cur.append(elem // 2)
    if not dp[elem - 1]:
        dp[elem - 1] = dp[elem] + 1
        cur.append(elem - 1)
print(dp[1])