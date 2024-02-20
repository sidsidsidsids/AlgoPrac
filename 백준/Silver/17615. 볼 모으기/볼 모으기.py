N = int(input())
arr = list(input())
ans = N

red = 0
blue = 0
start_r = False
start_b = False
if arr[0] == "R":
    start_r = True
else:
    start_b = True
for idx in range(1, N):
    if arr[idx] == "R":
        if start_r:
            pass
        else:
            red += 1
            if start_b:
                start_b = False
    else: # "B"
        if start_b:
            pass
        else:
            blue += 1
            if start_r:
                start_r = False

ans = min(red, blue, ans)

red = 0
blue = 0
start_r = False
start_b = False
if arr[N-1] == "R":
    start_r = True
else:
    start_b = True
for idx in range(N-1, -1, -1):
    if arr[idx] == "R":
        if start_r:
            pass
        else:
            red += 1
            if start_b:
                start_b = False
    else: # "B"
        if start_b:
            pass
        else:
            blue += 1
            if start_r:
                start_r = False

ans = min(red, blue, ans)

print(ans)