import sys
from collections import deque

M, S = map(int, sys.stdin.readline().rstrip('\n').split(":"))
time = int(M * 6 + S / 10)
if time == 3:
    print(1)
elif time == 1 or time == 6 or time == 60:
    print(2)
else:
    graph = [[0] * 361 for _ in range(2)]
    for i in [1, 6, 60]:
        graph[0][i] = 1
    graph[1][3] = 1
    Q = deque()
    for elem in (3, 1), (1, 0), (6, 0), (60, 0):
        Q.append(elem)

    flag = False
    while Q:
        t, i = Q.popleft()

        if i == 1:
            for n in t + 1, t + 3, t + 6, t + 60:
                if n == time:
                    print(graph[1][t] + 1)
                    flag = True
                    break
                if n <= 360 and not graph[1][n]:
                    graph[1][n] = graph[1][t] + 1
                    Q.append((n, 1))
        else:
            for n in t + 1, t + 6, t + 60:
                if n == time:
                    print(graph[0][t] + 2)
                    flag = True
                    break
                if n <= 360 and not graph[0][n]:
                    graph[0][n] = graph[0][t] + 1
                    Q.append((n, 0))

        if flag:
            break