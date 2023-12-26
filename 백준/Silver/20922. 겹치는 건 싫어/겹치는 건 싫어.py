N, K = map(int,input().split())
nums = list(map(int,input().split()))
if N == 1:
    print(1)
else:
    l = 0
    r = 1
    info = dict()
    info[nums[l]] = 1
    ans = 1
    cnt = 1
    moved = True
    while r < N:
        if moved:
            if nums[r] in info:
                info[nums[r]] += 1
            else:
                info[nums[r]] = 1
            cnt += 1
            if info[nums[r]] > K:
                moved = False
                cnt -= 1
            else:
                r += 1
        else:
            if info[nums[r]] <= K:
                moved = True
                cnt += 1
                r += 1
            else:
                info[nums[l]] -= 1
                l += 1
                cnt -= 1
        if cnt > ans:
            ans = cnt
        # print(l, r, info, cnt, ans)
    print(ans)
