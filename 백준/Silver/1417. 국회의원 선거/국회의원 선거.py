import sys
import heapq

N = int(sys.stdin.readline().strip())
target = int(sys.stdin.readline().strip())
PQ = []
for _ in range(N-1):
    heapq.heappush(PQ, -int(sys.stdin.readline().strip()))
count = 0
while PQ:
    elem = -heapq.heappop(PQ)
    if target > elem or elem == 0:
        break
    elem -= 1
    target += 1
    count += 1
    if target > elem and (PQ and target > -PQ[0]):
        break
    heapq.heappush(PQ, -elem)
print(count)