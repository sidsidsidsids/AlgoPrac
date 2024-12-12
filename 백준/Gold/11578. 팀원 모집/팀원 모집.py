N, M = map(int, input().split())
arr = []
for _ in range(M):
    info = list(map(int, input().split()))
    arr.append(info[1:])
check = [0] * N

answer = M + 1
def func(idx, cnt):
    global answer
    if cnt >= answer:
        return
    if idx == M:
        for n in range(N):
            if not check[n]:
                break
        else:
            answer = min(answer, cnt)
        return

    for elem in arr[idx]:
        check[elem - 1] += 1
    func(idx + 1, cnt + 1)
    for elem in arr[idx]:
        check[elem - 1] -= 1
    func(idx + 1, cnt)

func(0, 0)
print(answer if answer != M + 1 else -1)