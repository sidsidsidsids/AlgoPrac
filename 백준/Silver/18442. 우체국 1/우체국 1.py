V, P, L = map(int, input().split())
Vs = list(map(int, input().split()))

case = []
min_dist = L * V + 1
answer = []
def cases(idx, cnt):
    if idx == V+1:
        return
    if cnt == P:
        calculate()
        return
    case.append(idx)
    cases(idx+1, cnt+1)
    case.pop()
    cases(idx+1, cnt)
def calculate():
    global min_dist
    global answer
    office = [Vs[case[p]] for p in range(P)]
    flag = True
    dist = 0
    for v in Vs:
        value = L + 1
        for o in office:
            value = min(value, min(abs(o - v), L - abs(o - v)))
        dist += value
        if dist >= min_dist:
            flag = False
            break
    if flag:
        min_dist = min(min_dist, dist)
        answer = office
cases(0, 0)
print(min_dist)
print(*answer)