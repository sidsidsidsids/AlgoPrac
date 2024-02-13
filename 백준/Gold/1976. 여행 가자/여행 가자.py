from collections import deque
N = int(input())
M = int(input())
info = dict()
for n in range(N):
    info[n+1] = list()
    arr = list(map(int,input().split()))
    for idx in range(N):
        if arr[idx]:
            info[n+1].append(idx+1)
plan = list(map(int,input().split()))
visit = [0] * (N+1)
Q = deque()
Q.append(plan[0])
visit[plan[0]] = 1
plan = set(plan)
plan.remove(Q[0])
while Q:
    elem = Q.popleft()
    if elem in info:
        for dest in info[elem]:
            if not visit[dest]:
                Q.append(dest)
                visit[dest] = 1
                if dest in plan:
                    plan.remove(dest)
    if not plan:
        break
if plan:
    print("NO")
else:
    print("YES")
