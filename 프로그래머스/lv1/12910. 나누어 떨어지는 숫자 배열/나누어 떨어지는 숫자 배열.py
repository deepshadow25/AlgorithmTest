def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
        elif i%divisor !=0:
            continue
    if len(answer)==0:
        return [-1]
    return sorted(answer)