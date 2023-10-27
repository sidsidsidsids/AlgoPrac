N, K, B = map(int,input().split())
lights = [0] * N
for _ in range(B):
    target = int(input())
    lights[target-1] = 1
value = sum(lights[:K])
minimum = value
for n in range(1, N-K+1):
    value += lights[n+K-1] - lights[n-1]
    # print('value: ', value, ' plus idx: ', n+K-1,'val: ', lights[n+K-1], 'minus idx: ', n-1,'val: ', lights[n-1])
    if value < minimum:
        minimum = value
print(minimum)