import sys

while True:
    N = int(sys.stdin.readline().rstrip('\n'))
    if N == 0:
        break
    audio = list(sys.stdin.readline().rstrip('\n').split())
    maxsize = sys.maxsize
    minima = -maxsize
    maxima = maxsize
    flag = True

    for n in range(N):
        if maxima - minima < 2:
            flag = False
            break

        if (n+1) % 2:
            is_odd = True
        else:
            is_odd = False

        if audio[n] != "x":
            is_num = True
            mid = int(audio[n])
        else:
            is_num = False
        if is_num:
            left = "init"
            right = "init"
            if n != 0:
                if audio[n-1] != "x":
                    left = int(audio[n-1])
                else:
                    left = "x"
            if n != N-1:
                if audio[n+1] != "x":
                    right = int(audio[n+1])
                else:
                    right = "x"
            if is_odd:
                if left != "x" and left != "init" and left > mid:
                    pass
                elif left == "x" and maxima > mid:
                    pass
                elif left != "init":
                    flag = False
                    break
                if right != "x" and right != "init" and mid < right:
                    pass
                elif right == "x" and mid < maxima:
                    pass
                elif right != "init":
                    flag = False
                    break
            else:
                if left != "x" and left != "init" and left < mid:
                    pass
                elif left == "x" and minima < mid:
                    pass
                elif left != "init":
                    flag = False
                    break
                if right != "x" and right != "init" and mid > right:
                    pass
                elif right == "x" and mid > minima:
                    pass
                elif right != "init":
                    flag = False
                    break

        else:
            left = "init"
            right = "init"
            if n != 0:
                if audio[n - 1] != "x":
                    left = int(audio[n - 1])
                else:
                    flag = False
                    break
            if n != N - 1:
                if audio[n + 1] != "x":
                    right = int(audio[n + 1])
                else:
                    flag = False
                    break
            if is_odd:
                if left != "init":
                    maxima = min(maxima, left)
                if right != "init":
                    maxima = min(maxima, right)
            else:
                if left != "init":
                    minima = max(minima, left)
                if right != "init":
                    minima = max(minima, right)

    if not flag:
        print("none")
    else:
        if maxima - minima == 2:
            print(maxima - 1)
        elif maxima - minima == 1:
            print("none")
        else:
            print("ambiguous")
