N, L = map(int,input().split())
lights = [0] * N
for n in range(N):
    D, R, G = list(map(int,input().split()))
    lights[n] = [D, R, G]

dist = 0
time = 0
tIdx = 0
curLight = [0] * N
while dist < L:
    # print("time: ",time, " dist: ",dist, " traffic: ", lights, "/", curLight, " idx: ", tIdx)
    time += 1
    for cL in range(N):
        curLight[cL] += 1
        if curLight[cL] == lights[cL][1] + 1:
            curLight[cL] = -lights[cL][2] + 1
    if dist == lights[tIdx][0]:
        if curLight[tIdx] > 0:
            pass
        else:
            dist += 1
            tIdx += 1
            if tIdx > N-1:
                tIdx = 0
    else:
        dist += 1
print(time)