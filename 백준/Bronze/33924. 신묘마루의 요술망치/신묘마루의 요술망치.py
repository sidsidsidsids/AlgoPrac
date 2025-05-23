N, M = map(int, input().split())
arr = [0] * 9
arr[(N-1) * 2 + (M-1) + 1] = 1
K = int(input())
S = input()
for s in S:
    if s == "A":
        arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = \
            arr[5], arr[6], arr[7], arr[8], arr[1], arr[2], arr[3], arr[4]
    elif s == "B":
        arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = \
            arr[4], arr[3], arr[2], arr[1], arr[8], arr[7], arr[6], arr[5]
    elif s == "C":
        arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = \
            arr[8], arr[7], arr[6], arr[5], arr[4], arr[3], arr[2], arr[1]
    elif s == "D":
        arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = \
            arr[3], arr[1], arr[5], arr[2], arr[7], arr[4], arr[8], arr[6]
for i in range(1, 9):
    if arr[i]:
        print((i - 1) // 2 + 1, 1 if i % 2 else 2)
        break
