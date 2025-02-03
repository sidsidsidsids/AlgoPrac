import sys

N, K = map(int, sys.stdin.readline().strip().split())
X = list(map(int, sys.stdin.readline().strip().split()))

clap = 0
cnt = 0
for x in X:
    if clap < x:
        cnt += 1
        clap = x + K

print(cnt)