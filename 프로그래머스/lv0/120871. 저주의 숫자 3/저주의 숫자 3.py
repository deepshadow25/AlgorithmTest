def solution(n):
    n_list = [i for i in range(1,230)]
    result = []
    for i in n_list:
        if i%3!=0 and i%10!=3 and (i<30 or i>39) and (i<129 or i>139):
            result.append(i)
    return result[:100][n-1]