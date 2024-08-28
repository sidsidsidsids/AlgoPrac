import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())

arr = []
for n in range(N):
    s, e = map(int, sys.stdin.readline().rstrip('\n').split())
    arr.append((s, e, n))

arr.sort(key=lambda X: (X[1], X[0], X[2]))

day = [0] * 32
schedule = [0] * N

for s, e, i in arr:
    for d in range(s, e+1):
        if day[d] < K:
            day[d] += 1
            schedule[i] = d
            break

for elem in schedule:
    print(elem)
