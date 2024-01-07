S = str(input())
P = str(input())

record = set()
S_len = len(S)
for i in range(S_len):
    for j in range(i+1, S_len + 1):
        record.add(S[i:j])

P_len = len(P)
idx = 0
n_idx = 1
ans = 0
while idx < P_len:
    if n_idx == P_len:
        ans += 1
        break
    if P[idx:n_idx + 1] in record:
        n_idx += 1
        pass
    else:
        idx = n_idx
        n_idx = idx + 1
        ans += 1

print(ans)
