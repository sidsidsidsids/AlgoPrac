import sys
from collections import defaultdict

S = int(sys.stdin.readline().rstrip('\n'))
for s in range(S):
    F = int(sys.stdin.readline().rstrip('\n'))
    file = dict()
    for f in range(F):
        file_info = sys.stdin.readline().rstrip('\n').split()
        name, H, W = file_info[0], int(file_info[1]), int(file_info[2])
        picture = [list(sys.stdin.readline().rstrip('\n')) for _ in range(H)]
        file[name] = [H, W, picture]
    css = dict()
    cssom = defaultdict(list)
    stk = list()
    M = int(sys.stdin.readline().rstrip('\n'))
    for m in range(M):
        for loc in range(7):
            css_info = sys.stdin.readline().rstrip('\n')
            if loc == 0:
                css_name = css_info.replace('#', '').replace('{', '').strip()
            elif loc == 1:
                css_info = css_info.replace('pos-x', '').replace(':', '').replace('px', '').replace(';', '').strip()
                css_x = int(css_info)
            elif loc == 2:
                css_info = css_info.replace('pos-y', '').replace(':', '').replace('px', '').replace(';', '').strip()
                css_y = int(css_info)
            elif loc == 3:
                css_info = css_info.replace('position', '').replace(':', '').replace(';', '').strip()
                if len(css_info) > 8:
                    css_info = css_info.split('=')
                    parent = css_info[-1].strip()
                    cssom[parent].append(css_name)
                else:
                    stk.append(css_name)
            elif loc == 4:
                css_info = css_info.split(':')
                css_file = css_info[1].replace(';', '').strip()
            elif loc == 5:
                css_info = css_info.replace('layer', '').replace(':', '').replace(';', '').strip()
                css_layer = int(css_info)
            elif loc == 6:
                pass
        css[css_name] = [css_layer, css_y, css_x, css_file]

    while stk:
        elem = stk.pop()
        for child in cssom[elem]:
            css[child][1] += css[elem][1]
            css[child][2] += css[elem][2]
            stk.append(child)

    orders = []
    y_max = 0
    x_max = 0
    l_cur = 0
    cnt = 0
    while cnt < M:
        for key, val in css.items():
            if val[0] == l_cur:
                y_max = max(y_max, val[1] + file[val[3]][0])
                x_max = max(x_max, val[2] + file[val[3]][1])
                orders.append(key)
                cnt += 1
        l_cur += 1
    grid = [['.'] * x_max for _ in range(y_max)]

    for m in range(M):
        target = css[orders[m]]
        i = target[1]
        j = target[2]
        image_file = file[target[3]]
        height = image_file[0]
        width = image_file[1]
        image = image_file[2]

        for h in range(i, i+height):
            for w in range(j, j+width):
                if grid[h][w] != image[h-i][w-j] and image[h-i][w-j] != '.':
                    grid[h][w] = image[h-i][w-j]

    print(f'Scenario #{s+1}:')
    for line in grid:
        for elem in line:
            print(elem if elem != '.' else ' ', end="")
        print()
    print()