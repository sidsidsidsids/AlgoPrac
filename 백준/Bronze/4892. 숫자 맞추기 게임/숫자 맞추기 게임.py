import sys

answers = []
num = 1
while True:
    n0 = int(sys.stdin.readline())
    if not n0:
        break
    elems = [str(num) + "."]
    n1 = 3 * n0
    if n1 % 2:
        n2 = (n1 + 1) // 2
        elems.append("odd")
    else:
        n2 = n1 // 2
        elems.append("even")
    n3 = 3 * n2
    n4 = n3 // 9
    elems.append(n4)
    answers.append(elems)
    num += 1
for answer in answers:
    print(*answer)