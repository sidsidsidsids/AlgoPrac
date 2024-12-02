N = int(input())
abcd = list(map(int, input().split()))
burger = input()

def use(char):
    target = ord(char) - 97
    if abcd[target] <= 0:
        return False
    abcd[target] -= 1
    return True

def check(idx):
    if N == 1 and burger[idx] == 'a':
        return True
    elif N == 1:
        return False
    if idx == 0:
        if burger[idx] == burger[idx+1] or burger[idx] != 'a':
            return False
    elif idx == N-1:
        if burger[idx] == burger[idx-1] or burger[idx] != 'a':
            return False
    else:
        if burger[idx] == burger[idx-1] or burger[idx] == burger[idx+1]:
            return False
    return True

for n in range(N):
    cr = check(n)
    ur = use(burger[n])
    if not cr or not ur:
        print("No")
        break
else:
    print("Yes")