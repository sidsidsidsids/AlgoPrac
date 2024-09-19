import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_multiple(numbers: list):
    result = numbers[0]
    for num in numbers[1:]:
        if result >= num:
            result = lcm(result, num)
        else:
            result = lcm(num, result)
    return result

def monkey_dance(number: int):
    graph = [0] * (number + 1)
    visit = [0] * (number + 1)
    for _ in range(number):
        a, b = map(int, sys.stdin.readline().rstrip('\n').split())
        graph[a] = b

    distances = []
    for n in range(number):
        if not visit[n]:
            dist = 0
            visit[n] = 1
            current = n
            while True:
                current = graph[current]
                dist += 1
                visit[current] = 1
                if current == n:
                    break
            distances.append(dist)

    return lcm_multiple(distances)

while True:
    N = int(sys.stdin.readline().rstrip('\n'))
    if not N:
        break
    print(monkey_dance(N))
