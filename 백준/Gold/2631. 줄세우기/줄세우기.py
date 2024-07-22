import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [0] * N
for n in range(N):
    arr[n] = int(sys.stdin.readline().rstrip('\n'))

v = [1] * N
lis = 1
for i in range(N):
    target = arr[i]
    for j in range(i):
        if arr[j] < target:
            v[i] = max(v[j] + 1, v[i])
            lis = max(lis, v[i])
print(N - lis)