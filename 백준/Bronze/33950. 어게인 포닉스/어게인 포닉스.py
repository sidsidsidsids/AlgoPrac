n = int(input())
for _ in range(n):
    S = list(input())
    L = len(S)
    for i in range(1, L):
        if S[i-1] == "P" and S[i] == "O":
            S[i] = "HO"
    print(''.join(S))
