S = input()
T = input()

len_S = len(S)
def func(elems):
    if elems == S:
        return 1
    if len(elems) <= len_S:
        return 0
    ans = 0
    if elems[-1] == 'A':
        ans = func(elems[:-1])
    if ans == 1:
        return 1
    if elems[0] == 'B':
        ans = func(elems[::-1][:-1])
    return ans

print(func(T))