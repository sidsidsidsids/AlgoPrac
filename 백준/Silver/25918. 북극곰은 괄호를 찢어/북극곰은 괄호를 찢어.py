N = int(input())
S = input()
ans = 0
val = 0
for s in S:
    if s == '(':
        val += 1
    else:
        val -= 1
    ans = max(abs(val), ans)
print(ans if not val else -1)