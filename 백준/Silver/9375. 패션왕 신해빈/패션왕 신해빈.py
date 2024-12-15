import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip('\n'))
answer = [0] * N
for n in range(N):
    closet = defaultdict(set)
    M = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(M):
        item, kind = sys.stdin.readline().rstrip('\n').split()
        closet[kind].add(item)
    case = 1
    for key, val in closet.items():
        case *= (len(val) + 1)
    case -= 1
    answer[n] = str(case)
print("\n".join(answer))
