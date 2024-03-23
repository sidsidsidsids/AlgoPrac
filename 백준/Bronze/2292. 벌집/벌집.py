N = int(input())
def func(num):
    answer = 0
    if num == 1:
        answer = 1
    else:
        val = 1
        for n in range(1, num):
            val += 6 * n
            if num <= val:
                answer = n + 1
                break
    return answer
print(func(N))