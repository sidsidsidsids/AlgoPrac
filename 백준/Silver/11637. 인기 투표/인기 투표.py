import sys

T = int(sys.stdin.readline().rstrip('\n'))
for _ in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    total = 0
    maxima = 0
    idx = 0
    cnt = 1
    for n in range(N):
        g = int(sys.stdin.readline().rstrip('\n'))
        total += g
        if g >= maxima:
            if g == maxima:
                cnt += 1
            else:
                maxima = g
                idx = n + 1
                cnt = 1
    half = total // 2
    if cnt > 1:
        print("no winner")
    elif maxima > half:
        print(f"majority winner {idx}")
    elif maxima <= half:
        print(f"minority winner {idx}")