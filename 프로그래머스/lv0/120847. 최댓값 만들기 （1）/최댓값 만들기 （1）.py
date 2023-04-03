def solution(numbers):
    sorted(numbers)
    numbers.sort(reverse=False)
    a = numbers.pop(-1)
    b = numbers.pop(-1)
    return a*b