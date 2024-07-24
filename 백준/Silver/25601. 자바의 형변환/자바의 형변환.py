import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))

class C:
    def __init__(self, name):
        self.name = name
        self.parent = set()
        self.child = set()

    def add_parent(self, name):
        self.parent.add(name)

    def add_child(self, name):
        self.child.add(name)

info = dict()
for _ in range(N-1):
    A, B = map(str, sys.stdin.readline().rstrip('\n').split())
    if A not in info:
        info[A] = C(A)
    if B not in info:
        info[B] = C(B)
    info[A].add_parent(B)
    info[B].add_child(A)


c1, c2 = map(str, sys.stdin.readline().rstrip('\n').split())

flag = False
Q = deque()
Q.append(c1)
while Q:
    elem = Q.popleft()
    for c in info[elem].parent:
        if c == c2:
            flag = True
            break
        Q.append(c)
    if flag:
        break

if not flag:
    Q.append(c1)
    while Q:
        elem = Q.popleft()
        for c in info[elem].child:
            if c == c2:
                flag = True
                break
            Q.append(c)
        if flag:
            break

print(1 if flag else 0)