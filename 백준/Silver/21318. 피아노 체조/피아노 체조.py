import sys

N = int(sys.stdin.readline().rstrip('\n'))
difficulty = list(map(int,sys.stdin.readline().rstrip('\n').split()))
prefix = [0] * N
for n in range(1, N):
    if difficulty[n-1] > difficulty[n]:
        prefix[n] = prefix[n-1] + 1
    else:
        prefix[n] = prefix[n-1]

Q = int(sys.stdin.readline().rstrip('\n'))
answer = [0] * Q
for q in range(Q):
    x, y = map(int,sys.stdin.readline().rstrip('\n').split())
    answer[q] = prefix[y-1] - prefix[x-1]

for ans in answer:
    print(ans)