import sys

cards = [n for n in range(21)]
for _ in range(10):
    s, e = map(int, sys.stdin.readline().strip().split())
    d = e - s + 1
    temp = [0] * d
    for i in range(d):
        temp[i] = cards[e-i]
    for i in range(d):
        cards[s+i] = temp[i]
print(*cards[1:])