from collections import deque

def solution(order):
    order = deque(order)
    truck = 0
    sub = []
    
    for box in range(1, len(order)+1):
        if order[0] != box:
            sub.append(box)
            continue
        order.popleft()
        truck += 1
        while len(sub) != 0 and len(order) > 0:
            if order[0] == sub[-1]: 
                sub.pop()
                truck += 1
                order.popleft()
            else:
                break
    return truck