import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([])
for i in range(N):
    card.append(i+1)

while len(card) > 1:
    card.popleft()
    if len(card) > 1:
        top = card.popleft()
        card.append(top)
    else:
        break

print(card[0])
