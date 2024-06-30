square = 125 * 125
j, i = map(int,input().split())
if j == i == 0:
    print("125.00 125.00")
elif j == i == 125:
    print("0.00 0.00")
else:
    if j == 0:
        if i <= 125:
            x = 2 * square / (250 - i)
            y = 250.00 - x
        else:
            x = 2 * square / i
            y = 0.00
        print("{:.2f}".format(x), "{:.2f}".format(y))
    elif i == 0:
        if j <= 125:
            y = 2 * square / (250 - j)
            x = 250 - y
        else:
            y = 2 * square / j
            x = 0.00
        print("{:.2f}".format(x), "{:.2f}".format(y))
    elif j > i:
        y = 250 - (2 * square / j)
        print("0.00", "{:.2f}".format(y))
    else:
        x = 250 - (2 * square / i)
        print("{:.2f}".format(x), "0.00")