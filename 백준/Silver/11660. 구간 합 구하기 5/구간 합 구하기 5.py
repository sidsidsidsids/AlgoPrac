import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = arr[0][0]
for n in range(1, N):
    dp[0][n] += dp[0][n-1] + arr[0][n]
    dp[n][0] += dp[n-1][0] + arr[n][0]
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
answer = []
for _ in range(M):
    si, sj, ei, ej = map(int,input().split())
    si -= 1
    sj -= 1
    ei -= 1
    ej -= 1
    if si and sj:
        result = dp[ei][ej] - dp[si-1][ej] - dp[ei][sj - 1] + dp[si-1][sj - 1]
    else:
        if si:
            result = dp[ei][ej] - dp[si-1][ej]
        elif sj:
            result = dp[ei][ej] - dp[ei][sj - 1]
        else:
            result = dp[ei][ej]
    answer.append(result)
for ans in answer:
    print(ans)