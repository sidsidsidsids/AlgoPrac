import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().rstrip('\n').split())
letters = defaultdict(int)
for _ in range(N):
    letter = sys.stdin.readline().rstrip('\n')
    if len(letter) < M:
        pass
    else:
        letters[letter] += 1

letters = sorted(letters.items(), key = lambda X:(-X[1], -len(X[0]), X[0]))
for key, _ in letters:
    print(key)
