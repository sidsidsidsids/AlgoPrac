import sys


def time_to_index(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

diff = [0] * (86400 + 1)

n = int(sys.stdin.readline().strip())
queries = []

for _ in range(n):
    parts = sys.stdin.readline().strip().split()
    typ = parts[0]
    start = time_to_index(parts[1])
    end = time_to_index(parts[2])

    if typ == "1":
        diff[start] += 1
        diff[end] -= 1
    else:
        queries.append((start, end))

arr = [0] * 86400
cur = 0
for i in range(86400):
    cur += diff[i]
    arr[i] = cur

pre = [0] * 86400
pre[0] = arr[0]
for i in range(1, 86400):
    pre[i] = pre[i - 1] + arr[i]

for A, B in queries:
    if A == 0:
        sys.stdout.write(str(pre[B - 1]) + "\n")
    else:
        sys.stdout.write(str(pre[B - 1] - pre[A - 1]) + "\n")
