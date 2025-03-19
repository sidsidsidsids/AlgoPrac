import sys

N = int(sys.stdin.readline().strip())

jinju = None
cnt = [0] * 1002

for _ in range(N):
    D, C = sys.stdin.readline().strip().split()
    C = int(C)

    if D == "jinju":
        jinju = C

    if C <= 1000:
        cnt[C] += 1
    else:
        cnt[1001] += 1

k = 0
for i in range(jinju+1, 1002):
    k += cnt[i]

print(jinju)
print(k)
