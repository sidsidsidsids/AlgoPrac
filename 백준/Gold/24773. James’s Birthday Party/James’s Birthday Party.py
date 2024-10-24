import sys


while True:
    N, M = map(int, sys.stdin.readline().rstrip('\n').split())
    if N == 0 and M == 0:
        break
    F = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip('\n').split())
        F[a].append(b)
        F[b].append(a)
    V = [0] * N
    A = [0] * N
    C = 0

    def dfs(node, is_root):
        global C
        C += 1
        V[node] = C
        child_cnt = 0
        min_order = V[node]
        for child in F[node]:
            if V[child]:
                min_order = min(min_order, V[child])
                continue
            child_cnt += 1
            res = dfs(child, False)
            min_order = min(min_order, res)
            if not is_root and res >= V[node]:
                A[node] = 1
        if is_root and child_cnt >= 2:
            A[node] = 1
        return min_order

    flag = True
    for n in range(N):
        if not V[n]:
            dfs(n, True)
        if A[n] or len(F[n]) <= 1:
            flag = False
            break

    print("No" if flag else "Yes")