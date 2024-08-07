import sys

a, b = map(int, sys.stdin.readline().rstrip('\n').split())
cnt_2 = 0
cnt_5 = 0

n = 2
while b // n != (a-1) // n:
    cnt_2 += 1
    n *= 2

n = 5
while b // n != (a-1) // n:
    cnt_5 += 1
    n *= 5

print(min(cnt_2, cnt_5))