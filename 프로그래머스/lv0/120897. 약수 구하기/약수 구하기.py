def solution(n):
    answer = []
    k = 1
    for i in range(n+1): 
        if n % (i+1) == 0:
            answer.append(i+1)
            k += 1
        else:
            k += 1
    return answer