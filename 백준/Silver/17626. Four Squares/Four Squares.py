import math

n = int(input())
dp = [0, 1]

for x in range(2, n+1):
    minimum = n
    for i in range(1, int(math.sqrt(x)) + 1):
        minimum = min(minimum, dp[x - i**2])
    dp.append(minimum + 1)

print(dp[n])