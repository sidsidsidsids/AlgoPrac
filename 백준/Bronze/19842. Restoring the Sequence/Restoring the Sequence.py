n = int(input())
m = int(input())
a = list(map(int, input().split()))

def func(arr):
    if n - m != 1:
        print("No")
        return

    sort_copy = sorted(arr)
    if arr != sort_copy:
        print("No")
        return

    s = set()
    for num in arr:
        s.add(num)

    if len(s) != m:
        print("No")
        return

    answer = -1
    for num in range(1, n+1):
        if num in s:
            s.remove(num)
        else:
            if answer == -1:
                answer = num
            else:
                print("No")
                return

    if not s:
        print("Yes")
        print(answer)
    else:
        print("No")
    return

func(a)