import sys

N = int(sys.stdin.readline().rstrip('\n'))
answer = 0
for _ in range(N):
    a, d, g = map(int, sys.stdin.readline().rstrip('\n').split())
    score = a * (d + g)
    if a == (d + g):
        score *= 2
    answer = max(answer, score)
print(answer)