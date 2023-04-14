def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        temp = bin(x|y)[2:].replace('1','#').replace('0',' ')
        if len(temp) < n :
            temp = ' ' * (n-len(temp)) + temp
        answer.append(temp)
    return answer