import sys
sys.setrecursionlimit(40000)

N = int(input())
ans = [0]
def func(value, depth):
    if depth == N:
        if value % 3 == 0 and depth != 0:
            ans[0] += 1
        return
    if depth != 0:
        func(value, depth + 1)
    func(value + 1, depth + 1)
    func(value + 2, depth + 1)
func(0, 0)
print(ans[0])
