N = int(input())
P = [ i+1 for i in range(N) ]
T = 1
while len(P) > 1:
    targetIdx = ((T ** 3) % len(P)) - 1
    if targetIdx == -1 :
        P = P[:-1]
    else:
        P = P[(targetIdx + 1):] + P[:targetIdx]
    T += 1
print(P[0])

