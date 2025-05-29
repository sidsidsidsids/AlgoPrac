while True:
    n = int(input())
    if not n:
        break
    L = list()
    for _ in range(n):
        L.append(input())
    i = 1
    for l in L:
        le = len(l)
        if le > i:
            while l[i-1] != ' ' and i < le:
                i += 1
            if i == le and l[i-1] != ' ':
                i += 1
    print(i)