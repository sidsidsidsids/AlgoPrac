K = [0] * 2
for _ in range(int(input())):
    K[int(input())] += 1
print("Junhee is not cute!" if K[0] > K[1] else "Junhee is cute!")