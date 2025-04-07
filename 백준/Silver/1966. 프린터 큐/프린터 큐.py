import sys
from collections import deque, defaultdict

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    Q = deque(enumerate(map(int, sys.stdin.readline().strip().split())))
    H = defaultdict(int)
    S = set()
    for elem in Q:
        H[elem[1]] += 1
        S.add(elem[1])
    S = sorted(list(S), reverse=True)
    S.append(0)
    i = 0
    c = 0
    A = -1
    while Q:
        if Q[0][1] == S[i]:
            c += 1
            if Q[0][0] == M:
                A = c
                break
            H[S[i]] -= 1
            if not H[S[i]]:
                i += 1
            Q.popleft()
        else:
            Q.append(Q.popleft())
    print(A)