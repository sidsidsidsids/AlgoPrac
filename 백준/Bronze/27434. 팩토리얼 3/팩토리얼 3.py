import sys

N = int(sys.stdin.readline().rstrip('\n'))
a = 1
for n in range(1, N+1):
    a *= n
print(a)