def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    if numbers[1] >= 0 and numbers[0] < 0:
        answer = numbers[-1]*numbers[-2]
    if numbers[1] < 0:
        if abs(numbers[0]) * abs(numbers[1]) > abs(numbers[-1]) * abs(numbers[-2]):
            answer = numbers[0] * numbers[1]
        else:
            answer = numbers[-1] * numbers[-2]
    if numbers[0] > 0:
        answer = numbers[-1] * numbers[-2]
    return answer