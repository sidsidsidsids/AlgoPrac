import heapq
import sys

T = int(input())
answer = [[] for _ in range(T)]
for t in range(T):
    N = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    visit = [1] * N
    for n in range(N):
        action, value = sys.stdin.readline().rstrip("\n").split()
        if action == 'I':
            heapq.heappush(min_heap, (int(value), n))
            heapq.heappush(max_heap, (-int(value), n))
        else:
            if value == '-1':
                if min_heap:
                    visit[heapq.heappop(min_heap)[1]] = 0
            else:
                if max_heap:
                    visit[heapq.heappop(max_heap)[1]] = 0
        while min_heap and visit[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        while max_heap and visit[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
    if min_heap:
        answer[t] = [-max_heap[0][0], min_heap[0][0]]
    else:
        pass

for ans in answer:
    if ans:
        print(*ans)
    else:
        print('EMPTY')