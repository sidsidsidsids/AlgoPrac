import sys

N = int(sys.stdin.readline().strip())
answer = []
for _ in range(N):
    names = list(sys.stdin.readline().strip().split())
    god = 'god'
    for name in names[1:]:
        god += name
    answer.append(god)
print("\n".join(answer))