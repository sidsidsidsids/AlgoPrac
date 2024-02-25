N, M, H = map(int,input().split())
table = [0] * (H+1)
cases = set()
for _ in range(N):
    arr = list(map(int,input().split()))
    tmp_table = [0] * (H+1)
    new_case = set()
    for elem in arr:
        if elem <= H:
            new_case.add(elem)
            tmp_table[elem] += 1
        for case in cases:
            if case + elem <= H:
                new_case.add(case + elem)
                tmp_table[case + elem] += table[case]
    for elem in new_case:
        table[elem] += tmp_table[elem]
        tmp_table[elem] = 0
    cases.update(new_case)
print(table[H] % 10007)