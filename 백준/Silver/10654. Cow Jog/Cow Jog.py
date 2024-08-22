import sys

N, T = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]

answer = 1

pos = arr[-1][0] + arr[-1][1] * T

for n in range(N-2, -1, -1):
    cur = arr[n][0] + arr[n][1] * T
    if cur < pos:
        answer += 1
        pos = cur

print(answer)