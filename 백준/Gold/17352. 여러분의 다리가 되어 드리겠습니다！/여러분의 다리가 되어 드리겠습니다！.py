import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-2):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

V = [0] * (N+1)
path = [1]
V[1] = 1
while path:
    elem = path.pop()
    for nelem in arr[elem]:
        if not V[nelem]:
            V[nelem] = 1
            path.append(nelem)
start = -1
end = -1
for n in range(1, N+1):
    if start != -1 and end != -1:
        break
    if V[n]:
        if start == -1:
            start = n
    else:
        if end == -1:
            end = n

print(start, end)