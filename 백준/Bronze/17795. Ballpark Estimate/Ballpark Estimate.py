import sys

N = sys.stdin.readline().rstrip('\n')
print(round(int(N), 1 - len(N)))