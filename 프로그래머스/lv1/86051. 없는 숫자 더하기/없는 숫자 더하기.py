def solution(numbers):
    result = 0
    i = 0
    while 0<=i<=9:
        if i not in numbers:
            result += i
            i += 1
        else:
            i += 1
    return result