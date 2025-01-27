import sys

N, M = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

answer = -1
for i in range(N-2):
    c1 = cards[i]
    for j in range(i+1, N-1):
        c2 = cards[j]
        for k in range(j+1, N):
            c3 = cards[k]
            if answer < c1 + c2 + c3 <= M:
                answer = c1 + c2 + c3
print(answer)