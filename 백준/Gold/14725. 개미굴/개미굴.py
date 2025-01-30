import sys

N = int(sys.stdin.readline().strip())
cave = dict()
prev = -1
for _ in range(N):
    info = list(sys.stdin.readline().strip().split())
    I = int(info[0])
    for i in range(1, I+1):
        if i == 1:
            if info[i] in cave:
                prev = cave[info[i]]
                continue
            cave[info[i]] = dict()
            prev = cave[info[i]]
            continue
        if info[i] in prev:
            prev = prev[info[i]]
            continue
        prev[info[i]] = dict()
        prev = prev[info[i]]
        continue

def func(depth, hashmap):
    hashmap = dict(sorted(hashmap.items(), key=lambda X:X[0]))
    for key, val in hashmap.items():
        print(f"{'-' * (depth * 2)}{key}")
        if val:
            func(depth + 1, hashmap[key])

func(0, cave)