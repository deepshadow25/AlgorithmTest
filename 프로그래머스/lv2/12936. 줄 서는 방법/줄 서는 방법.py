from math import factorial

def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n+1)]
    k -= 1
    
    for i in range(n, 0, -1):
        div, k = divmod(k, factorial(i-1))
        answer.append(numbers.pop(div))
        
    return answer