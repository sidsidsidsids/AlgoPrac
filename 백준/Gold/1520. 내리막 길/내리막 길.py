M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

def func(y, x):
    if y == M-1 and x == N-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]

    cnt = 0
    for ny, nx in [[y-1, x],[y, x+1],[y+1, x],[y, x-1]]:
        if 0 <= ny < M and 0 <= nx < N:
            if arr[y][x] > arr[ny][nx]:
                cnt += func(ny, nx)

    dp[y][x] = cnt
    return dp[y][x]

ans = func(0, 0)
print(ans)