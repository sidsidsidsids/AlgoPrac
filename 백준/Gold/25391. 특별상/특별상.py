import sys

N, M, K = map(int,sys.stdin.readline().split())
scores = [[] for _ in range(N)]

for n in range(N):
    scores[n] = list(map(int,sys.stdin.readline().split()))

scores = sorted(scores, key=lambda X:X[1], reverse=True)
scores[K:] = sorted(scores[K:], key=lambda X:X[0], reverse=True)

value = 0
for s in scores[:M+K]:
    value += s[0]
print(value)