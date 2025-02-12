import sys
import heapq
from collections import defaultdict

N = int(sys.stdin.readline().strip())
hashmap = defaultdict(list)
answer = 0
for _ in range(N):
    Q = list(sys.stdin.readline().strip().split())
    target = Q[1]
    if Q[0] == '1':
        for e in Q[3:]:
            heapq.heappush(hashmap[target], -int(e))
    elif Q[0] == '2':
        b = int(Q[2])
        if target in hashmap and hashmap[target]:
            for _ in range(b):
                if hashmap[target]:
                    answer -= heapq.heappop(hashmap[target])
                else:
                    break
print(answer)