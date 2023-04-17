def solution(r1, r2):
    answer = 4
    for i in range(1, r2):
        x2 = int((r2**2 - i**2)**0.5)
        if i >= r1:
            answer += 4 * (x2+1)
        else:
            x1 = int((r1**2 - i**2)**0.5)
            if x1**2 + i**2 == r1**2:
                answer += 4 * (x2-x1+1)
            else:
                answer += 4 * (x2-x1)
    return answer