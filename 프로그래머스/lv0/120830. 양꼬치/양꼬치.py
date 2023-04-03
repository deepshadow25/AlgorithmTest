def solution(n, k):
    answer = n*12000 + k*2000
    if n >= 10:
        answer -= (2000*(n//10))
    return answer