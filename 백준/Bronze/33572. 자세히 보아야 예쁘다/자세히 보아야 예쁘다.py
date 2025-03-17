import sys

N, M = map(int, sys.stdin.readline().strip().split())
A = sum(list(map(int, sys.stdin.readline().strip().split()))) - N
print("OUT" if M > A else "DIMI")