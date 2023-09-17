from collections import deque
N, K = map(int,input().split())

V = [0] * 100001;
G = [0] * 100001;

Q = deque();
Q.append(N);
V[N] = 1

while Q:
    elem = Q.popleft();
    for nElem in [elem-1, elem+1, elem*2]:
        if 0 <= nElem < 100001:
            if not V[nElem]:
                G[nElem] = G[elem] + 1
                V[nElem] = 1
                Q.append(nElem)
    if V[K]:
        break
print(G[K])


