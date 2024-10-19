import sys
from collections import deque

N, E = map(int, sys.stdin.readline().rstrip('\n').split())

path_0 = [[] for _ in range(N)]
path_1 = [[] for _ in range(N)]

for _ in range(E):
    A, B, V = map(int, sys.stdin.readline().rstrip('\n').split())
    if V == 0:
        path_0[A].append(B)
        path_0[B].append(A)
    else:
        path_1[A].append(B)
        path_1[B].append(A)

visit_0 = [0] * N
visit_1 = [0] * N

Q = deque()
Q.append((0, 0))
Q.append((0, 1))
L = 2
step = 0
visit_0[0] = 1
visit_1[0] = 1
flag = False
while Q:
    current, value = Q.popleft()
    L -= 1
    if current == N-1:
        flag = True
        break
    if value == 0:
        for node in path_1[current]:
            if not visit_1[node]:
                Q.append((node, 1))
                visit_1[node] = 1
    else:
        for node in path_0[current]:
            if not visit_0[node]:
                Q.append((node, 0))
                visit_0[node] = 1
    if L == 0:
        L = len(Q)
        step += 1

print(step if flag else -1)