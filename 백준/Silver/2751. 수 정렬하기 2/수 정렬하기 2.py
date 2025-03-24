import sys

N = int(sys.stdin.readline().strip())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline().strip()))
num.sort()
for e in num:
    print(e)