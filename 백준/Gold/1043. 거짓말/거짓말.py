N, M = map(int,input().split())
truth_input = list(map(int,input().split()))
truth = set(truth_input[1:])

graph = dict()
for n in range(N):
    graph[n+1] = set()

party = []
for m in range(M):
    party_input = list(map(int,input().split()))
    people = party_input[1:]
    for person in people:
        for another in people:
            if person != another:
                graph[person].add(another)
    party.append(people)

V = [0] * (N+1)
cur = []
for elem in truth:
    cur.append(elem)
    V[elem] = 1
while cur:
    pos = cur.pop()
    for next_pos in graph[pos]:
        if not V[next_pos]:
            cur.append(next_pos)
            V[next_pos] = 1

cnt = 0
for people in party:
    flag = True
    for person in people:
        if V[person]:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)