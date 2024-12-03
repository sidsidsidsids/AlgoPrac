import sys
import heapq
from collections import defaultdict

N = int(sys.stdin.readline().rstrip('\n'))
hm = defaultdict(list)
Q = []
md = -1
for _ in range(N):
    p, d = map(int, sys.stdin.readline().rstrip('\n').split())
    hm[d].append(p)
    md = max(md, d)

money = 0
while md > 0:
    if md in hm:
        for elem in hm[md]:
            heapq.heappush(Q, -elem)
    if Q:
        money -= heapq.heappop(Q)
    md -= 1
print(money)