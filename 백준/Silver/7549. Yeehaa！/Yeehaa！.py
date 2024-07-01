import sys
import math
T = int(sys.stdin.readline().rstrip('\n'))
for t in range(T):
    line = list(sys.stdin.readline().rstrip('\n').split())
    R = float(line[0])
    degree = 360 / int(line[1]) / 2
    print(f'Scenario #{t+1}:')
    print("{:.3f}".format(round(R * math.sin(math.radians(degree)) / (1 + math.sin(math.radians(degree))), 3)))
    print()