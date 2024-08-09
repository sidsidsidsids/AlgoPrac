import sys

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    n_val = 0
    x_val = 0

    left, right = sys.stdin.readline().rstrip('\n').split('=')
    stk = ''
    temp = ''
    for elem in left:
        if elem == '+':
            if temp:
                if stk == '+' or stk == '':
                    n_val += int(temp)
                else:
                    n_val -= int(temp)
                temp = ''
            stk = '+'
        elif elem == '-':
            if temp:
                if stk == '+' or stk == '':
                    n_val += int(temp)
                else:
                    n_val -= int(temp)
                temp = ''
            stk = '-'
        elif elem == 'x':
            if temp:
                if stk == '+' or stk == '':
                    x_val -= int(temp)
                else:
                    x_val += int(temp)
                temp = ''
            else:
                if stk == '+' or stk == '':
                    x_val -= 1
                else:
                    x_val += 1
            stk = ''
        else:
            temp += elem

    if temp:
        if stk == '+' or stk == '':
            n_val += int(temp)
        else:
            n_val -= int(temp)
    stk = ''
    temp = ''
    for elem in right:
        if elem == '+':
            if temp:
                if stk == '+' or stk == '':
                    n_val -= int(temp)
                else:
                    n_val += int(temp)
                temp = ''
            stk = '+'
        elif elem == '-':
            if temp:
                if stk == '+' or stk == '':
                    n_val -= int(temp)
                else:
                    n_val += int(temp)
                temp = ''
            stk = '-'
        elif elem == 'x':
            if temp:
                if stk == '+' or stk == '':
                    x_val += int(temp)
                else:
                    x_val -= int(temp)
                temp = ''
            else:
                if stk == '+' or stk == '':
                    x_val += 1
                else:
                    x_val -= 1
            stk = ''
        else:
            temp += elem

    if temp:
        if stk == '+' or stk == '':
            n_val -= int(temp)
        else:
            n_val += int(temp)
    if n_val and x_val:
        print(n_val // x_val)
    elif n_val == 0 and x_val == 0:
        print('IDENTITY')
    elif n_val == 0:
        print(0)
    else:
        print('IMPOSSIBLE')
