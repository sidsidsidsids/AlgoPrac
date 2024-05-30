from collections import deque
s = input()
t = input()
deq = deque()
for elem in t:
    deq.append(elem)
L_s = len(s)
L_t = len(t)
is_reverse = False;
while L_t > L_s:
    if not is_reverse:
        output = deq.pop()
        if output == 'B':
            is_reverse = True
    else:
        output = deq.popleft()
        if output == 'B':
            is_reverse = False
    L_t -= 1
r = ''
if not is_reverse:
    while deq:
        r += deq.popleft()
else:
    while deq:
        r += deq.pop()
print(1 if r == s else 0)