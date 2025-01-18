L = int(input())
A = list(map(int, input().split()))
V = [0] * 10

def func(s, e):
    if s == 1:
        if e == 3 and not V[2]:
            return False
        elif e == 7 and not V[4]:
            return False
        elif e == 9 and not V[5]:
            return False
        else:
            return True
    elif s == 2:
        if e == 8 and not V[5]:
            return False
        else:
            return True
    elif s == 3:
        if e == 7 and not V[5]:
            return False
        elif e == 9 and not V[6]:
            return False
        else:
            return True
    elif s == 4:
        if e == 6 and not V[5]:
            return False
        else:
            return True
    elif s == 7:
        if e == 9 and not V[8]:
            return False
        else:
            return True
    return True

start = A[0]
V[start] = 1
for l in range(1, L):
    end = A[l]
    if V[end]:
        print("NO")
        break
    able = func(min(start, end), max(start, end))
    if able:
        V[end] = 1
        start = end
        continue
    else:
        print("NO")
        break
else:
    print("YES")