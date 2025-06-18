N, M = map(int, input().split())
counter = [0] * M
maxima = -1
total = 0
for _ in range(N):
    value = 0
    inputs = list(input().split())
    for m in range(M):
        nine = inputs[m].count("9")
        total += nine
        value += nine
        counter[m] += nine
    maxima = max(value, maxima)

print(total - max(max(counter), maxima))