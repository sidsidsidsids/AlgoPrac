S = input()
r = len(S) - 1
l = 0
while l < r:
    if S[l] != S[r]:
        print(0)
        break
    l += 1
    r -= 1
else:
    print(1)