import sys

N = int(sys.stdin.readline().strip())
sticks = []
for _ in range(N):
    sticks.append(int(sys.stdin.readline().strip()))

stack = []
for n in range(N-1, -1, -1):
    if not stack:
        stack.append(sticks[n])
        continue
    if sticks[n] > stack[-1]:
        stack.append(sticks[n])

print(len(stack))