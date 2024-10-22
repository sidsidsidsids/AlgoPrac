import sys

N, S = map(int, sys.stdin.readline().rstrip('\n').split())
arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

answer = 0
record = set()
init = [0] * N
record.add(str(init[:]))
def func(idx: int, cnt: list, val: int):
    global answer
    global record
    R = str(cnt)
    if val == S and R not in record:
        answer += 1
        record.add(R)
    if idx == N:
        return
    v = arr[idx]
    cnt[idx] = 1
    func(idx + 1, cnt[:], val + v)
    cnt[idx] = 0
    func(idx + 1, cnt[:], val)

func(0, init[:], 0)
print(answer)