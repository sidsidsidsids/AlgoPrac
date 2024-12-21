import sys

M, N, L = map(int, sys.stdin.readline().rstrip('\n').split())
pos = list(map(int, sys.stdin.readline().rstrip('\n').split()))
pos = sorted(pos)
ans = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split())
    l = 0
    r = M-1
    while l <= r:
        m = (l + r) // 2
        t = pos[m]
        if abs(x-t) + y <= L:
            ans += 1
            break
        if x == t:
            break
        elif x < t:
            r = m - 1
        elif x > t:
            l = m + 1
print(ans)