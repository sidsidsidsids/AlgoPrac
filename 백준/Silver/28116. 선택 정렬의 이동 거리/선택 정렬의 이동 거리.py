import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))
idx = [0] * (N + 1)
ans = [0] * N
for n in range(N):
    idx[arr[n]] = n+1
for n in range(1, N+1):
    if idx[n] == n:
        pass
    else:
        c = arr[n-1]
        arr[n-1], arr[idx[n]-1] = arr[idx[n]-1], arr[n-1]
        idx[n], idx[c] = idx[c], idx[n]
        dist = abs(idx[n] - idx[c])
        ans[n-1] += dist
        ans[c-1] += dist
print(*ans)