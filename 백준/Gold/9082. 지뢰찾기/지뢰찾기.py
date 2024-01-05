from collections import deque
T = int(input())
ans = [0] * T
for t in range(T):
    N = int(input())
    num = list(map(int,input()))
    arr = str(input())
    Q = deque()

    cnt = 0
    if num[0] == 0:
        pass
    elif num[0] == 1:
        cnt += 1
        Q.append(0)
    else:
        cnt += 2
        Q.append(0)
        Q.append(1)

    for n in range(1, N-1):
        if Q and Q[0] < n - 1:
            Q.popleft()
        if num[n] > len(Q):
            Q.append(n + 1)
            cnt += 1

    if num[-1] > len(Q):
        cnt += 1

    ans[t] = cnt

for elem in ans:
    print(elem)