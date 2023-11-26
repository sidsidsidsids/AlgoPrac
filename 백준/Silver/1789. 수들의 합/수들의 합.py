N = int(input())
v = 0
n = 1
while v < N:
    v += n
    if v > N:
        n -= 1
        break
    elif v == N:
        break
    else:
        n += 1
if n == 1:
    print(1)
else:
    print(n)