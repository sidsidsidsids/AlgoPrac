import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip('\n'))
for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    graph = defaultdict(dict)
    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().rstrip('\n').split())
        graph[x][y] = z
        graph[y][x] = z

    visit = [0] * M
    cheapest = sys.maxsize
    answer = [-1]
    def dfs(current, cost, record):
        global answer
        global cheapest

        if cost >= cheapest:
            return
        if current == M-1:
            if cost < cheapest:
                answer = record[:]
                cheapest = cost
            return
        for key, value in graph[current].items():
            if not visit[key]:
                visit[key] = 1
                record.append(key)
                dfs(key, cost + value, record[:])
                record.pop()
                visit[key] = 0
    dfs(0, 0, [0])
    print(f'Case #{t}:', end=" ")
    print(*answer)