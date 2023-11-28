from collections import deque
import sys
N, M, K, X = map(int,sys.stdin.readline().split())
way = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int,sys.stdin.readline().split())
    way[a].append(b)
V = [0] * (N+1)

Q = deque()
Q.append(X)
V[X] = 1
dist = 0
lenQ = 1
answer = -1
while Q:
    elem = Q.popleft()
    lenQ -= 1
    for nelem in way[elem]:
        if not V[nelem]:
            Q.append(nelem)
            V[nelem] = 1
    if lenQ == 0:
        lenQ = len(Q)
        dist += 1
        if dist == K:
            if lenQ:
                answer = Q
            else:
                pass
            break
if type(answer) != int:
    answer = sorted(answer)
    for ans in answer:
        print(ans)
else:
    print(answer)