import sys
N, L = map(int,sys.stdin.readline().rstrip('\n').split())
ladder = []
for _ in range(N):
    width, direction = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    if direction == 1:
        ladder.append([L - width, L, 1])
    else:
        ladder.append([0, width, 0])

H = 0
T = 0

def jump(bot, top):
    bs, be, _ = ladder[bot]
    ns, ne, _ = ladder[top]
    return bs <= ne and ns <= be

def move(num):
    elem = ladder[num]
    if elem[2] == 0:
        if elem[1] == L:
            elem[2] = 1
            elem[0] -= 1
            elem[1] -= 1
        else:
            elem[0] += 1
            elem[1] += 1
    else:
        if elem[0] == 0:
            elem[2] = 0
            elem[0] += 1
            elem[1] += 1
        else:
            elem[0] -= 1
            elem[1] -= 1
    return elem

while True:
    if H == N-1:
        break
    if jump(H, H+1):
        H += 1
    else:
        break

while H < N-1:
    T += 1
    for n in range(N):
        ladder[n] = move(n)
    while True:
        if H == N-1:
            break
        if jump(H, H+1):
            H += 1
        else:
            break
    if H == N-1:
        break

print(T)