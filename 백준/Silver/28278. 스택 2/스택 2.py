import sys

N = int(sys.stdin.readline())
S = []
for _ in range(N):
    order = list(map(int, sys.stdin.readline().split()))
    k = order[0]
    if k == 1:
        S.append(order[1])
    elif k == 2:
        if S:
            print(S.pop())
        else:
            print(-1)
    elif k == 3:
        print(len(S))
    elif k == 4:
        print(0 if S else 1)
    elif k == 5:
        print(S[-1] if S else -1)