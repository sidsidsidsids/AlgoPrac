N = int(input())
ropes = [0] * N
for n in range(N):
    ropes[n] = int(input())

ropes = sorted(ropes)
value = ropes[-1]
cnt = 2
for n in range(N-2,-1,-1):
    if ropes[n] * cnt >= value:
        value = ropes[n] * cnt
        cnt += 1
    else:
        cnt += 1
print(value)