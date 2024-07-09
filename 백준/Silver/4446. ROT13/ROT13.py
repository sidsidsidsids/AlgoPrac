mo = ["a", "i", "y", "e", "o", "u"]
ja = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

check = set()
for m in mo:
    check.add(m)

while True:
    try:
        temp = input()
        answer = ""
        for elem in temp:
            if elem.isalpha():
                flag = False
                if elem.isupper():
                    elem = elem.lower()
                    flag = True
                if elem in check:
                    idx = mo.index(elem)
                    elem = mo[(idx + 3) % 6]
                else:
                    idx = ja.index(elem)
                    elem = ja[(idx + 10) % 20]
                if flag:
                    elem = elem.upper()
            answer += elem
        print(answer)
    except:
        break