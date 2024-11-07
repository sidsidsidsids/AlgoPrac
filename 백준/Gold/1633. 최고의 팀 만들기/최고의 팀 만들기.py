import sys

arr = []
while True:
    try:
        W, B = map(int, sys.stdin.readline().rstrip('\n').split())
        arr.append((W, B))
    except:
        break

L = len(arr)
dp = [[[0] * 16 for _ in range(16)] for _ in range(L + 1)]

for i in range(L):
    for w in range(16):
        for b in range(16):
            if w+1 <= 15:
                dp[i+1][w+1][b] = max(dp[i+1][w+1][b], dp[i][w][b] + arr[i][0])
            if b+1 <= 15:
                dp[i+1][w][b+1] = max(dp[i+1][w][b+1], dp[i][w][b] + arr[i][1])
            dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])

print(dp[L][15][15])