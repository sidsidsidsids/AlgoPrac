import sys
from collections import deque

T = int(sys.stdin.readline().rstrip('\n'))
for t in range(1, T+1):
    if t != 1:
        print()
    M, N, P = map(int, sys.stdin.readline().rstrip('\n').split())

    legs = list(sys.stdin.readline().rstrip('\n').split())
    path = [[] for _ in range(N)]
    addr = dict()
    for m in range(M):
        addr[legs[m]] = m

    for n in range(N):
        s, e = sys.stdin.readline().rstrip('\n').split()
        si, ei = addr[s], addr[e]
        path[si].append(ei)
        path[ei].append(si)

    answer = [0] * P
    for p in range(P):
        size, start, end = sys.stdin.readline().rstrip('\n').split()
        size = int(size)
        si, ei = addr[start], addr[end]
        Q = deque()
        V = [0] * M
        Q.append(si)
        V[si] = 1
        dist = 0
        Q_size = 1
        flag = False
        while Q:
            elem = Q.popleft()
            Q_size -= 1
            if elem == ei:
                flag = True
                break

            if path and path[elem]:
                for nelem in path[elem]:
                    if not V[nelem]:
                        Q.append(nelem)
                        V[nelem] = 1

            if Q_size == 0:
                dist += 1
                Q_size = len(Q)

        if flag:
            answer[p] = dist * size * 100

    print(f'DATA SET {t}')
    print()
    for amount in answer:
        if amount != 0:
            print(f'${amount}')
        else:
            print('NO SHIPMENT POSSIBLE')