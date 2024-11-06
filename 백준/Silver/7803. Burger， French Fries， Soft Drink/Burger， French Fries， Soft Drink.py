import sys

while True:
    try:
        N, O = sys.stdin.readline().rstrip('\n').split()
        N = int(N)
        L = len(O)
        info = dict()
        info["B"] = 0
        info["F"] = 0
        info["S"] = 0

        arr = []
        flag = False
        for l in range(L):
            info[O[l]] += 1
            flag = False
            if (l + 1) % 3 == 0:
                if info["B"] == info["F"] and info["F"] == info["S"]:
                    arr.append(info["B"])
                    info["B"] = 0
                    info["F"] = 0
                    info["S"] = 0
                    flag = True

        if not flag or len(arr) < N:
            print("Impossible")
        else:
            def nCk(n, k):
                up = 1
                down = 1
                for _ in range(k):
                    up *= n
                    n -= 1
                for _ in range(k):
                    down *= k
                    k -= 1
                return up // down
            print(nCk(len(arr) - 1, N - 1))
    except:
        break