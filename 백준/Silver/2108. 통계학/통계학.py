import sys
from collections import defaultdict
N = int(sys.stdin.readline().rstrip('\n'))
maxima = -4001
minima = 4001
hashmap = defaultdict(int)
arr = []
counter = 0
count_list = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip('\n'))
    arr.append(num)
    maxima = max(maxima, num)
    minima = min(minima, num)
    hashmap[num] += 1
    if hashmap[num] > counter:
        counter = hashmap[num]
        count_list = [num]
    elif hashmap[num] == counter:
        count_list.append(num)

arr = sorted(arr)
count_list = sorted(count_list)
print(int(round(sum(arr) / N, 0)))
print(arr[N // 2])
print(count_list[0] if len(count_list) < 2 else count_list[1])
print(maxima - minima)
