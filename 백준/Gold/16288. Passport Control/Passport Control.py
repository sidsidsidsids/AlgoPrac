import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

Q = [0] * K
for elem in arr:
    flag = False
    for k in range(K):
        if elem > Q[k]:
            Q[k] = elem
            flag = True
            break
    if not flag:
        break
print("NO" if not flag else "YES")