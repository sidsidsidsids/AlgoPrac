from collections import defaultdict
N, M = map(int, input().split())
DNA = []
for _ in range(N):
    DNA.append(input())

answer = ''
dist = 0
for m in range(M):
    hm = defaultdict(int)
    for n in range(N):
        hm[DNA[n][m]] += 1
    sort_hm = sorted(hm.items(), key=lambda X:(-X[1], X[0]))
    answer += sort_hm[0][0]
    if len(sort_hm) > 1:
        for e, v in sort_hm[1:]:
            dist += v
print(answer)
print(dist)