import sys

N, M = map(int, sys.stdin.readline().strip().split())
answer = list(map(int, sys.stdin.readline().strip().split()))
models = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

maxima = 0
for model in models:
    cnt = 0
    for m in range(M):
        if answer[m] == model[m]:
            cnt += 1
    maxima = max(cnt, maxima)

flag = False
def func(idx, used, arr):
    global flag
    if flag:
        return
    if idx == N:
        if used >= 3 and used % 2:
            estimate = [0] * M
            for m in range(M):
                if arr[m] - ((used + 1) // 2) >= 0:
                    estimate[m] = 1
            cnt = 0
            for m in range(M):
                if answer[m] == estimate[m]:
                   cnt += 1
            if cnt > maxima:
                flag = True
        return

    func(idx + 1, used, arr[:])
    for m in range(M):
        arr[m] += models[idx][m]
    func(idx + 1, used + 1, arr[:])

func(0, 0, [0] * M)
print(1 if flag else 0)