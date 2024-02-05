N, M = map(int,input().split())
arr = list(map(int,input().split()))

l = 0
r = 0
cnt = arr[l]
if cnt >= M:
    print(1)
else:
    ans = N+1
    while l < N:
        if cnt < M:
            if r < N-1:
                r += 1
                cnt += arr[r]
            else:
                break
        else:
            if ans > r - l + 1:
                ans = r - l + 1
            cnt -= arr[l]
            l += 1
            if l > r:
                r += 1
    if ans == N+1:
        print(0)
    else:
        print(ans)