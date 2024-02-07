from collections import deque
import sys
input = sys.stdin.readline
word = list(str(input().rstrip('\n')))
N = int(input())
L_word = deque()
R_word = deque()
for w in word:
    L_word.append(w)
for _ in range(N):
    actions = input().split()
    if actions[0] == "L":
        if L_word:
            elem = L_word.pop()
            R_word.appendleft(elem)
    elif actions[0] == "D":
        if R_word:
            elem = R_word.popleft()
            L_word.append(elem)
    elif actions[0] == "B":
        if L_word:
            L_word.pop()
    else: #actions[0] == "P"
        L_word.append(actions[1])
if L_word:
    for w in L_word:
        print(w, end="")
if R_word:
    for w in R_word:
        print(w, end="")