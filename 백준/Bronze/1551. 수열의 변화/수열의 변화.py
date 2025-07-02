from collections import deque
N, K = map(int, input().split())
S = input()
L = deque(map(int, S.split(",")))
I = 1
while K:
    T = L.popleft()
    for i in range(N-I):
        F = L[i]
        L[i] -= T
        T = F
    K -= 1
    I += 1
S = ""
for e in L:
    S += str(e)+","
print(S[:-1])