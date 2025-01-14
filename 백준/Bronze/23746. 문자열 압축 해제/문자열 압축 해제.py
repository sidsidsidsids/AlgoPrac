N = int(input())
hm = dict()
for _ in range(N):
    e, k = input().split()
    hm[k] = e
S = input()
s = ''
for e in S:
    s += hm[e]
si, ei = map(int, input().split())
print(s[si-1:ei])