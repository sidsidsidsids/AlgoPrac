import sys

N = int(sys.stdin.readline().rstrip('\n'))
arr = [0] * N
for n in range(N):
    c, r, s, d = sys.stdin.readline().rstrip('\n').split()
    arr[n] = [c, int(r) * 2 + int(s) * 3 + int(d)]
arr = sorted(arr, key=lambda X:(-X[1], X[0]))
if len(arr) > 0:
    print(arr[0][0])
if len(arr) > 1:
    print(arr[1][0])