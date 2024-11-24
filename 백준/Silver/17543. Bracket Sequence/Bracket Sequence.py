import sys
N = int(sys.stdin.readline().rstrip('\n'))
tokens = list(int(x) if x not in "()" else x for x in sys.stdin.readline().rstrip('\n').split())
stk = []
depth = 0
modulo = 10 ** 9 + 7
for token in tokens:
    if token == '(':
        stk.append('(')
        depth += 1
    elif token == ')':
        if depth % 2:
            value = 1
            while stk[-1] != '(':
                value *= stk.pop()
                value %= modulo
            stk.pop()
            stk.append(value)
        else:
            value = 0
            while stk[-1] != '(':
                value += stk.pop()
                value %= modulo
            stk.pop()
            stk.append(value)
        depth -= 1
    else:
        stk.append(token)
print(sum(stk) % modulo)