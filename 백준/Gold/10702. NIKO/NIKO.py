N = int(input())
format_dict = dict()
format_list = []
for _ in range(N):
    O, V, N = map(int, input().rstrip('\n').split('-'))
    format_dict[(O, V, N)] = 0
    format_list.append((O, V, N))
players = []
M = int(input())
for _ in range(M):
    players.append(list(input()))

def func(idx, o, v, n, cnt):
    if idx == M or cnt == 10:
        if (o, v, n) in format_dict:
            format_dict[(o, v, n)] = 1
        return

    func(idx + 1, o, v, n, cnt)
    for position in players[idx]:
        if position == 'O':
            func(idx + 1, o + 1, v, n, cnt + 1)
        elif position == 'V':
            func(idx + 1, o, v + 1, n, cnt + 1)
        elif position == 'N':
            func(idx + 1, o, v, n + 1, cnt + 1)

func(0, 0, 0, 0, 0)
for elem in format_list:
    print("DA" if format_dict[elem] == 1 else "NE")