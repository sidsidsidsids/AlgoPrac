import heapq
N = int(input())
arr = []
for _ in range(N):
    a, b = map(int,input().split())
    arr.append([a, b])
L, P = map(int,input().split())

def func(num, info, goal, oil):
    info = sorted(info, key=lambda X:X[0])
    info.append([goal,0])
    oil_heap = []
    cnt = 0

    for loc, p in info:
        if oil >= goal:
            break
        while oil < loc and oil_heap:
            oil += -heapq.heappop(oil_heap)
            cnt += 1
        if oil < loc:
            cnt = -1
            break
        heapq.heappush(oil_heap, -p)
    return cnt

print(func(N, arr, L, P))