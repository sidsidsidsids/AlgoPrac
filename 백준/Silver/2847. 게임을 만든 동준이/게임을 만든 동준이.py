N = int(input())
levels = [0] * N
for n in range(N):
    levels[n] = int(input())

answer = 0

for n in range(N-2, -1, -1):
    if levels[n] >= levels[n+1]:
        diff = levels[n] - levels[n+1]
        levels[n] -= diff + 1
        answer += diff + 1

print(answer)