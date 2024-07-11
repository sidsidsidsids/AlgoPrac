import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [0] * (N + 1)
for _ in range(N):
    s, e = map(int,sys.stdin.readline().rstrip('\n').split())
    for i in range(s, e+1):
        arr[i] += 1
answer = -1
for n in range(N, 0, -1):
    if arr[n] == n:
        answer = n
        break
print(answer)