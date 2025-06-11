S = input()
A = ""
for e in ["U", "A", "P", "C"]:
    if e not in S:
        A += e
print(A)