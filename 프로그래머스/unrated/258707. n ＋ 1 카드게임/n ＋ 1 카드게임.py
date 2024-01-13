def solution(coin, cards):
    hand = set(cards[:len(cards) // 3])
    target = len(cards) + 1
    answer = 0
    rest = set()
    n1 = len(cards) // 3
    n2 = len(cards) // 3 + 1
    while True:
        answer += 1
        next_round = False
        if n2 < len(cards):
            rest.add(cards[n1])
            rest.add(cards[n2])
        else:
            break

        for elem in hand:
            if target - elem in hand:
                hand.remove(elem)
                hand.remove(target - elem)
                next_round = True
                break
        if next_round:
            n1 += 2
            n2 += 2
            continue

        for nelem in rest:
            if target - nelem in hand and coin > 0:
                rest.remove(nelem)
                hand.remove(target - nelem)
                next_round = True
                coin -= 1
                break
        if next_round:
            n1 += 2
            n2 += 2
            continue

        for nnelem in rest:
            if target - nnelem in rest and coin > 1:
                rest.remove(nnelem)
                rest.remove(target - nnelem)
                next_round = True
                coin -= 2
                break
        if next_round:
            n1 += 2
            n2 += 2
            continue

        break

    return answer