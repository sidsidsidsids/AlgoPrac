import sys
import heapq

N = int(sys.stdin.readline().strip())
awarded = set()
answer = []
A = []
B = []
C = []
D = []
for _ in range(N):
    X, a, b, c, d = map(int, sys.stdin.readline().strip().split())
    A.append((-a, X))
    B.append((-b, X))
    C.append((-c, X))
    D.append((-d, X))
heapq.heapify(A)
heapq.heapify(B)
heapq.heapify(C)
heapq.heapify(D)
for scores in [A, B, C, D]:
    while True:
        _, i = heapq.heappop(scores)
        if i not in awarded:
            answer.append(i)
            awarded.add(i)
            break

print(*answer)