import sys

n = int(sys.stdin.readline().rstrip('\n'))
flag = True
for _ in range(3):
    s = set(map(int, sys.stdin.readline().rstrip('\n').split()))
    if 7 not in s:
        flag = False
print(777 if flag else 0)