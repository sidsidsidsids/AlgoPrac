from collections import deque
import sys
N, M = map(int,sys.stdin.readline().rstrip("\n").split())
height = list(map(int,sys.stdin.readline().rstrip("\n").split()))
graph = dict()
for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip("\n").split())
    if height[a-1] > height[b-1]:
        if a not in graph:
            graph[a] = set()
        graph[a].add(b)
    else:
        if b not in graph:
            graph[b] = set()
        graph[b].add(a)

arr = [1] * (N+1)

Q = deque()
for elem in graph.keys():
    Q.append((elem, 1))

while Q:
    pos, cnt = Q.popleft()
    if arr[pos] > cnt:
        continue
    if pos in graph:
        for next_path in graph[pos]:
            if arr[next_path] < cnt + 1:
                arr[next_path] = cnt + 1
                Q.append((next_path, cnt + 1))

for i in range(1,N+1):
    print(arr[i])