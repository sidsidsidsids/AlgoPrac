import sys

T = int(sys.stdin.readline().strip())
M = 2 ** 32
answer = []
for _ in range(T):
    x, y = map(int,sys.stdin.readline().strip().split())
    Q = [x]
    V = set()
    V.add(x)
    while Q:
        e = Q.pop()
        if e == y:
            answer.append("Yes")
            break
        mul = (e * 2) % M
        div = e // 2
        for val in (mul, div):
            if val not in V:
                V.add(val)
                Q.append(val)
    else:
        answer.append("No")
print("\n".join(answer))