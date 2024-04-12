N, K = map(int,input().split())
num = list(map(int,input()))
ans = []

for n in range(N):
    while K and ans and ans[-1] < num[n]:
        ans.pop()
        K -= 1
    ans.append(num[n])

while K:
    ans.pop()
    K -= 1

for a in ans:
    print(a,end="")