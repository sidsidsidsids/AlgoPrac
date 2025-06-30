N = int(input())
for _ in range(N):
    S = input()
    le = len(S)
    l, r = 0, le-1
    flag = True
    while l < r:
        if S[l].lower() != S[r].lower():
            flag = False
            break
        l += 1
        r -= 1
    print("Yes" if flag else "No")