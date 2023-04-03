def solution(num1, num2):
    num1=int(num1);num2=int(num2)
    if (num1 or num2) < -50000 or (num1 or num2) > 50000 :
        print ("숫자는 -5만과 +5만 사이로 넣어주세요")
        return
    answer = num1-num2
    return answer