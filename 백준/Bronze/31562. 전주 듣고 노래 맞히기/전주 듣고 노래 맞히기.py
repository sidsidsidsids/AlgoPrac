N, M = map(int, input().split())
hashmap = dict()
for _ in range(N):
    info = tuple(input().split())
    hashmap[info[2:5]] = hashmap.get(info[2:5], [])
    hashmap[info[2:5]].append(info[1])
for _ in range(M):
    trial = tuple(input().split())
    if trial in hashmap:
        if len(hashmap[trial]) == 1:
            print(hashmap[trial][0])
        else:
            print("?")
    else:
        print("!")