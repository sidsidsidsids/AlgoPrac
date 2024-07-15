import sys

S, N = sys.stdin.readline().rstrip('\n').split()
N = int(N)
LS = len(S)

def func(n: int, l: int):
    global N
    if N <= l:
        return

    func(n + 1, l * 2)
    if N <= l:
        return

    if N == l + 1:
        N -= 1
    else:
        N -= l + 1

func(0, LS)
print(S[N - 1])