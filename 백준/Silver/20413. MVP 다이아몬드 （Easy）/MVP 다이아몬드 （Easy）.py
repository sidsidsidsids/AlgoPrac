import sys
from collections import deque

N = int(sys.stdin.readline().rstrip('\n'))
MVP = dict()
MVP["S"], MVP["G"], MVP["P"], MVP["D"] = map(int, sys.stdin.readline().rstrip('\n').split())
grades = sys.stdin.readline().rstrip('\n')

Q = deque()
answer = 0
current = 0
for grade in grades:
    if len(Q) >= 2:
        current -= Q.popleft()
    if grade == "B":
        addition = max(MVP["S"] - 1 - current, 0)
    elif grade == "S":
        addition = max(MVP["G"] - 1 - current, 0)
    elif grade == "G":
        addition = max(MVP["P"] - 1 - current, 0)
    elif grade == "P":
        addition = max(MVP["D"] - 1 - current, 0)
    elif grade == "D":
        addition = MVP["D"]
    current += addition
    answer += addition
    Q.append(addition)

print(answer)