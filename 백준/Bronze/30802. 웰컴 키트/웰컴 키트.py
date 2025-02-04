import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
T, P = map(int, sys.stdin.readline().strip().split())

T_cnt = 0
for e in A:
    T_cnt += e // T
    if e % T:
        T_cnt += 1
print(T_cnt)
print(N // P, N % P)