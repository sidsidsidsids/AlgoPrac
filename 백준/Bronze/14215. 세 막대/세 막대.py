S = list(map(int, input().split()))
S.sort()
if S[-1] < S[-3] + S[-2]:
    print(sum(S))
else:
    print(sum(S[:-1]) * 2 - 1)