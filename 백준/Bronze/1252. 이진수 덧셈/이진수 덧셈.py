import sys

a, b = sys.stdin.readline().strip().split()
A = int(a, 2)
B = int(b, 2)
print(bin(int(a, 2) + int(b, 2))[2:])