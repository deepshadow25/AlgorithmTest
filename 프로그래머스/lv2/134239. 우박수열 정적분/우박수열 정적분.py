def solution(k, ranges):
    area = [0.0]
    answer = []
    
    while k != 1:
        n = (k//2) if k%2==0 else (3*k)+1
        minY, maxY = min(n, k), max(n, k)
        area.append(area[-1] + (minY + 0.5 * (maxY-minY)))
        k = n
        
    Len = len(area)
    
    for x1, x2 in ranges:
        if Len + (x2-1) >= x1:
            answer.append(float(area[x2-1]-area[x1]))
        else:
            answer.append(-1)
            
    return answer
