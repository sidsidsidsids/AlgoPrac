A, B, V = map(int,input().split())
time = ((V-A) / (A-B))
if time % 1:
    time = -(-time//1)
print(round(time) + 1)