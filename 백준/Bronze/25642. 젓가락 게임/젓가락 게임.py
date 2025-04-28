용태, 유진 = map(int, input().split())
flag = True
while True:
    if flag:
        유진 += 용태
        if 유진 >= 5:
            break
        flag = False
    else:
        용태 += 유진
        if 용태 >= 5:
            break
        flag = True
print("yt" if flag else "yj")