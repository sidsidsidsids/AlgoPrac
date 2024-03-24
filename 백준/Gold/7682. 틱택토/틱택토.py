answer = []
while True:
    c = input()
    if c == 'end':
        break

    cnt_x = 0
    cnt_o = 0
    is_finish = True
    for com in c:
        if com == 'X':
            cnt_x += 1
        elif com == 'O':
            cnt_o += 1
        elif com == '.':
            is_finish = False

    if cnt_x - cnt_o != 1 and cnt_x - cnt_o != 0:
        answer.append('invalid')
        continue

    check_x = False
    check_o = False
    if c[0] == c[1] == c[2] == 'X' or c[3] == c[4] == c[5] == 'X' or c[6] == c[7] == c[8] == 'X' \
        or c[0] == c[3] == c[6] == 'X' or c[1] == c[4] == c[7] == 'X' or c[2] == c[5] == c[8] == 'X' \
            or c[0] == c[4] == c[8] == 'X' or c[2] == c[4] == c[6] == 'X':
        check_x = True
    if c[0] == c[1] == c[2] == 'O' or c[3] == c[4] == c[5] == 'O' or c[6] == c[7] == c[8] == 'O' \
        or c[0] == c[3] == c[6] == 'O' or c[1] == c[4] == c[7] == 'O' or c[2] == c[5] == c[8] == 'O' \
            or c[0] == c[4] == c[8] == 'O' or c[2] == c[4] == c[6] == 'O':
        check_o = True

    if (check_o and check_x) or (not check_o and not check_x and not is_finish):
        answer.append('invalid')
        continue
    else:
        if (check_o and cnt_x > cnt_o) or (check_x and cnt_x == cnt_o):
            answer.append('invalid')
            continue
    answer.append('valid')

for a in answer:
    print(a)