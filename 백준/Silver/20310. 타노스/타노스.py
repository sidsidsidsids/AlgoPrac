arr = list(input())
arr_len = len(arr)
cnt_0 = 0
cnt_1 = 0
for elem in arr:
    if elem == "0":
        cnt_0 += 1
    else:
        cnt_1 += 1
goal_0 = cnt_0 // 2
goal_1 = cnt_1 // 2
cur_0 = 0
del_0 = 0
del_1 = 0
idx = 0
while idx < arr_len and (del_0 < goal_0 or del_1 < goal_1):
    if arr[idx] == "0":
        if cur_0 == goal_0:
            if del_0 < goal_0:
                arr[idx] = -1
                del_0 += 1
            else:
                pass
        else:
            cur_0 += 1
    else: # arr[idx] == "1"
        if del_1 == goal_1:
            pass
        else:
            arr[idx] = -1
            del_1 += 1
    idx += 1
for elem in arr:
    if elem != -1:
        print(elem, end="")