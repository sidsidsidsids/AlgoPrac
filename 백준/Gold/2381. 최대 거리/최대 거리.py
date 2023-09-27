N = int(input())
sumMax = -2000000
sumMin = 2000000
difMax = -2000000
difMin = 2000000

for n in range(N):
    a, b = map(int,input().split())
    if a+b > sumMax:
        sumMax = a+b
    if a+b < sumMin:
        sumMin = a+b
    if a-b > difMax:
        difMax = a-b
    if a-b < difMin:
        difMin = a-b
        
print(max(sumMax-sumMin, difMax-difMin))