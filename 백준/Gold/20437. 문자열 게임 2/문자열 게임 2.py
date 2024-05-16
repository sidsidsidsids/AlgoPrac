from collections import deque

T = int(input())
answer = [-1] * T
for t in range(T):
    target = input()
    minima = 10001
    maxima = -1
    info = dict()
    K = int(input())
    for c in range(len(target)):
        spell = target[c]
        if spell not in info:
            info[spell] = deque()
        info[spell].append(c)
        if len(info[spell]) == K:
            value = info[spell][-1] - info[spell][0] + 1
            minima = min(minima, value)
            maxima = max(maxima, value)
            info[spell].popleft()
    if minima != 10001 and maxima != -1:
        answer[t] = (minima, maxima)

for ans in answer:
    if ans != -1:
        print(*ans)
    else:
        print(ans)

