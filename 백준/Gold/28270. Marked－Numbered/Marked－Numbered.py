import sys
from collections import defaultdict
C = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().strip().split()))

stk = [0]
answer = []
idx = defaultdict(int)
for c in range(C):
    v = M[c]
    while stk[-1] > v:
        e = stk.pop()
        idx[e] = 0
    if stk[-1] == v:
        idx[v] += 1
        answer.append(idx[v])
    elif stk[-1] < v:
        if v - stk[-1] == 1:
            stk.append(v)
            idx[v] += 1
            answer.append(idx[v])
        else:
            answer = [-1]
            break
print(*answer)