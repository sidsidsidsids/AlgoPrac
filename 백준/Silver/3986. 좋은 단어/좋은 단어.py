import sys

T = int(sys.stdin.readline().rstrip('\n'))
answer = 0
for _ in range(T):
    S = sys.stdin.readline().rstrip('\n')
    if len(S) % 2:
        continue
    stk = []
    for s in S:
        if stk and stk[-1] == s:
            stk.pop()
        else:
            stk.append(s)
    if not stk:
        answer += 1
print(answer)