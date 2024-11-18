N, S, R = map(int, input().rstrip('\n').split())
kayak = [0] * (N+2)
broke = [0] * (N+2)
broken = list(map(int, input().rstrip('\n').split()))
for e in broken:
    broke[e] = 1
having = list(map(int, input().rstrip('\n').split()))
for e in having:
    kayak[e] = 1

for n in range(1, N+1):
    if broke[n] and kayak[n]:
        broke[n] = 0
        kayak[n] = 0

answer = 0
for n in range(1, N+1):
    if broke[n]:
        for i in range(n-1, n+2):
            if kayak[i]:
                kayak[i] = 0
                break
        else:
            answer += 1

print(answer)