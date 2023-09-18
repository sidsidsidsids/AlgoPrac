import sys
N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

l = 0
r = max(trees)
while l <= r:
    value = 0
    target = (l + r) // 2
    for tree in trees:
        if tree >= target:
            value += tree - target
    if value >= M:
        ans = target
        l = target+1
    else:
        r = target-1
print(ans)
