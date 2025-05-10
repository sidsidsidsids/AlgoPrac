N = int(input())
M = dict()
for _ in range(N):
    L = input().split()
    M[L[0]] = M.get(L[0], 0) + int(L[1])
for k, v in M.items():
    if v == 5:
        print("YES")
        break
else:
    print("NO")