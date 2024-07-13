import sys

N, a, b, c, d, e, f, g, h, M = map(int, sys.stdin.readline().rstrip('\n').split())

T = N * 3
info = [0] * T
for i in range(T):
    i_2 = i * i
    i_3 = i_2 * i
    i_5 = i_3 * i * i
    W_i = (a * i_5 + b * i_2 + c) % d
    U_i = (e * i_5 + f * i_3 + g) % h
    info[i] = (W_i, U_i)

info.sort(key = lambda X : (-X[1], X[0]))

answer = 0
for n in range(N):
    answer += (info[n][0] % M)
print(answer % M)