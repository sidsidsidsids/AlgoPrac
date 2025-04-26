N = int(input())
for i in range(1, N+1):
    if i != 1:
        print()
    start = set()
    hashmap = dict()
    S = int(input())
    for _ in range(S-1):
        a, b = input().split()
        if a not in hashmap:
            hashmap[a] = {"before": None, "after": None}
        if b not in hashmap:
            hashmap[b] = {"before": None, "after": None}
        hashmap[a]["after"] = b
        hashmap[b]["before"] = a
        if hashmap[a]["before"] is None:
            start.add(a)
        if hashmap[a]["before"] is not None and a in start:
            start.remove(a)
        if b in start:
            start.remove(b)
    for elem in start:
        path = [elem]
        cur = elem
    while cur is not None:
        route = hashmap[cur]["after"]
        path.append(route)
        cur = route
    print(f"Scenario #{i}:")
    for elem in path[:-1]:
        print(elem)
