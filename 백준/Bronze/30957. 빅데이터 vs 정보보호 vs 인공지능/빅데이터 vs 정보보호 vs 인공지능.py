N = int(input())
STR = input()
hm = dict()
hm["B"] = 0
hm["S"] = 0
hm["A"] = 0
M = 0
for e in STR:
    hm[e] += 1
    M = max(M, hm[e])

ans = ""
for w in ["B", "S", "A"]:
    if hm[w] == M:
        ans += w
print(ans if ans != "BSA" else "SCU")