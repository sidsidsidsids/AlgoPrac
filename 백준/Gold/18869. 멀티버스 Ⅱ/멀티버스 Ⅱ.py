import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    keys = sorted(list(set(planets)))
    # print(keys)
    ranks = {keys[i]: i for i in range(len(keys))}
    # print(ranks)
    add = tuple([ranks[x] for x in planets])
    # print(add)
    universe[add] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)