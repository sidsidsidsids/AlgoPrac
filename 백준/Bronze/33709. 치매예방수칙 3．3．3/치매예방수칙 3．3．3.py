import re
N = input()
print(sum(list(map(int, re.split(r"[.|:|#]", input())))))