N, M = map(int,input().split())
meat = []
sum_mass = 0
for n in range(N):
    m, p = map(int,input().split())
    meat.append((m, p))
    sum_mass += m
if sum_mass < M:
    print(-1)
else:
    meat = sorted(meat, key=lambda X : (X[1], -X[0]))
    value = 0
    mass = 0
    tmp = 1
    for n in range(N):
        if mass >= M:
            if value and value // tmp == meat[n][1]:
                continue
            else:
                value = min(meat[n][1], value)
            break

        mass += meat[n][0]

        if n and meat[n][1] == meat[n-1][1]:
            tmp += 1
        else:
            tmp = 1

        if mass >= M:
            value = meat[n][1] * tmp
            if tmp == 1:
                break

    print(value)