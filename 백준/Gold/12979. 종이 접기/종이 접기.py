import sys

W, H, A = map(int, sys.stdin.readline().strip().split())

def cases(square):
    lsts = []
    for i in range(1, int(square ** (1/2))+1):
        if not square % i:
            lsts.append((i, square // i))
    return lsts


targets = cases(A)

def calculates(w, h):
    if W < w or H < h:
        return -1
    cnt = 0
    tW, tH = W, H
    while tW > w:
        if tW % 2:
            tW += 1
        tW //= 2
        cnt += 1
    while tH > h:
        if tH % 2:
            tH += 1
        tH //= 2
        cnt += 1
    return cnt


answer = 200001
for a, b in targets:
    value = calculates(a, b)
    if value != -1 and value < answer:
        answer = value
    value = calculates(b, a)
    if value != -1 and value < answer:
        answer = value

print(answer if answer != 200001 else -1)