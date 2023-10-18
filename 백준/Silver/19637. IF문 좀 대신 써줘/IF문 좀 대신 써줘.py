import sys

N, M = map(int,sys.stdin.readline().split())
name = [[] for _ in range(N)]
for n in range(N):
    a, b = sys.stdin.readline().split()
    name[n] = [a, int(b)]
s = 0
e = N-1
for _ in range(M):
    power = int(sys.stdin.readline())
    l = s
    r = e
    output = name[0][0]
    while l <= r:
        mid = (l+r) // 2
        if power <= name[mid][1]:
            output = name[mid][0]
            r = mid - 1
        else:
            l = mid + 1
    print(output)