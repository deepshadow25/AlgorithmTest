import math

def solution(m, n, startX, startY, balls):
    return [compare(m, n, x, y, startX, startY) for x, y in balls]

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2,2))

def compare(m, n, x, y, startX, startY):
    left, right, low, high = float('inf'),float('inf'),float('inf'),float('inf')
    if not (startX==x and startY>y):
        low = distance(startX, -startY, x, y)
    if not (startX>x and startY==y):
        left = distance(-startX, startY, x, y)
    if not (startX==x and startY<y):
        high = distance(startX, 2*n-startY, x, y)
    if not (startX<x and startY==y):
        right = distance(2*m-startX, startY, x, y)
    return round(math.pow(min(left,right,low,high),2))
