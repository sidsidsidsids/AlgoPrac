L = list(map(int, input().split()))

def changer(l, r):
    if L[l] > L[r]:
        L[l], L[r] = L[r], L[l]
        print(*L)

while True:
    for i in range(0, 4):
        changer(i, i+1)
    if L == [1, 2, 3, 4, 5]:
        break