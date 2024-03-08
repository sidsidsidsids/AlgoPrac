import heapq

N, M, X = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int,input().split())
    arr[s].append((t, e))
def dijk(s, e):
    Q = [(0, s)]
    dist = [10000 * N + 1] * (N + 1)
    dist[s] = 0
    while Q:
        elem = heapq.heappop(Q)
        cur_dist, cur_loc = elem[0], elem[1]

        if dist[cur_loc] < cur_dist:
            continue

        for next_elem in arr[cur_loc]:
            next_dist, next_loc = next_elem[0], next_elem[1]
            cost = cur_dist + next_dist
            if dist[next_loc] > cost:
                dist[next_loc] = cost
                heapq.heappush(Q, (cost, next_loc))

    if s == X:
        return dist
    return dist[e]

answer = 0
party_to_home = dijk(X, 0)
for n in range(1, N+1):
    if n != X:
        home_to_party = dijk(n, X)
        if home_to_party + party_to_home[n] > answer:
            answer = home_to_party + party_to_home[n]
print(answer)
