import sys

top_bra = ['.*','*.','*.','**','**','*.','**','**','*.','.*']
mid_bra = ['**','..','*.','..','.*','.*','*.','**','**','*.']
while True:
    D = int(sys.stdin.readline().rstrip('\n'))
    if not D:
        break
    flag = sys.stdin.readline().rstrip('\n')
    if flag == 'S':
        top = []
        mid = []
        bot = ['..'] * D
        msg = str(sys.stdin.readline().rstrip('\n'))
        for num in msg:
            i = int(num)
            top.append(top_bra[i])
            mid.append(mid_bra[i])
        print(*top)
        print(*mid)
        print(*bot)
    else:
        top = sys.stdin.readline().rstrip('\n').split()
        mid = sys.stdin.readline().rstrip('\n').split()
        bot = sys.stdin.readline().rstrip('\n').split()
        msg = ''
        for d in range(D):
            if top[d] == '*.':
                if mid[d] == '..':
                    msg += '1'
                elif mid[d] == '*.':
                    msg += '2'
                elif mid[d] == '.*':
                    msg += '5'
                elif mid[d] == '**':
                    msg += '8'
            elif top[d] == '.*':
                if mid[d] == '*.':
                    msg += '9'
                elif mid[d] == '**':
                    msg += '0'
            elif top[d] == '**':
                if mid[d] == '..':
                    msg += '3'
                elif mid[d] == '*.':
                    msg += '6'
                elif mid[d] == '.*':
                    msg += '4'
                elif mid[d] == '**':
                    msg += '7'
            else:
                break
        print(msg)