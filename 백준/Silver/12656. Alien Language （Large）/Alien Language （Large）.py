import sys
from collections import deque

L, D, N = map(int, sys.stdin.readline().rstrip('\n').split())

aliens = set()
parents = set()

for _ in range(D):
    word = sys.stdin.readline().rstrip('\n')
    temp = ''
    for elem in word:
        temp += elem
        parents.add(temp)
    aliens.add(temp)

for n in range(1, N+1):
    case = sys.stdin.readline().rstrip('\n')
    flag = False
    is_stk = False
    stk = []
    Q = deque()
    for elem in case:
        if elem == '(':
            is_stk = True
            continue
        elif elem == ')':
            is_stk = False
            if flag and not Q:
                break
            else:
                if not flag:
                    flag = True
                    for w in stk:
                        if w in parents:
                            Q.append(w)
                else:
                    temp_Q = deque()
                    while Q:
                        word = Q.popleft()
                        for w in stk:
                            add_word = word + w
                            if add_word in parents:
                                temp_Q.append(add_word)
                    Q = temp_Q
            stk = []
        else:
            if is_stk:
                stk.append(elem)
                continue
            else:
                if flag and not Q:
                    break
                else:
                    if not flag:
                        flag = True
                        if elem in parents:
                            Q.append(elem)
                    else:
                        temp_Q = deque()
                        while Q:
                            word = Q.popleft()
                            add_word = word + elem
                            if add_word in parents:
                                temp_Q.append(add_word)
                        Q = temp_Q

    size = 0
    for word in Q:
        if word in aliens:
            size += 1
    print(f'Case #{n}: {size}')