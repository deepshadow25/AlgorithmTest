def solution(n):
    answer = ''
    n = sorted(list(''.join(str(n))), reverse=True)
    for i in n:
        answer += i
    return int(answer)