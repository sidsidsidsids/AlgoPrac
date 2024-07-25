import sys

N, Q = map(int, sys.stdin.readline().rstrip('\n').split())
score = [0] * N
total = 0
maxima = 0
junghoo = 0
for _ in range(Q):
    a, x, y = map(int, sys.stdin.readline().rstrip('\n').split())
    if a == 1:
        if y == N + 1:
            junghoo += x
        else:
            score[y-1] += x
            maxima = max(score[y-1], maxima)
            total += x
    else:
        ub = junghoo + x
        print('YES' if ub > maxima and (ub - 1) * N >= total + y else 'NO')