def solution(order):
    answer = 0
    for i in range(len(str(order))):
        if int(str(order)[i])%3==0 and int(str(order)[i])!=0:
            answer += 1
        else:
            continue
    return answer  