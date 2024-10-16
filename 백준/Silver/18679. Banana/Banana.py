import sys

N = int(sys.stdin.readline().rstrip('\n'))
D = dict()
for _ in range(N):
    eng, mino = sys.stdin.readline().rstrip('\n').split(' = ')
    D[eng] = mino
T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    K = int(sys.stdin.readline().rstrip('\n'))
    answer = []
    S = list(sys.stdin.readline().rstrip('\n').split())
    for s in S:
        answer.append(D[s])
    print(*answer)