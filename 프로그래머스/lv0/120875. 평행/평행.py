import numpy as np

def slope(dots1, dots2):
    return np.divide((dots2[0] - dots1[0]), (dots2[1] - dots1[1]))

def solution(dots):
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    elif slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    elif slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    else:
        return 0