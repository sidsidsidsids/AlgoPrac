import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))
C = list(map(int, sys.stdin.readline().rstrip('\n').split()))
Q = deque()
answer = [0] * N
for n in range(N):
    Q.append([n, C[n]])
S = 0
while Q:
    S += 1
    number, needed = Q.popleft()
    needed -= 1
    if needed == 0:
        answer[number] = S
    else:
        Q.append([number, needed])
print(*answer)
