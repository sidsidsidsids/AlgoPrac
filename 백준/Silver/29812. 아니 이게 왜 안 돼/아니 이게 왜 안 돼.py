import sys

N = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()
D, M = map(int, sys.stdin.readline().strip().split())

hash_map = {'H': 0, 'Y': 0, 'U': 0}

energy = 0
seq = 0
for i in range(N):
    if S[i] in "HYU":
        hash_map[S[i]] += 1
        if seq:
            energy += min(D * seq, D + M)
        seq = 0
    else:
        seq += 1
if seq:
    energy += min(D * seq, D + M)
count = min(hash_map['H'], hash_map['Y'], hash_map['U'])
print(energy if energy else "Nalmeok")
print(count if count else "I love HanYang University")