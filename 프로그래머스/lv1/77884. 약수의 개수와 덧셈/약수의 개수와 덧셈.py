from collections import defaultdict

def solution(left, right):
    answer = []
    for i in range(left, right+1): 
        if len(divisor_loop(i)[i]) % 2:
            answer.append(-i)
        else:
            answer.append(i)
    return sum(answer)

def divisor_loop(num: int):
    result = defaultdict(list)
    for i in range(1, num+1):
        for j in range(1, int(num/i) + 1):
            result[i*j].append(i)
    return result