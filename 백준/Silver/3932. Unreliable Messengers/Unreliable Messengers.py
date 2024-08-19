import sys
from collections import deque

def change(follower: str, deq: deque, D: int):
    if follower == 'J':
        elem = deq.pop()
        deq.appendleft(elem)
    elif follower == 'C':
        elem = deq.popleft()
        deq.append(elem)
    elif follower == 'E':
        half = D // 2
        left = deque(); right = deque()
        for _ in range(half):
            left.append(deq.popleft())
            right.append(deq.pop())
        deq.extendleft(right); deq.extend(left)
    elif follower == 'A':
        deq.reverse()
    elif follower == 'P':
        for i in range(D):
            if deq[i].isdigit():
                if deq[i] == '0':
                    deq[i] = '9'
                else:
                    deq[i] = str(int(deq[i]) - 1)
    elif follower == 'M':
        for i in range(D):
            if deq[i].isdigit():
                if deq[i] == '9':
                    deq[i] = '0'
                else:
                    deq[i] = str(int(deq[i]) + 1)

    return deq

N = int(sys.stdin.readline().rstrip('\n'))
for _ in range(N):
    followers = sys.stdin.readline().rstrip('\n')
    F = len(followers)
    message = sys.stdin.readline().rstrip('\n')
    M = len(message)
    msg = deque()
    for e in message:
        msg.append(e)
    for f in range(F-1, -1, -1):
        msg = change(followers[f], msg, M)
    answer = ''
    for e in msg:
        answer += e
    print(answer)