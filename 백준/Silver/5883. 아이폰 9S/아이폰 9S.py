N = int(input())
B = [0] * N
elems = set()
for b in range(N):
    elem = int(input())
    B[b] = elem
    if elem not in elems:
        elems.add(elem)
ans = 0
for e in elems:
    check = list()
    for b in range(N):
        if B[b] != e:
            check.append(B[b])
    cnt = 1
    tmpVal = 0
    for idx in range(1, len(check)):
        if check[idx] == check[idx-1]:
            cnt += 1
            if idx == (len(check) - 1):
                if tmpVal < cnt:
                    tmpVal = cnt
        else:
            if tmpVal < cnt:
                tmpVal = cnt
            cnt = 1
    if tmpVal > ans:
        ans = tmpVal
print(ans)