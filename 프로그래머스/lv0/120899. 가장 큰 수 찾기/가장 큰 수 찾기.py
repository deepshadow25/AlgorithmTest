def solution(array):
    answer = [max(array)]
    for i in range(len(array)):
        if array[i] == max(array):
            answer.append(i)
    return answer