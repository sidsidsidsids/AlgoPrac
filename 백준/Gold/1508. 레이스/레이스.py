N, M, K = map(int,input().split())
arr = list(map(int,input().split()))
bot = 0
top = N
start_idx = 0
target_idx = 1
result = set()
while bot <= top:
    mid = (top + bot) // 2
    while target_idx < K and len(result) < M:
        if arr[target_idx] - arr[start_idx] >= mid:
            result.add(start_idx)
            result.add(target_idx)
            start_idx = target_idx
        target_idx += 1
    if len(result) < M:
        top = mid - 1
    else:
        ans = result
        bot = mid + 1
    result = set()
    start_idx = 0
    target_idx = 1
ans_arr = [0] * K
for idx in ans:
    ans_arr[idx] = 1
for elem in ans_arr:
    print(elem,end="")

