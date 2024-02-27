N = int(input())
arr = sorted(list(map(int,input().split())))
ans = 200000
for idx in range(N):
    val = arr[idx] + arr[-(idx+1)]
    if val < ans:
        ans = val
print(ans)