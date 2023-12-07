import sys
input = sys.stdin.readline
N = int(input())
people = [0] * 100001
inputMax = 0
for _ in range(N):
    inputVal = int(input())
    people[inputVal] += 1
    if inputVal > inputMax:
        inputMax = inputVal
people = people[:inputMax+1]

ans = 0
idx = inputMax
order = 1
while True:
    if people[idx]:
        check = idx - (order - 1)
        if check > 0:
            ans += check
            people[idx] -= 1
            order += 1
            if order > N:
                break
        else:
            idx -= 1
            if not idx:
                break
    else:
        idx -= 1
        if not idx:
            break


print(ans)