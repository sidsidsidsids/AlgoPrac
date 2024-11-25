from collections import deque

K, H, L = map(int, input().split())
graph = [[] for _ in range((3 * K * (K - 1) + 1) + 1)]

t = 0
for k in range(K, K * 2):
    if t == 0:
        for i in range(1, k + 1):
            if i == 1:
                graph[i].append(i + 1)
            elif i == k:
                graph[i].append(i - 1)
            else:
                graph[i].append(i + 1)
                graph[i].append(i - 1)
    else:
        for i in range(1, k + 1):
            if i == 1:
                graph[t + i].append(t + i + 1)
                graph[t + i].append(t + i - (k - 1))
                graph[t + i - (k - 1)].append(t + 1)
            elif i == k:
                graph[t + i].append(t + i - 1)
                graph[t + i].append(t + i - k)
                graph[t + i - k].append(t + i)
            else:
                graph[t + i].append(t + i + 1)
                graph[t + i].append(t + i - 1)
                graph[t + i].append(t + i - (k - 1))
                graph[t + i].append(t + i - k)
                graph[t + i - (k - 1)].append(t + i)
                graph[t + i - k].append(t + i)
    t += k
for k in range(K * 2 - 2, K - 1, -1):
    for i in range(1, k + 1):
        if i == 1:
            graph[t + i].append(t + i + 1)
            graph[t + i].append(t + i - k)
            graph[t + i].append(t + i - (k + 1))
        elif i == k:
            graph[t + i].append(t + i - 1)
            graph[t + i].append(t + i - k)
            graph[t + i].append(t + i - (k + 1))
        else:
            graph[t + i].append(t + i + 1)
            graph[t + i].append(t + i - 1)
            graph[t + i].append(t + i - k)
            graph[t + i].append(t + i - (k + 1))
        graph[t + i - k].append(t + i)
        graph[t + i - (k + 1)].append(t + i)
    t += k

visit = [0] * ((3 * K * (K - 1) + 1) + 1)
Q = deque()
Q.append(H)
visit[H] = 1
depth = 0
space = 1
while Q:
    elem = Q.popleft()
    space -= 1
    for node in graph[elem]:
        if not visit[node]:
            visit[node] = 1
            Q.append(node)
    if space == 0:
        space = len(Q)
        depth += 1
    if depth == L:
        break
Q = sorted(Q)
print(space)
for elem in Q:
    print(elem)