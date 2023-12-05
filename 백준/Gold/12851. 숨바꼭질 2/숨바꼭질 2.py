from collections import deque

N, K = map(int,input().split())

def finding(N,K):
    V = [0] * 100001
    Q = deque()
    Q.append(N)
    cnt = 0
    result = 0

    while Q:
        elem = Q.popleft()
        cur = V[elem]

        if elem == K:
            result = cur
            cnt += 1
            continue

        for next in [elem - 1, elem + 1, elem * 2]:
            if 0 <= next <= 100000:
                if not V[next] or V[next] == cur + 1:
                        Q.append(next)
                        V[next] = cur + 1

    return [result, cnt]

if N == K:
    print(0)
    print(1)
else:
    answer = finding(N,K)
    print(answer[0])
    print(answer[1])
