N = int(input())
arr = list(map(int,input().split()))
if len(arr) == 1:
    print('A')
elif len(arr) == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A')
else:
    l = 0
    r = 1
    answer = set()
    for a in range(-200,200):
        b = arr[r] - arr[l] * a
        l += 1
        r += 1
        flag = True
        while r < len(arr):
            if arr[l] * a + b != arr[r]:
                flag = False
                break
            l += 1
            r += 1
        if flag:
            answer.add(arr[l] * a + b)
            if len(answer) > 1:
                break
        l = 0
        r = 1
    if len(answer) > 1:
        print('A')
    elif len(answer) == 1:
        print(answer.pop())
    else:
        print('B')