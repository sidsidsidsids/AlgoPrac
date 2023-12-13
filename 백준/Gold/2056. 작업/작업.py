from collections import deque
import copy

N = int(input())

time = [0] * (N+1)
path = [[] for _ in range(N+1)]
cond = [set() for _ in range(N+1)]
for n in range(1,N+1):
    inputs = list(map(int,input().split()))
    time[n] = inputs[0]
    for elem in inputs[2:]:
        path[elem].append(n)
        cond[n].add(elem)

Q = deque()
V = [0] * (N+1)
curT = [0] * (N+1)
curC = copy.deepcopy(cond)

for idx in range(1,N+1):
    if len(cond[idx]) == 0:
        Q.append(idx)

while Q:
    elem = Q.popleft()
    V[elem] = 1
    curT[elem] += time[elem]
    for nelem in path[elem]:
        curC[nelem].remove(elem)
        if len(curC[nelem]) == 0 and not V[nelem]:
            Q.append(nelem)
            for belem in cond[nelem]:
                value = curT[belem]
                if value > curT[nelem]:
                    curT[nelem] = value
print(max(max(time),max(curT)))

