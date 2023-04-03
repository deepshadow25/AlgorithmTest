def solution(num1, num2):
    num1 = int(num1) ; num2 = int(num2)
    if (num1 or num2) > 100 or (num1 or num2) < 0:
        return
    else:
        return num1-int(num1/num2)*num2
    return