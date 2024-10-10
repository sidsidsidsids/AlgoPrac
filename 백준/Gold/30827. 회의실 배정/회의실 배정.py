import sys

N, K = map(int, sys.stdin.readline().rstrip('\n').split())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().rstrip('\n').split())))

arr = sorted(arr, key=lambda X:(X[1],X[0]))

room = [0] * K
count = 0
for start, end in arr:
    for k in range(K):
        if room[k] < start:
            room[k] = end
            count += 1
            room.sort(reverse=True)
            break

print(count)