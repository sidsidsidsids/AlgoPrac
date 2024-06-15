import sys

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
before = [set() for _ in range(N+1)]
after = [set() for _ in range(N+1)]
for _ in range(M):
    orders = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    K = orders[0]
    for i in range(1, 1+K):
        singer = orders[i]
        for b in range(1, i):
            before[singer].add(orders[b])
        for a in range(i+1, 1+K):
            after[singer].add(orders[a])
answer = []
Q = []
for i in range(1, 1+N):
    if not before[i]:
        Q.append(i)
while Q:
    elem = Q.pop()
    answer.append(elem)
    for n_elem in after[elem]:
        before[n_elem].remove(elem)
        if not before[n_elem]:
            Q.append(n_elem)

if len(answer) == N:
    for ans in answer:
        print(ans)
else:
    print(0)