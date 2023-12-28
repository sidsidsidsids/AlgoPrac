N = int(input())
skyline = [0] * N
for n in range(N):
    _, h = map(int,input().split())
    skyline[n] = h
cnt = 0
i = 0
values = [0]
while i < N:
    if values[-1] < skyline[i]:
        cnt += 1
        values.append(skyline[i])
    else:
        while values[-1] > skyline[i]:
            values.pop()
        if values[-1] < skyline[i]:
            cnt += 1
            values.append(skyline[i])
    i += 1
print(cnt)