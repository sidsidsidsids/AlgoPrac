import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
arr = [[] for _ in range(N)]
for n in range(N):
    arr[n] = list(sys.stdin.readline().rstrip('\n').split())

answer = -1
minima = sys.maxsize
for n in range(N):
    value = 0
    maxval = 0
    for m in range(M):
        for nn in range(N):
            if nn == n:
                continue
            pos, ans = arr[nn]
            if ans[m] == "1":
                if pos == "L":
                    value -= 1
                elif pos == "R":
                    value += 1
        maxval = max(maxval, abs(value))
    if maxval < minima:
        answer = n + 1
        minima = maxval

print(answer)
print(minima)
