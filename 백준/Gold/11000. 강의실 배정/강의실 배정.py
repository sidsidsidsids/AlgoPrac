import sys
import heapq
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    s, e = map(int,sys.stdin.readline().split())
    arr.append((s, e))
arr.sort(key = lambda X:(X[0], X[1]))

heap = []
heapq.heappush(heap, arr[0][1])
for n in range(1, N):
    if arr[n][0] < heap[0]:
        heapq.heappush(heap, arr[n][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[n][1])
print(len(heap))