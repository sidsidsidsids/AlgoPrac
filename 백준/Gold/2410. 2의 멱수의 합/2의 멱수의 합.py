import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [0] * (N + 1)
d = 1000000000
for i in range(N+1):
    if 2 ** i > N:
        break
    k = 2 ** i
    arr[k] += 1
    for l in range(k + 1, N + 1):
        arr[l] += arr[l - k]
        arr[l] %= d

print(arr[N])