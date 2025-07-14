import sys
for _ in range(int(sys.stdin.readline().strip())):
    print(sum(list(map(int, sys.stdin.readline().strip().split()))))