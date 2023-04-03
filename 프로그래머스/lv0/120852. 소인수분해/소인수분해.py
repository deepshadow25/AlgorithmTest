def solution(n):
    x = 2
    answer = []
    while x<=n:
        if n%x==0:
            answer.append(x)
            n /= x
        else:
            x += 1
    if len(answer) == 0:
        return [n]
    return sorted((set(answer)))