N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def func(N, array):
    H = N // 2
    tmp = [[] for _ in range(H)]
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            check = []
            for ni in range(i, i + 2):
                for nj in range(j, j + 2):
                    check.append(array[ni][nj])
            check.sort(reverse=True)
            tmp[i // 2].append(check[1])
    return tmp

while N > 1:
    result = func(N, arr)
    arr = result[:]
    N = N // 2

print(arr[0][0])