def solution(brown, yellow):
    x = ((brown/2-2)+(((2-(brown/2))**2 - 4*yellow)**0.5))/2
    y = yellow/x
    return [x+2, y+2]