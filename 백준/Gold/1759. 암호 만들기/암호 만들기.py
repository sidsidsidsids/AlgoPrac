L, C = map(int,input().split())
arr = list(input().split())
arr = sorted(arr)
V = [0] * C
def func(s, c, ja, mo, i):
    if c >= L:
        if ja >= 2 and mo >= 1:
            print(s)
        return
    for idx in range(i, C):
        if not V[idx]:
            V[idx] = 1
            if arr[idx] in ['a', 'e', 'i', 'o', 'u']:
                func(s + arr[idx], c + 1, ja, mo + 1, idx+1)
            else:
                func(s + arr[idx], c + 1, ja + 1, mo, idx+1)
            V[idx] = 0
func('', 0, 0, 0, 0)
