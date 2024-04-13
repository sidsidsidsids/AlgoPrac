arr = input()

def func(array):
    answer = 0
    stack = []
    flag = False
    for elem in array:
        if elem == '(':
            flag = True
            stack.append(elem)
        else:
            if flag:
                stack.pop()
                answer += len(stack)
                flag = False
            else:
                stack.pop()
                answer += 1
    return answer

print(func(arr))