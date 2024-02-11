R, C, N = map(int,input().split())
arr = [list(input()) for _ in range(R)]
if N <= 1:
    pass
else:
    if (N-2) % 4 == 1 or (N-2) % 4 == 3:
        new_arr = [list("O" * C) for _ in range(R)]
        new_next_arr = False
        for i in range(R):
            for j in range(C):
                if arr[i][j] == "O":
                    for ni, nj in [[i-1,j],[i+1,j],[i,j+1],[i,j-1],[i,j]]:
                        if 0 <= ni < R and 0 <= nj < C:
                            new_arr[ni][nj] = "."
        if (N-2) % 4 == 3:
            new_next_arr = [list("O" * C) for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    if new_arr[i][j] == "O":
                        for ni, nj in [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1], [i, j]]:
                            if 0 <= ni < R and 0 <= nj < C:
                                new_next_arr[ni][nj] = "."
        if not new_next_arr:
            arr = new_arr[:]
        else:
            arr = new_next_arr[:]
    else:
        arr = [list("O" * C) for _ in range(R)]

for i in range(R):
    for j in range(C):
        print(arr[i][j], end="")
    print()