import sys
import heapq

N = int(sys.stdin.readline().strip())
hq = []
answer = []
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if not hq:
            answer.append(0)
        else:
            answer.append(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -num)
print("\n".join(map(str, answer)))