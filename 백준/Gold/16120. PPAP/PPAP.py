import sys

N = sys.stdin.readline().strip()

cnt = 0
stk = []
for e in N:
    stk.append(e)
    cnt += 1
    while cnt >= 4 and stk[-4:] == ['P', 'P', 'A', 'P']:
        stk.pop()
        stk.pop()
        stk.pop()
        cnt -= 3
print("PPAP" if stk == ['P'] else "NP")
