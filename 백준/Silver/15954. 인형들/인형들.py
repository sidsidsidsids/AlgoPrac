import math

n, K = map(int,input().split())
preference = list(map(int,input().split()))
def dist(m, list):
    result = 0
    for i in list:
        result += (i - m) ** 2
    return result / len(list)

results = []
for i in range(n - K + 1):
    for j in range(n - K - i + 2):
        tmp = preference[i:i + K + j]
        m = sum(tmp) / len(tmp)
        dis = dist(m, tmp)
        results.append(dis)

result = min(results)
print(math.sqrt(result))