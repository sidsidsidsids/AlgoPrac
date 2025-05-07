for _ in range(3):
    문자 = input()
    현재 = ""
    연속 = 1
    기록 = 1
    for 원소 in 문자:
        if 원소 == 현재:
            연속 += 1
            기록 = max(기록, 연속)
        else:
            연속 = 1
        현재 = 원소
    print(기록)