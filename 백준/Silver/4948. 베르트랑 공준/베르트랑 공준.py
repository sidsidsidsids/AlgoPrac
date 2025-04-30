import math

M = 123456 * 2
arr = [True] * (M + 1)
arr[0] = arr[1] = False

for i in range(2, int(math.sqrt(M)) + 1):
    if arr[i]:
        for j in range(i*i, M+1, i):
            arr[j] = False

while True:
    num = int(input())
    if num == 0:
        break
    print(sum(arr[num+1:num*2+1]))
