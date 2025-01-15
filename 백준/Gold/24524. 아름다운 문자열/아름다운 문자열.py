S = input()
T = input()
LT = len(T)
arr = [0] * LT
arrT = list(T)

def func(i, e):
    if i == LT:
        return
    if i == 0:
        if e == arrT[i]:
            arr[i] += 1
        elif arr[i]:
            func(i+1, e)
    else:
        if e == arrT[i] and arr[i-1] and arr[i-1] > arr[i]:
            arr[i] += 1
        elif arr[i]:
            func(i+1, e)

for s in S:
    func(0, s)

print(arr[-1])