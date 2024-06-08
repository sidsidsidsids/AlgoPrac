from collections import defaultdict
import sys


class File:
    def __init__(self, name):
        self.name = name


class Folder:
    def __init__(self, name):
        self.name = name
        self.subfolders = {}
        self.subfiles = {}

    def add_folder(self, name):
        if name not in self.subfolders:
            self.subfolders[name] = Folder(name)

    def add_file(self, name):
        if name not in self.subfiles:
            self.subfiles[name] = File(name)


N, M = map(int, sys.stdin.readline().rstrip('\n').split())
main_folder = Folder('main')
folder_map = {'main': main_folder}
suspend = defaultdict(list)
for _ in range(N+M):
    parent, target, is_folder = sys.stdin.readline().rstrip('\n').split()
    is_folder = int(is_folder)
    if parent in folder_map:
        parent_folder = folder_map[parent]
        if is_folder:
            parent_folder.add_folder(target)
            folder_map[target] = parent_folder.subfolders[target]
        else:
            parent_folder.add_file(target)
    else:
        suspend[parent].append((target, is_folder))

while suspend:
    for parent in list(suspend.keys()):
        if parent in folder_map:
            parent_folder = folder_map[parent]
            for target, is_folder in suspend.pop(parent):
                if is_folder:
                    parent_folder.add_folder(target)
                    folder_map[target] = parent_folder.subfolders[target]
                else:
                    parent_folder.add_file(target)


query = int(sys.stdin.readline().rstrip('\n'))
for _ in range(query):
    target = sys.stdin.readline().rstrip('\n').split('/')[-1]
    Q = [target]
    files = set()
    file_kinds = 0
    file_cnts = 0
    while Q:
        folder_name = Q.pop()
        current_folder = folder_map[folder_name]
        for file in current_folder.subfiles:
            if file not in files:
                files.add(file)
                file_kinds += 1
            file_cnts += 1
        for folder in current_folder.subfolders:
            Q.append(folder)
    print(file_kinds, file_cnts)