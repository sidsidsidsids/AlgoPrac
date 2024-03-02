import heapq

n = int(input())
arr = []
ans = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if arr:
            ans.append(heapq.heappop(arr))
        else:
            ans.append(0)
    else:
        heapq.heappush(arr,x)
for a in ans:
    print(a)