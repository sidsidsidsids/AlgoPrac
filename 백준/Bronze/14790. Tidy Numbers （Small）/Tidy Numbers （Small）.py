import sys

T = int(sys.stdin.readline().rstrip('\n'))
for t in range(T):
    N = int(sys.stdin.readline().rstrip('\n'))
    S = str(N)
    L = len(S)
    arr = []
    for s in S:
        arr.append(int(s))

    for i in range(L - 2, -1, -1):
        if arr[i] > arr[i+1]:
            arr[i] -= 1
            for j in range(i+1, L):
                arr[j] = 9
    ans = ""
    for elem in arr:
        ans += str(elem)
    ans = int(ans)

    print(f'Case #{t + 1}: {ans}')