T = int(input())
for _ in range(T):
    word = list(input())
    word_len = len(word)
    i, j = 0, 1
    for idx in range(1, word_len):
        if word[idx] > word[idx - 1]:
            if i < idx:
                i = idx
    for idx in range(1, word_len):
        if word[idx] > word[i - 1]:
            if j < idx:
                j = idx
    if i and j:
        word[i-1], word[j] = word[j], word[i-1]
        word[i:] = list(reversed(word[i:]))
    for w in word:
        print(w, end="")
    print()