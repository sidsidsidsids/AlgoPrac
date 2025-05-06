N = int(input())
C = 0
for _ in range(N):
    V = ""
    S = set()
    W = input()
    F = True
    for w in W:
        if w != V:
            if w in S:
                F = False
                break
            V = w
            S.add(w)
    C += 1 if F else 0
print(C)