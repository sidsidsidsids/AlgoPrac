case = 1
while True:
    L, P, V = map(int, input().split())
    if not L and not P and not V:
        break
    print(f"Case {case}: {L * (V // P) + min(L, V % P)}")
    case += 1