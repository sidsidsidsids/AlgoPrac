import sys
S = sys.stdin.readline().rstrip('\n')
L = len(S)
arr = [[0] * (L + 1) for _ in range(26)]
for j in range(1, L+1):
    num = ord(S[j-1]) - 97
    for i in range(26):
        if i == num:
            arr[i][j] = arr[i][j-1] + 1
        else:
            arr[i][j] = arr[i][j-1]

q = int(sys.stdin.readline().rstrip('\n'))
answer = []
for _ in range(q):
    a, l, r = sys.stdin.readline().rstrip('\n').split()
    l = int(l)
    r = int(r) + 1
    a = ord(a) - 97
    answer.append(arr[a][r] - arr[a][l])
for ans in answer:
    print(ans)