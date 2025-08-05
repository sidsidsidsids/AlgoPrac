Q = int(input())
N = 0
F = True
for _ in range(Q):
    x, y = map(int, input().split())
    if x == 1:
        N += y
    else:
        N -= y
        if N < 0:
            F = False
print("See you next month" if F else "Adios")