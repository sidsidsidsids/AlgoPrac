import math
H, Y = map(int, input().split())
L = [0] * (Y+1)
L[0] = H
for i in range(1, Y+1):
    L[i] = math.floor(L[i-1] * 1.05)
    if i >= 3:
        L[i] = max(L[i], math.floor(L[i-3] * 1.20))
    if i >= 5:
        L[i] = max(L[i], math.floor(L[i-5] * 1.35))
print(max(L))