import sys

L, P = map(int, sys.stdin.readline().strip().split())
news = list(map(int, sys.stdin.readline().strip().split()))
answers = []
LP = L * P
for elem in news:
    answers.append(elem - LP)
print(*answers)