from collections import deque
T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    start = list(map(int,input().split()))
    store = [[] for _ in range(N)]
    for n in range(N):
        store[n] = list(map(int,input().split()))
    end = list(map(int,input().split()))

    Q = deque()
    Q.append((start[0], start[1]))
    V = [0] * N
    result = "sad"
    while Q:
        elem = Q.popleft()
        X, Y = elem[0], elem[1]
        if abs(end[0] - X) + abs(end[1] - Y) <= 1000:
            result = "happy"
            break
        for n in range(N):
            if not V[n] and abs(store[n][0] - X) + abs(store[n][1] - Y) <= 1000:
                Q.append((store[n][0], store[n][1]))
                V[n] = 1
    answer.append(result)
for ans in answer:
    print(ans)