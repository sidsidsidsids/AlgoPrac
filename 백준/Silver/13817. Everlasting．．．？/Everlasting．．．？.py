import sys

prime = [1] * 1000001
prime[0] = 0
prime[1] = 0
for n in range(2, 1000001):
    if prime[n]:
        for m in range(n + n, 1000001, n):
            prime[m] = 0

answer = []
while True:
    a, b = map(int, sys.stdin.readline().rstrip('\n').split())

    if not a or not b:
        break

    a_factors = []
    for i in range(2, a + 1):
        if prime[i] and a % i == 0:
            a_factors.append(i)

    if len(a_factors) > 1:
        a_key = a_factors[-1] - sum(a_factors[:-1])
    else:
        a_key = a_factors[0]

    b_factors = []
    for i in range(2, b + 1):
        if prime[i] and b % i == 0:
            b_factors.append(i)
    if len(b_factors) > 1:
        b_key = b_factors[-1] - sum(b_factors[:-1])
    else:
        b_key = b_factors[0]

    answer.append('a' if a_key > b_key else 'b')

for ans in answer:
    print(ans)