import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
bit_HM = dict()
for n in range(1, N+1):
    bin_code = sys.stdin.readline().strip()
    target = int(bin_code, 2)
    for i in range(K):
        neighbor = target ^ (1 << i)
        if neighbor in bit_HM:
            for j in bit_HM[neighbor]:
                graph[j].append(n)
                graph[n].append(j)
    if target not in bit_HM:
        bit_HM[target] = []
    bit_HM[target].append(n)

visit = [-1] * (N+1)
Q = deque()
Q.append(1)
visit[1] = 0
while Q:
    elem = Q.popleft()
    for node in graph[elem]:
        if visit[node] == -1:
            Q.append(node)
            visit[node] = elem

M = int(sys.stdin.readline().strip())
answers = []
for _ in range(M):
    J = int(sys.stdin.readline().strip())
    if visit[J] != -1:
        path = []
        node = J
        while visit[node] != -1:
            path.append(node)
            node = visit[node]
        answers.append(path[::-1])
    else:
        answers.append([-1])
for answer in answers:
    print(*answer)