import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip('\n').split())
customer = list(map(int, sys.stdin.readline().rstrip('\n').split()))

togi = 0
coffee = 0
result = True
Q = deque()
customer.append(2000001)
c = 0

for i in range(customer[-2] + 1):
    # print(i, togi, coffee, Q)
    while i + M >= customer[c]:
        Q.append(customer[c])
        c += 1
    if Q and i == Q[0]:
        if coffee:
            coffee -= 1
            Q.popleft()
            pass
        else:
            result = False
            break
    else:
        if Q and coffee < len(Q):
            if togi:
                togi -= 1
                coffee += 1
            else:
                togi += 1
        else:
            togi += 1

print("success" if result else "fail")
