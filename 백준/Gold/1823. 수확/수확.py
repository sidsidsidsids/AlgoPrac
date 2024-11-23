import sys
sys.setrecursionlimit(2000^2 + 1)

N = int(sys.stdin.readline().rstrip('\n'))
H = []
for _ in range(N):
    H.append(int(sys.stdin.readline().rstrip('\n')))
dp = [[0] * N for _ in range(N)]

def func(l: int, r: int, depth: int):
    if l > r:
        return 0
    if dp[l][r]:
        return dp[l][r]
    dp[l][r] = max(func(l + 1, r, depth + 1) + H[l] * depth, func(l, r - 1, depth + 1) + H[r] * depth)
    return dp[l][r]

print(func(0, N-1, 1))