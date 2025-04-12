import sys

N = int(sys.stdin.readline().strip())
H = list(map(int, sys.stdin.readline().strip().split()))

arrows = dict()
shots = 0

for h in H:
    if arrows.get(h, 0) > 0:
        arrows[h] -= 1
        arrows[h-1] = arrows.get(h-1, 0) + 1
    else:
        shots += 1
        arrows[h-1] = arrows.get(h-1, 0) + 1

print(shots)