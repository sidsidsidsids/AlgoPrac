import sys

N, M = map(int, sys.stdin.readline().strip().split())
want = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    want[u].append(v)
    want[v].append(u)

mate = 0
mated = [0] * (N+1)
def func(idx, cnt):
    global mate
    if cnt < mate - (N - (idx-1)):
        return
    if idx == N+1:
        if mate < cnt:
            mate = cnt
        return
    if mated[idx]:
        func(idx+1, cnt)
    else:
        for elem in want[idx]:
            if not mated[elem]:
                mated[idx] = 1
                mated[elem] = 1
                func(idx+1, cnt+1)
                mated[elem] = 0
                mated[idx] = 0
        func(idx+1, cnt)

func(1, 0)
print(mate * 2 + 1 if mate * 2 < N else mate * 2)