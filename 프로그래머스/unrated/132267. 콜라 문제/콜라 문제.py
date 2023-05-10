def solution(a, b, n):
    answer = 0
    while n!=0:
        c = n%a
        n = n//a
        answer += n * b
        n = n*b + c
        if n < a:
            break
    return answer