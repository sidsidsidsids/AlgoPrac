import sys
import heapq
N = int(sys.stdin.readline().rstrip('\n'))
a = []
output = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip('\n'))
    if x == 0:
        if not a:
            output.append(0)
        else:
            output.append(heapq.heappop(a)[1])
    else:
        heapq.heappush(a, (abs(x), x))
for e in output:
    print(e)