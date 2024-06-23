import sys
W, H, X, Y, P = map(int,sys.stdin.readline().rstrip('\n').split())
R = H / 2
cnt = 0
def check(x, y):
    if X <= x <= X + W and Y <= y <= Y + H:
        return True
    if (X - x) ** 2 + ((Y + R) - y) ** 2 <= R ** 2:
        return True
    if ((X + W) - x) ** 2 + ((Y + R) - y) ** 2 <= R ** 2:
        return True
    return False
for _ in range(P):
    x, y = map(int,sys.stdin.readline().rstrip('\n').split())
    if check(x, y):
        cnt += 1
print(cnt)