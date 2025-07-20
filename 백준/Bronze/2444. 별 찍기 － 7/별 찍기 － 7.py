from collections import deque
N = int(input())
D = deque()
D.append("*" * (2*N - 1))
N -= 1
k = 1
while N:
    S = " " * k + "*" * (2*N - 1)
    D.append(S)
    D.appendleft(S)
    k += 1
    N -= 1
for d in D:
    print(d)