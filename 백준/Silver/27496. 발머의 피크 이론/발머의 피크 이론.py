N, L = map(int,input().split())
drink = list(map(int,input().split()))

ans = 0
value = 0
for n in range(L):
    if n == N:
        break
    value += drink[n]
    if 129 <= value <= 138:
        ans += 1

for n in range(L,N):
    value += drink[n] - drink[n-L]
    if 129 <= value <= 138:
        ans += 1

print(ans)