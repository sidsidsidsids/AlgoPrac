N = int(input())
ans = [0] * N
for n in range(N):
    arr = input()
    l = 0
    r = len(arr) - 1
    is_pseudo = False
    is_palindrome = True
    while l <= r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            is_pseudo = True
            is_able = False
            if arr[l] == arr[r-1] and not is_able:
                new_l = l
                new_r = r-1
                is_able = True
                while new_l <= new_r:
                    if arr[new_l] == arr[new_r]:
                        new_l += 1
                        new_r -= 1
                    else:
                        is_able = False
                        break
            if arr[l+1] == arr[r] and not is_able:
                new_l = l + 1
                new_r = r
                is_able = True
                while new_l <= new_r:
                    if arr[new_l] == arr[new_r]:
                        new_l += 1
                        new_r -= 1
                    else:
                        is_able = False
                        break
            if not is_able:
                is_palindrome = False
            break
    if not is_pseudo and is_palindrome:
        ans[n] = 0
    elif is_pseudo and is_palindrome:
        ans[n] = 1
    else:
        ans[n] = 2

for a in ans:
    print(a)