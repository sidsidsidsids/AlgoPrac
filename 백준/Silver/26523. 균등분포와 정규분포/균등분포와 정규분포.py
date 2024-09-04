import sys

for _ in range(100):
    cnt = 0
    for _ in range(5000):
        n = float(sys.stdin.readline().rstrip('\n'))
        if n <= 0.05:
            cnt += 1
    print('A' if cnt >= 180 else 'B')