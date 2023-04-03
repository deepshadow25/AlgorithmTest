def solution(num):
    answer = 0
    while num > 1:
        if num%2 == 0:
            num /= 2
            answer += 1
            continue
        if num%2 != 0:
            num = 3*num + 1
            answer += 1
            continue
    if answer > 500:
        return -1
    if num == 1 and answer == 0:
        return 0
    return answer