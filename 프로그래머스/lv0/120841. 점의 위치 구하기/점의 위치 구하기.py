def solution(dot):
    sorted(dot)
    x = dot[0]; y = dot[1]
    if x == 0 or y == 0: pass
    if x>0 and y>0: return 1
    if x<0 and y>0: return 2
    if x<0 and y<0: return 3
    if x>0 and y<0: return 4