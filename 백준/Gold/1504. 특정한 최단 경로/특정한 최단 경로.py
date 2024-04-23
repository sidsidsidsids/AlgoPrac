import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

N, E = map(int,input().split())
path = dict()
for _ in range(E):
    s, e, c = map(int,input().split())
    if s in path:
        path[s][e] = c
    else:
        path[s] = dict()
        path[s][e] = c
    if e in path:
        path[e][s] = c
    else:
        path[e] = dict()
        path[e][s] = c

def dijk(start, end):
    V = [0] * (N+1)
    arr = [inf] * (N+1)
    V[start] = 1
    arr[start] = 0
    Q = [[start, arr[start]]]

    while Q:
        cur_pos, cur_cost = heapq.heappop(Q)
        if arr[cur_pos] < cur_cost:
            continue
        if cur_pos in path:
            for next_pos, next_cost in path[cur_pos].items():
                new_cost = cur_cost + next_cost
                if new_cost < arr[next_pos]:
                    arr[next_pos] = new_cost
                    heapq.heappush(Q, [next_pos, new_cost])

    if arr[end] != (1000 * N + 1):
        return arr[end]
    return -1

a, b = map(int,input().split())

ans = inf
s_to_a = dijk(1, a)
s_to_b = dijk(1, b)
ab = dijk(a, b)
a_to_e = dijk(a, N)
b_to_e = dijk(b, N)
if ab > -1:
    if s_to_a > -1 and b_to_e > -1:
        ans = min(ans, s_to_a + ab + b_to_e)
    if s_to_b > -1 and a_to_e > -1:
        ans = min(ans, s_to_b + ab + a_to_e)
if ans >= inf:
    print(-1)
else:
    print(ans)