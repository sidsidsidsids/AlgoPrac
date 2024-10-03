import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    N, K = map(int, sys.stdin.readline().rstrip('\n').split())
    arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    arr = sorted(arr)
    l = 0
    r = N-1
    result = 0
    closest = sys.maxsize
    while l < r:
        value = arr[l] + arr[r]
        if abs(K - value) <= closest:
            if abs(K - value) == closest:
                result += 1
            elif abs(K - value) < closest:
                result = 1
                closest = abs(K - value)
        if value < K:
            l += 1
        elif value > K:
            r -= 1
        else:
            l += 1
            r -= 1
    print(result)
