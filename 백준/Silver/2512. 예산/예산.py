N = int(input())
arr = list(map(int,input().split()))
money = int(input())

ans = 0
l = 0
r = max(arr)
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for elem in arr:
        cnt += min(elem, mid)
    if cnt <= money:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)
