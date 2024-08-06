import sys

INF = sys.maxsize
dp = [INF] * 101
dp[2] = 1; dp[3] = 7; dp[4] = 4; dp[5] = 2; dp[6] = 6; dp[7] = 8;
for i in range(8, 101):
    for j in range(2, 8):
        dp[i] = min(dp[i], dp[i-j] * 10 + (0 if j == 6 else dp[j]))

def maxima(num):
    value = ''
    if n % 2:
        value += '7'
        value += '1' * ((num // 2) - 1)
    else:
        value += '1' * (num // 2)
    return int(value)

def minima(num):
    return dp[num]

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    n = int(sys.stdin.readline().rstrip('\n'))
    print(minima(n), maxima(n))