def solution(n):
    answer = 0
    a = 1
    while n >= a:
        if n%a == 0:
            answer += 1
            a += 1
        else:
            a += 1
    return answer