import sys

N = int(sys.stdin.readline().rstrip('\n'))
TVs = []
for _ in range(N):
    TVs.append(sys.stdin.readline().rstrip('\n'))
answer = ""

for n in range(N):
    if n == 0 and TVs[n] == "KBS1":
        break
    if TVs[n] == "KBS1":
        k = n
        while TVs[0] != "KBS1":
            TVs[k-1], TVs[k] = TVs[k], TVs[k-1]
            answer += "4"
            k -= 1
        break
    answer += "1"

for n in range(N):
    if n == 1 and TVs[n] == "KBS2":
        break
    if TVs[n] == "KBS2":
        k = n
        while TVs[1] != "KBS2":
            TVs[k-1], TVs[k] = TVs[k], TVs[k-1]
            answer += "4"
            k -= 1
        break
    answer += "1"

print(answer)