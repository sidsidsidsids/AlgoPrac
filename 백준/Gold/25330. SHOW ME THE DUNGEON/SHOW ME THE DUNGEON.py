import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))

memo = {}

def action(mask, health, cumulative):
    if health < 0:
        return 0
    key = (mask, health, cumulative)
    if key in memo:
        return memo[key]

    max_score = 0
    for i in range(N):
        if not (mask & (1 << i)):
            cost = cumulative + A[i]
            next_health = health - cost
            if next_health < 0:
                continue
            score = P[i] + action(mask | (1 << i), next_health, cumulative + A[i])
            max_score = max(max_score, score)

    memo[key] = max_score
    return max_score

print(action(0, K, 0))