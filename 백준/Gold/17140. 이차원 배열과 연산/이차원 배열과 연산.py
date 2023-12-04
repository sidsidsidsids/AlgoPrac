r, c, k = map(int,input().split())
r -= 1
c -= 1
board = [list(map(int,input().split())) for _ in range(3)]
t = 0
while True:
    if len(board) > r and len(board[0]) > c and board[r][c] == k:
        break
    else:
        if t > 100:
            t = -1
            break
        H = len(board)
        W = len(board[0])
        if H >= W: # R
            new_dict = dict()
            longest = 0
            for idx in range(H):
                cnt = dict()
                width = 0
                for n in board[idx]:
                    if n:
                        if n in cnt:
                            cnt[n] += 1
                        else:
                            cnt[n] = 1
                            width += 2
                cnt = sorted(cnt.items(), key=lambda X:(X[1], X[0]))
                new_dict[idx] = cnt
                if width > longest:
                    longest = width
            if longest > 100:
                longest = 100
            board = [[0] * longest for _ in range(H)]
            for key, value in new_dict.items():
                idx = 0
                for value_key, value_value in value:
                    board[key][idx] = value_key
                    board[key][idx+1] = value_value
                    idx += 2
                    if idx > 100:
                        break
            t += 1
        else: # C
            new_dict = dict()
            longest = 0
            for idx in range(W):
                cnt = dict()
                height = 0
                for i in range(H):
                    if board[i][idx]:
                        n = board[i][idx]
                        if n in cnt:
                            cnt[n] += 1
                        else:
                            cnt[n] = 1
                            height += 2
                cnt = sorted(cnt.items(), key=lambda X: (X[1], X[0]))
                new_dict[idx] = cnt
                if height > longest:
                    longest = height
            if longest > 100:
                longest = 100
            board = [[0] * W for _ in range(longest)]
            for key, value in new_dict.items():
                idx = 0
                for value_key, value_value in value:
                    board[idx][key] = value_key
                    board[idx + 1][key] = value_value
                    idx += 2
                    if idx > 100:
                        break
            t += 1
print(t)