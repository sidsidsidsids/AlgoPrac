import sys
from itertools import combinations
T = int(sys.stdin.readline())
ans = [0] * T

for tc in range(T):
    n, m, k = map(int,sys.stdin.readline().split())
    bob = list(map(int,sys.stdin.readline().split()))
    ali = list(map(int,sys.stdin.readline().split()))
    bCase = list(combinations(bob,k))
    aCase = list(combinations(ali,k))
    bL = len(bCase)
    aL = len(aCase)
    for B in range(bL):
        bCase[B] = sum(bCase[B])
    for A in range(aL):
        aCase[A] = sum(aCase[A])
    bCase = sorted(bCase)
    aCase = sorted(aCase)
    maxDif = max(abs(aCase[-1] - bCase[0]), abs(bCase[-1] - aCase[0]))
    minDif = 100000000 * k
    bP = 0
    aP = 0
    while bP < bL and aP < aL:
        if abs(bCase[bP] - aCase[aP]) < minDif:
            minDif = abs(bCase[bP] - aCase[aP])
            if aCase[aP] > bCase[bP]:
                bP += 1
            elif bCase[bP] > aCase[aP]:
                aP += 1
            else:
                break
        else:
            if aCase[aP] > bCase[bP]:
                bP += 1
            elif bCase[bP] > aCase[aP]:
                aP += 1
            else:
                break
    ans[tc] = [minDif, maxDif]

for elem in ans:
    print(*elem)

