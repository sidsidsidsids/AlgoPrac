import sys

N, M = map(int, sys.stdin.readline().strip().split())

files = []
for _ in range(N):
    files.append(tuple(sys.stdin.readline().strip().split(".")))
extensions = set()
for _ in range(M):
    extensions.add(sys.stdin.readline().strip())

sort_files = sorted(files, key=lambda X:(X[0], X[1]))

answer = []
temp = []
for file, ext in sort_files:
    if temp and file != temp[0][0]:
        for t_file, t_ext in temp:
            answer.append(t_file + "." + t_ext)
        temp = []
    if ext in extensions:
        answer.append(file + "." + ext)
    else:
        temp.append((file, ext))
for t_file, t_ext in temp:
    answer.append(t_file + "." + t_ext)
print("\n".join(answer))