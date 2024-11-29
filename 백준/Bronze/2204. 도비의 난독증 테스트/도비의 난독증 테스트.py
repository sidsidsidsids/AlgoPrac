while True:
    N = int(input())
    if N == 0:
        break
    arr = []
    for n in range(N):
        S = input()
        arr.append((S.lower(), S))
    print(sorted(arr, key=lambda X:(X[0], X[1]))[0][1])