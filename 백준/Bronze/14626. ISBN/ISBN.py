N = input()
res = 0
target = bool
for i in range(13):
    flag = True if (i+1) % 2 else False # 홀수면 True
    if N[i] == "*":
        target = flag
        continue
    if flag:
        res += int(N[i]) % 10
    else:
        res += int(N[i]) * 3 % 10
if target:
    print((10 - res) % 10)
else:
    V = (10 - res) % 10
    for v in range(10):
        if (v * 3) % 10 == V:
            print(v)
            break