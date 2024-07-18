import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [0] * N
for n in range(N):
    arr[n] = int(sys.stdin.readline().rstrip('\n'))
arr.sort(reverse=True)

i = 1
ans = 1
maxima = arr[0] + 1
for n in range(1, N):
    if arr[n] + N >= maxima:
        ans += 1
    maxima = max(maxima, arr[n] + (n + 1))

print(ans)