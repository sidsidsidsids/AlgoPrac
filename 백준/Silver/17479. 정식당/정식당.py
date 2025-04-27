normal = dict()
special = dict()
service = set()

A, B, C = map(int, input().split())
for _ in range(A):
    menu, price = input().split()
    normal[menu] = int(price)
for _ in range(B):
    menu, price = input().split()
    special[menu] = int(price)
for _ in range(C):
    menu = input()
    service.add(menu)
    
normal_price = 0
special_price = 0
service_count = 0

N = int(input())
for _ in range(N):
    order = input()
    if order in normal:
        normal_price += normal[order]
    elif order in special:
        special_price += special[order]
    elif order in service:
        service_count += 1
if (special_price > 0 and normal_price < 20000) or (service_count > 0 and (normal_price + special_price) < 50000) or service_count > 1:
    print("No")
else:
    print("Okay")