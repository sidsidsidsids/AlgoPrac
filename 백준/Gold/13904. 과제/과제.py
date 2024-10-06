import sys
import heapq

T = int(sys.stdin.readline().rstrip('\n'))
arr = [[] for _ in range(T)]
for t in range(T):
    arr[t] = tuple(map(int, sys.stdin.readline().rstrip('\n').split()))
arr = sorted(arr, key = lambda X:(-X[0], -X[1]))

Q = []
while arr:
    d, w = arr.pop()
    heapq.heappush(Q, (w, d))
    if len(Q) > d:
        heapq.heappop(Q)

answer = 0
while Q:
    w, d = Q.pop()
    answer += w
print(answer)