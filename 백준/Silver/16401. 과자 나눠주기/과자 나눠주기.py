import sys
M, N = map(int,sys.stdin.readline().rstrip('\n').split())
L = list(map(int,sys.stdin.readline().rstrip('\n').split()))
L.sort()
l = 1
r = L[-1]
a = 0
while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for n in range(N-1, -1, -1):
        cnt += (L[n] // mid)
        if cnt >= M:
            a = mid
            l = mid + 1
            break
    else:
        r = mid - 1
print(a)