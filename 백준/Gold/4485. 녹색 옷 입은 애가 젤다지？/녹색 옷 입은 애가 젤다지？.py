import sys
import heapq
num = 1

while True:
    N = int(sys.stdin.readline().rstrip('\n'))
    if not N:
        break
    grid = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for _ in range(N)]
    pq = [(grid[0][0], 0, 0)]
    while pq:
        v, y, x = heapq.heappop(pq)
        if y == N-1 and x == N-1:
            print(f'Problem {num}: {v}')
            break
        for ny, nx in [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]:
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] != -1:
                heapq.heappush(pq,(v + grid[ny][nx], ny, nx))
                grid[ny][nx] = -1
    num += 1
