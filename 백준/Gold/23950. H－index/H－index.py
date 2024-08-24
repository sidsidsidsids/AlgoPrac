import sys
import heapq

T = int(sys.stdin.readline().rstrip('\n'))
for t in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    h = 0
    pq = []
    ans = [0] * N

    for n in range(N):
        elem = arr[n]
        if elem > h:
            heapq.heappush(pq, elem)
        if len(pq) >= h + 1:
            h += 1
            while pq and pq[0] <= h:
                heapq.heappop(pq)
        ans[n] = h

    print(f"Case #{t+1}:", *ans)