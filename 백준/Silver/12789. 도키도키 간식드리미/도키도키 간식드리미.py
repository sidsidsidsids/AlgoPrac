import sys

N = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().strip().split()))
spare = [N+1]
V = 1
for elem in line:
    while spare[-1] == V:
        spare.pop()
        V += 1
    if elem == V:
        V += 1
    else:
        if elem < spare[-1]:
            spare.append(elem)
        else:
            break
while spare and spare[-1] == V:
    spare.pop()
    V += 1

print("Nice" if V == N+2 else "Sad")