S = input()
A = 0
for s in S:
    if s in "ABC":
        A += 3
    elif s in "DEF":
        A += 4
    elif s in "GHI":
        A += 5
    elif s in "JKL":
        A += 6
    elif s in "MNO":
        A += 7
    elif s in "PQRS":
        A += 8
    elif s in "TUV":
        A += 9
    elif s in "WXYZ":
        A += 10
    else:
        A += 11
print(A)