import sys

T = int(sys.stdin.readline().rstrip('\n'))
result = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip('\n').split()))

    tree = [0] * (N * 4)
    def init(start, end, idx):
        if start == end:
            tree[idx] = arr[start]
            return tree[idx]
        mid = (start + end) // 2
        tree[idx] = max(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))
        return tree[idx]

    init(0, N-1, 1)
    def func(start, end, idx, left, right):
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return tree[idx]
        mid = (start + end) // 2
        return max(func(start, mid, idx * 2, left, right), func(mid + 1, end, idx * 2 + 1, left, right))

    visit = [-1] * (N + 1)
    flag = True
    for n in range(N):
        elem = arr[n]
        if visit[elem] != -1:
            maxima = func(0, N-1, 1, visit[elem], n)
            if maxima > elem:
                flag = False
                break
        visit[elem] = n

    result.append("Yes" if flag else "No")

sys.stdout.write("\n".join(map(str, result)))