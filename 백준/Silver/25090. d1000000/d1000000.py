import sys
T = int(sys.stdin.readline().rstrip('\n'))
for t in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    S = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    S.sort()
    V = 1
    cnt = 0
    for s in S:
        if s >= V:
            cnt += 1
            V += 1
    print(f'Case #{t+1}: {cnt}')