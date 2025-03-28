import sys
from functools import reduce

bowls = sys.stdin.readline().strip()


def calculate_height(state, bowl):
    value, prev_shape = state

    if bowl == prev_shape:
        value += 5
    else:
        value += 10

    return value, bowl


answer, _ = reduce(calculate_height, bowls, (0, ''))

print(answer)
