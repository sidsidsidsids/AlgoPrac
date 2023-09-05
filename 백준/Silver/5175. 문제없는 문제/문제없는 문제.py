from itertools import combinations

T = int(input())
for tc in range(T):
    M, N = map(int,input().split())
    Q = [0] * N
    for n in range(N):
        Q[n] = set(map(int,input().split()))
    answer = []
    algoSet = [[n, chr(n + 65)] for n in range(N)]
    for n in range(1,N+1):
        combList = list(combinations(algoSet, n))
        for tuples in combList:
            test = set()
            inputQ = set()
            for atom in tuples:
                for algos in Q[atom[0]]:
                    test.add(algos)
                inputQ.add(atom[1])
            if len(test) == M:
                answer = inputQ
                break
        if answer:
            break
    print(f'Data Set {tc+1}:', *sorted(answer))
    print()