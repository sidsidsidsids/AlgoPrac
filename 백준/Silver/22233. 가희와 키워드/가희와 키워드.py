import sys
N, M = map(int,sys.stdin.readline().split())
memo = set()
for n in range(N):
    word = sys.stdin.readline().rstrip()
    memo.add(word)
for m in range(M):
    words = list(map(str,sys.stdin.readline().rstrip().split(',')))
    for word in words:
        if word in memo:
            memo.remove(word)
    print(len(memo))