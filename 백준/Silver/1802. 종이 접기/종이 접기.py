T = int(input())
ans = [0] * T
for t in range(T):
    case = str(input())
    able = True

    def check(size: int, center_loc: int):
        global able
        if size <= 2 or not able:
            return
        else:
            for i in range(1, (size + 1) // 2):
                if case[center_loc - i] == case[center_loc + i]:
                    able = False
                    return
                else:
                    pass
            check((size + 1) // 2, center_loc - ((size + 1) // 2) // 2)
            check((size + 1) // 2, center_loc + ((size + 1) // 2) // 2)

    case_len = len(case)
    for n in range(12):
        if 2 ** n >= case_len:
            check(2 ** n, case_len // 2)
            break

    if able:
        ans[t] = 'YES'
    else:
        ans[t] = 'NO'
for elem in ans:
    print(elem)

