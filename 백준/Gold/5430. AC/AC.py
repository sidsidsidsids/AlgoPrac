from collections import deque

T = int(input())
for t in range(T):
    ans = ''
    Q = deque()
    revQ = deque()
    action = str(input())
    actlen = len(action)
    N = int(input())
    nums = input()[1:-1].split(',')
    Q.extend(nums)
    revQ.extendleft(nums)
    isRev = 0

    for idx in range(actlen):
        if action[idx] == 'R':
            if isRev:
                isRev -= 1
            else:
                isRev += 1
        elif action[idx] == 'D':
            if isRev:
                if Q:
                    elem = Q.pop()
                    if elem == '':
                        ans = 'error'
                        break
                    revQ.popleft()
                else:
                    ans = 'error'
                    break
            else:
                if Q:
                    elem = Q.popleft()
                    if elem == '':
                        ans = 'error'
                        break
                    revQ.pop()
                else:
                    ans = 'error'
                    break
        # print(idx,'번째',' reverse?:', isRev, Q, revQ)

    if ans:
        print(ans)
    else:
        if isRev:
            ansStr = ''
            for elem in revQ:
                ansStr += str(elem) + ","
            ansStr = ansStr[:-1]
        else:
            ansStr = ''
            for elem in Q:
                ansStr += str(elem) + ","
            ansStr = ansStr[:-1]
        ans = '[' + ansStr + ']'
        print(ans)