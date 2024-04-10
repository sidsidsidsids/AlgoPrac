a = input()

def fun(arr):
    stack = []
    temp = [0] * 31
    depth = 0
    flag = True
    for a in arr:
        if a == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
                if temp[depth + 1]:
                    temp[depth] += 2 * temp[depth + 1]
                    temp[depth + 1] = 0
                else:
                    temp[depth] += 2
                depth -= 1
        elif a == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            else:
                stack.pop()
                if temp[depth + 1]:
                    temp[depth] += 3 * temp[depth + 1]
                    temp[depth + 1] = 0
                else:
                    temp[depth] += 3
                depth -= 1
        else:
            stack.append(a)
            depth += 1
    if not flag or stack:
        answer = 0
    else:
        answer = temp[1]
    return answer

print(fun(a))
