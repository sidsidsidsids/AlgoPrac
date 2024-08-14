import sys

trees = []

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip('\n').split())
    if a == 1:
        trees.append(b)
    else:
        if trees:
            target = max(trees[-1] - b, 0)
            if trees and trees[-1] >= target:
                trees[-1] = target

cur = trees[-1] if trees else 0
ans = 0
while trees:
    elem = trees.pop()
    if elem >= cur:
        ans += cur
    else:
        cur = elem
        ans += cur

print(ans)