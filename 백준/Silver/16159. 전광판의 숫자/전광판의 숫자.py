from itertools import permutations
info = dict()
info[(0, 0, 1, 1, 1, 0, 0)] = 0
info[(0, 0, 0, 0, 0, 0, 0)] = 1
info[(0, 1, 1, 1, 0, 1, 0)] = 2
info[(0, 0, 1, 0, 1, 0, 0)] = 3
info[(0, 0, 0, 0, 1, 0, 0)] = 4
info[(0, 1, 0, 0, 1, 1, 0)] = 5
info[(0, 0, 0, 1, 1, 1, 0)] = 6
info[(0, 1, 1, 0, 0, 0, 0)] = 7
info[(0, 1, 1, 1, 1, 1, 0)] = 8
info[(1, 1, 1, 1, 1, 1 ,1)] = 9

num_info = [
    [[0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 1, 0, 1, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 0, 1, 1, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0]],
    [[0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0]],
]

board = [[] for _ in range(7)]
for n in range(7):
    board[n] = list(input())
L = len(board[0])
target = []
for j in range(4, L, 6):
    value = []
    for i in range(7):
        value.append(int(board[i][j]))
    value = tuple(value)
    target.append(info[value])

cases = list(permutations(sorted(target)))
target = tuple(target)
answer = -1
flag = False
for case in cases:
    if flag:
        answer = case
        break
    if case == target:
        flag = True
        continue

if answer == -1:
    print("The End")
else:
    for n in range(7):
        for num in answer:
            for elem in num_info[num][n]:
                print(elem, end="")
        print()
