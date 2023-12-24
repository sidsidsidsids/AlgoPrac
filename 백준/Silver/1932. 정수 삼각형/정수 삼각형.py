N = int(input())
triangle = [[0] * N for _ in range(N)]
for n in range(N):
    nums = list(map(int,input().split()))
    if n == 0:
        triangle[0][0] = nums[0]
    else:
        for j in range(n+1):
            if j == 0:
                triangle[n][j] = triangle[n-1][0] + nums[j]
            elif j == n:
                triangle[n][j] = triangle[n-1][n-1] + nums[j]
            else:
                triangle[n][j] = max(triangle[n-1][j-1], triangle[n-1][j]) + nums[j]
print(max(triangle[-1]))
