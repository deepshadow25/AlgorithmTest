def solution(num1, num2):
    num1 = int(num1) ; num2 = int(num2)
    if (num1 or num2) > 100 or (num1 or num2) < 0:
        return
    return int(num1/num2)