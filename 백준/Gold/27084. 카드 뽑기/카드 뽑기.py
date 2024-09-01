import sys

N = int(sys.stdin.readline().rstrip('\n'))
A = list(map(int, sys.stdin.readline().rstrip('\n').split()))
R = 10 ** 9 + 7

D = dict()
for elem in A:
    if elem not in D:
        D[elem] = 1
    else:
        D[elem] += 1

answer = 1
for _, v in D.items():
    answer *= (v + 1)

print((answer - 1) % R)