import sys
import heapq

N, K = map(int,sys.stdin.readline().split())
gems = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

bags.sort()
gems.sort()

answer = 0
heap = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(heap, -gems[0][1])
        heapq.heappop(gems)
    if heap:
        answer -= heapq.heappop(heap)

print(answer)