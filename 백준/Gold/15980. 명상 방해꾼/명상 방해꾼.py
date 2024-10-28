import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [[] for _ in range(N)]
L = [0] * M
R = [0] * M
for n in range(N):
    arr[n] = list(sys.stdin.readline().rstrip('\n').split())
    S = arr[n][0]
    arr[n][1] = list(map(int, arr[n][1]))
    cnt = 0
    for m in range(M):
        cnt += arr[n][1][m]
        if S == "L":
            L[m] += cnt
        else:
            R[m] += cnt

result = sys.maxsize
target = -1
for n in range(N):
    cnt = 0
    tmp = 0
    for m in range(M):
        cnt += arr[n][1][m]
        if arr[n][0] == "L":
            tmp = max(tmp, abs(L[m] - cnt - R[m]))
        else:
            tmp = max(tmp, abs(L[m] + cnt - R[m]))
    if tmp < result:
        result = tmp
        target = n + 1

print(target)
print(result)