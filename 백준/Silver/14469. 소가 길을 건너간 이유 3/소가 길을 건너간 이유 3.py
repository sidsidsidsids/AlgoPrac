N = int(input())
cows = [[] for _ in range(N)]
for n in range(N):
    a, t = map(int,input().split())
    cows[n] = [a, t]
cows = sorted(cows, key=lambda X:X[0])

t = 0
for n in range(N):
    if cows[n][0] > t:
        t = cows[n][0] + cows[n][1]
    else:
        t += cows[n][1]
print(t)