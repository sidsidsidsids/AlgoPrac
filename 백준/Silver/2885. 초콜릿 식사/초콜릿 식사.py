N = int(input())
minima = 20
for i in range(20):
    if 2**i >= N:
        minima = i
        break
ans_1 = 2 ** minima

if N == ans_1:
    print(ans_1, 0)
else:
    target = minima
    ans_2 = 0
    while N:
        if N > 2 ** target:
            N -= 2 ** target
        elif N == 2 ** target:
            break
        ans_2 += 1
        target -= 1
        if target == -1:
            break

    print(ans_1, ans_2)
