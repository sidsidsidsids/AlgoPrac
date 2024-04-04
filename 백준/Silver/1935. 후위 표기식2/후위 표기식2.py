N = int(input())
a = [0] * N
v = list(input())
for n in range(N):
    a[n] = int(input())

def solution(length, calculate, array):
    stack = []
    for cal in calculate:
        if cal != '+' and cal != '-' and cal != '/' and cal != '*':
            stack.append(array[ord(cal) - 65])
        else:
            elem_2 = stack.pop()
            elem_1 = stack.pop()
            if cal == '+':
                stack.append(elem_1 + elem_2)
            elif cal == '-':
                stack.append(elem_1 - elem_2)
            elif cal == '*':
                stack.append(elem_1 * elem_2)
            elif cal == '/':
                stack.append(elem_1 / elem_2)
    return stack[0]

print("{:.2f}".format(solution(N, v, a)))