target = input()
num_input = ''
arr = []
for elem in target:
    if elem != '+' and elem != '-':
        num_input += elem
    else:
        arr.append(int(num_input))
        num_input = ''
        arr.append(elem)
if num_input:
    arr.append(int(num_input))

ans = 0
tmp = 0
minus = False
for act in arr:
    if type(act) == int:
        if not minus:
            ans += act
        else:
            tmp += act
    else:
        if act == "-":
            if not minus:
                minus = True
            else:
                ans -= tmp
                tmp = 0
if tmp:
    ans -= tmp
print(ans)