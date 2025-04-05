import sys

N, M = map(int, sys.stdin.readline().strip().split())
apart = []
record = []
for m in range(1, M+1):
    L, R = map(int, sys.stdin.readline().strip().split())
    record.append((L, m))
    record.append((R, m))
record = sorted(record, key=lambda X:X[0])
apart.append(record[-1][1])
for elem in record:
    apart.append(elem[1])
print(apart[N%(M*2)])