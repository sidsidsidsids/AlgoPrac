import sys

x, y = map(int, sys.stdin.readline().rstrip('\n').split())
flag = False

def func(a, b, depth):
    global flag
    if flag:
        return
    if a == b == 0:
        flag = True
        return
    dist = 3 ** depth
    if a >= dist:
        func(a - dist, b, depth + 1)
    if b >= dist:
        func(a, b - dist, depth + 1)

func(x, y, 0)
print(1 if flag else 0)