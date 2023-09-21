K, N = map(int,input().split())
LAN = [0] * K
for k in range(K):
    LAN[k] = int(input())

l = 1
r = max(LAN)
ans = 0
while l <= r:
    m = (l + r) // 2
    cnt = 0
    for line in LAN:
        cnt += line // m
    if N <= cnt:
        ans = m
        l = m + 1
    else:
        r = m - 1
print(ans)
