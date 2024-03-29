N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

s_m1 = 0
s_0 = 0
s_1 = 0

def dq(si, sj, size):
    global s_m1, s_0, s_1
    c_m1 = 0
    c_0 = 0
    c_1 = 0

    for i in range(si, si+size):
        for j in range(sj, sj+size):
            if arr[i][j] == -1:
                c_m1 += 1
            elif arr[i][j] == 0:
                c_0 += 1
            elif arr[i][j] == 1:
                c_1 += 1

    if c_m1 == size**2:
        s_m1 += 1
    elif c_0 == size**2:
        s_0 += 1
    elif c_1 == size**2:
        s_1 += 1
    else:
        for ni in range(si, si+size, size//3):
            for nj in range(sj, sj+size, size//3):
                dq(ni, nj, size//3)

dq(0, 0, N)
print(s_m1)
print(s_0)
print(s_1)