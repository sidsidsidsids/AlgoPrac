def I(R, G, B):
    v = 2126*R + 7152*G + 722*B
    if v >= 2_040_000:
        return "."
    if v >= 1_530_000:
        return "-"
    if v >= 1_020_000:
        return "+"
    if v >= 510_000:
        return "o"
    return "#"

N, M = map(int, input().split())
A = []
for _ in range(N):
    IO = list(map(int, input().split()))
    lst = []
    for i in range(0, 3*M, 3):
        lst.append(I(IO[i], IO[i+1], IO[i+2]))
    A.append(lst)
for line in A:
    for elem in line:
        print(elem, end="")
    print()