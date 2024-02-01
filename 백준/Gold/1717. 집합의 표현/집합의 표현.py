import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int,input().split())
path = [i for i in range(N+1)]

def get_parent(x):
    if path[x] != x:
        path[x] = get_parent(path[x])
    return path[x]

for _ in range(M):
    t, a, b = map(int,input().split())
    if t == 0:
        a_parent = get_parent(a)
        b_parent = get_parent(b)
        if a_parent >= b_parent:
            path[a_parent] = b_parent
        else:
            path[b_parent] = a_parent
    else:
        if get_parent(a) == get_parent(b):
            print("YES")
        else:
            print("NO")