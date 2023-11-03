N, K = map(int,input().split())
nums = [1] * (N+1)
cnt = 0
idx = 2
while True:
    for nidx in range(idx,N+1):
        if nums[nidx] and not nidx % idx:
            nums[nidx] = 0
            cnt += 1
            if cnt == K:
                ans = nidx
                break
    if cnt == K:
        break
    else:
        while nums[idx] != 1:
            idx += 1
print(ans)