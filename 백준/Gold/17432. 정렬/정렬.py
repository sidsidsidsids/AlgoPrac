import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    arr = [0] * N
    for num in range(N, 0, -1):
        if M == 0:
            break
        diff = min(M, num-1)
        arr[N - 1 - diff] = num
        M -= diff
    num = 1
    for n in range(N):
        if not arr[n]:
            arr[n] = num
            num += 1

    print(*arr)