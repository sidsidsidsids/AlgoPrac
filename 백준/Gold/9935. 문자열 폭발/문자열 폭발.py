original = input()
explosion = input()
checklen = len(explosion)
target = explosion[-1]
stack = []

for word in original:
    if word == target and len(stack) >= checklen - 1:
        ableBreak = True
        for idx in range(1, checklen):
            if explosion[-(idx+1)] == stack[-idx]:
                pass
            else:
                ableBreak = False
                break
        if ableBreak:
            for _ in range(checklen - 1):
                stack.pop()
        else:
            stack.append(word)
    else:
        stack.append(word)

if stack:
    for s in stack:
        print(s,end="")
else:
    print("FRULA")