N = int(input())
cnt = 0
vowels = {97, 101, 105, 111, 117}
answer = ''
def generator(name, n):
    global cnt
    global answer
    if cnt == N:
        return
    if n == 5:
        answer += name + '\n'
        cnt += 1
        return
    if n % 2:
        for elem in vowels:
            generator(name + chr(elem), n + 1)
    else:
        for elem in range(97, 123):
            if elem in vowels:
                continue
            else:
                generator(name + chr(elem), n + 1)
generator('', 0)
print(answer)