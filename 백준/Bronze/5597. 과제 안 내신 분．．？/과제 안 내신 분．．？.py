N = [1] * 31
for _ in range(28):
    N[int(input())] = 0
for n in range(1, 31):
    if N[n]:
        print(n)