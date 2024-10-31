import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    cafes = []
    for _ in range(N):
        cafes.append(tuple(map(int, sys.stdin.readline().rstrip('\n').split())))
    cafes = sorted(cafes, key=lambda X:(X[0], X[1]))
    nums = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    result = [0] * (N + 1)
    result[0] = 1

    current = 0
    def func(arr: list):
        global current
        L = len(arr)
        if L <= 1:
            result[result[0]] = arr[0]
            result[0] += 1
            current = arr[0][1]
            return

        lo = arr[0][1]
        hi = arr[-1][1]
        if abs(lo - current) < abs(hi - current):
            for i in range(L):
                result[result[0]] = arr[i]
                result[0] += 1
            current = arr[i][1]
        else:
            for i in range(L-1, -1, -1):
                result[result[0]] = arr[i]
                result[0] += 1
            current = arr[i][1]
        return

    targets = []
    for x, y in cafes:
        if targets and targets[-1][0] != x:
            func(targets)
            targets = [(x, y)]
        else:
            targets.append((x, y))

    if targets:
        func(targets)

    for num in nums[1:]:
        print(*result[num])