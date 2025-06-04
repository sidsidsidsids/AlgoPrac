from collections import deque

N = int(input())
S = deque(input())
C = 1
while S:
    if S[0] == "S":
        S.popleft()
    elif S[0] == "L":
        S.popleft()
        S.popleft()
    C += 1
print(min(C, N))