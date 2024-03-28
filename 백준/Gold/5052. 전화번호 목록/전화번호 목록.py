T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    book = dict()
    for n in range(N):
        nums = str(input())
        book[nums] = 1
    answer = "YES"
    for k, v in book.items():
        k_len = len(k)
        for i in range(k_len):
            if k[:i] in book.keys():
                answer = "NO"
                break
        if answer == "NO":
            break
    ans.append(answer)
for a in ans:
    print(a)