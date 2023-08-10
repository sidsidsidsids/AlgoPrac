N, X = map(int,input().split())
data = list(map(int,input().split()))

l = 0
value = sum(data[l:X])
maxValue = value
maxCount = 1
for nl in range(1, N-X+1):
    value = value - data[nl-1] + data[nl+X-1]
    if value == maxValue:
        maxCount += 1
    elif value > maxValue:
        maxValue = value
        maxCount = 1

if not value and not maxValue:
    print("SAD")
else:
    print(maxValue)
    print(maxCount)



