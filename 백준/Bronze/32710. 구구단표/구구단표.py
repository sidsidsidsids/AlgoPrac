import sys

nums = set()
for a in range(2, 10):
    for b in range(1, 10):
        nums.update((a, b, a*b))

N = int(sys.stdin.readline())
print(1 if N in nums else 0)