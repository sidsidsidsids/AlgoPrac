T = int(input())
answer = []
for _ in range(T):
    v = int(input())
    flag = False
    for i in range(2, int((2 * v) ** 0.5) + 1):
        val, n = divmod((v - i * (i + 1) // 2), i)
        if n:
            continue
        else:
            flag = True
            break
    if flag:
        ans = f'{v} = '
        for num in range(val + 1, val + 1 + i):
            if num != val + i:
                ans += f'{num} + '
            else:
                ans += f'{num}'
    else:
        ans = 'IMPOSSIBLE'
    answer.append(ans)
for elem in answer:
    print(elem)