import sys
import heapq
N, T = map(int,input().split())
farm = [list(map(int,input().split())) for _ in range(N)]
d = [(3, 0), (2, 1), (1, 2), (0, 3), (-1, 2), (-2, 1), (-3, 0), (-2, -1), (-1, -2), (0, -3), (1, -2), (2, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]
INF = sys.maxsize
dist = [[INF] * N for _ in range(N)]

answer = INF
Q = [(0, 0, 0)]
while Q:
    time, i, j = heapq.heappop(Q)
    if time > dist[i][j]:
        continue
    rest = (N-1 - i) + (N-1 - j)
    if rest <= 2:
        answer = min(answer, time + rest * T)

    for di, dj in d:
        if 0 <= i + di < N and 0 <= j + dj < N:
            distance = time + (T * 3) + farm[i+di][j+dj]

            if dist[i + di][j + dj] > distance:
                dist[i + di][j + dj] = distance
                heapq.heappush(Q, (distance, i + di, j + dj))
print(answer)