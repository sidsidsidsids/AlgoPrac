from collections import deque
F, S, G, U, D = map(int,input().split())
arr = [-1] * (F+1)
if S == G:
    print(0)
else:
    Q = deque()
    Q.append(S)
    arr[S] = 0
    flag = False
    while Q and not flag:
        elem = Q.popleft()
        for n_elem in [elem + U, elem - D]:
            if 0 < n_elem < F+1 and arr[n_elem] == -1:
                arr[n_elem] = arr[elem] + 1
                Q.append(n_elem)
            if n_elem == G:
                flag = True
                break
    print(arr[G] if arr[G] > -1 else "use the stairs")
