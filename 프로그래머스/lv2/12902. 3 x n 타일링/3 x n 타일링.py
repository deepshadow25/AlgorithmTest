def solution(n):
    answer = [1, 3]
    if n == 2:
        return answer[1]
    
    n /= 2
    n -= 1  # n = 2 (4/2)인 경우부터 직사각형 수를 셀 것임. 3 -> 1
    while n > 0:
        answer = [answer[1], 4*answer[1]-answer[0]]
        n -= 1
    return answer[1]%1000000007