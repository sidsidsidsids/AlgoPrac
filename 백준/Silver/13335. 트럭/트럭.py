from collections import deque
Q = deque()
n, w, L = map(int,input().split())
trucks = list(map(int,input().split()))
for truck in trucks:
    Q.append(truck)
bridge = deque()
ans = 0
curL = 0
while True:
    if bridge:
        out = False
        for idx in range(len(bridge)):
            bridge[idx][1] -= 1
            if bridge[idx][1] == 0:
                curL -= bridge[idx][0]
                out = True
        if out:
            bridge.popleft()
    else:
        if ans:
            break

    if len(bridge) < w:
        if Q and curL + Q[0] <= L:
            elem = Q.popleft()
            bridge.append([elem, w])
            curL += elem
        else:
            pass
    else:
        pass
    ans += 1
print(ans)
