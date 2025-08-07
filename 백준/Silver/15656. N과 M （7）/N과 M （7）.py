def func(num, crit, table, depth, array):
    if depth == crit:
        print(*array)
    else:
        for n in range(num):
            array.append(table[n])
            func(num, crit, table, depth+1, array)
            array.pop()

N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
func(N, M, L, 0, [])