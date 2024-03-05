N = int(input())
word = input()
len_word = len(word)
target = [0] * 123
cnt = 0
for elem in word:
    target[ord(elem)] += 1
for _ in range(N-1):
    comp = input()
    temp = target[:]
    r = 0
    w = 0
    for i in comp:
        idx = ord(i)
        if temp[idx] > 0:
            r += 1
        else:
            w += 1
        temp[idx] -= 1
    if len_word - r <= 1 and w <= 1:
        cnt += 1
print(cnt)