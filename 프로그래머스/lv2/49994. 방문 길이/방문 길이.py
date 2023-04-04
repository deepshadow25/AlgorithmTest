def solution(dirs):
    x, y = 5, 5
    path = []
    move = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}
    for i in range(len(dirs)):
        (dx, dy) = move[dirs[i]]
        if not (0 <= x+dx <=10 and 0<= y+dy <=10):
            continue
        path.append((x, y, x+dx, y+dy))
        path.append((x+dx, y+dy, x, y))
        x = x + dx
        y = y + dy
    mapset = set(path)
    return len(mapset)//2