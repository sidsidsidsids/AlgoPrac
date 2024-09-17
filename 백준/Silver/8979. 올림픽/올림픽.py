import sys

def solve(total: int, target: int, record: list):
    ranking = sorted(record, key=lambda X:(-X[1], -X[2], -X[3]))
    nn, G, S, B = ranking[0]
    if nn == target:
        return 1
    rank = 1
    for i in range(1, total):
        num, gold, silver, bronze = ranking[i]
        if gold < G or (gold >= G and silver < S) or (gold >= G and silver >= S and bronze < B):
            rank = i + 1
            G = gold; S = silver; B = bronze
        if num == target:
            break
    return rank

N, K = map(int, sys.stdin.readline().rstrip('\n').split())
L = []
for _ in range(N):
    L.append(tuple(map(int, sys.stdin.readline().rstrip('\n').split())))
print(solve(N, K, L))
