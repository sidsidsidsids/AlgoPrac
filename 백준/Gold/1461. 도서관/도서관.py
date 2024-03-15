N, M = map(int,input().split())
arr = list(map(int,input().split()))

left = []
right = []
for elem in arr:
    if elem > 0:
        right.append(elem)
    else:
        left.append(elem)
left.sort()
right.sort(reverse=True)

left_max = 0
right_max = 0
ans = 0
for n in range(0, len(left), M):
    val = -left[n]
    if not left_max:
        left_max = val
        ans += val
    else:
        ans += val * 2
for n in range(0, len(right), M):
    val = right[n]
    if not right_max:
        right_max = val
        ans += val
    else:
        ans += val * 2

if left_max >= right_max:
    ans += right_max
else:
    ans += left_max

print(ans)