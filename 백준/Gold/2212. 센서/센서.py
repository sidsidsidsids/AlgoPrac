N = int(input())
K = int(input())
sensors = list(map(int,input().split()))

sensors = set(sensors)
sensors = list(sensors)
sensors = sorted(sensors)
sensors_len = len(sensors)
dist = list()
for n in range(1, sensors_len):
    dist.append(sensors[n] - sensors[n-1])
dist = sorted(dist, reverse=True)
if K >= N:
    print(0)
else:
    print(sum(dist[K-1:]))