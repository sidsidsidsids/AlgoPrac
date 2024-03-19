arr = list(map(int,input().split()))

def function(array):
    answer = 0
    for i in range(1,5):
        array[i] = array[i] / 100

    def recursion(cnt, lim, rec, y, x, val):
        if cnt == lim:
            nonlocal answer
            answer += val
            return
        else:
            for idx in range(1, 5):
                ny, nx = y, x
                if array[idx]:
                    if idx == 1:
                        nx = x + 1
                    elif idx == 2:
                        nx = x - 1
                    elif idx == 3:
                        ny = y + 1
                    elif idx == 4:
                        ny = y - 1

                    if (ny, nx) in rec:
                        continue
                    else:
                        rec.add((ny, nx))
                        val *= array[idx]
                        recursion(cnt + 1, lim, rec, ny, nx, val)
                        val /= array[idx]
                        rec.remove((ny, nx))

    recursion(0, array[0], {(0, 0)}, 0, 0, 1)
    return round(answer, 10)

print(function(arr))