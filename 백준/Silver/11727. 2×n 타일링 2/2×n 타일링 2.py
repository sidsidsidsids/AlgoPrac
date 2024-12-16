N = int(input())
v = 0
for n in range(N):
    if v == 0:
        v = 1
        continue
    v *= 2
    if n % 2:
        v += 1
    else:
        v -= 1
    v %= 10007
print(v)