sound = input()
quack = [0] * 5

def func(s):
    if s == 'q':
        quack[1] += 1
    elif s == 'u':
        if quack[1] > quack[2]:
            quack[2] += 1
        else:
            return False
    elif s == 'a':
        if quack[2] > quack[3]:
            quack[3] += 1
        else:
            return False
    elif s == 'c':
        if quack[3] > quack[4]:
            quack[4] += 1
        else:
            return False
    elif s == 'k':
        if quack[4]:
            quack[0] = max(quack[0], quack[1])
            quack[4] -= 1
            quack[3] -= 1
            quack[2] -= 1
            quack[1] -= 1
        else:
            return False
    return True

def able():
    if sum(quack[1:]) > 0:
        return False
    else:
        return True

for e in sound:
    res = func(e)
    if not res:
        print(-1)
        break
else:
    if able():
        print(quack[0])
    else:
        print(-1)