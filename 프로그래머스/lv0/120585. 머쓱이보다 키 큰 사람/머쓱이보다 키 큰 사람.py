def solution(array, height):
    answer = []
    for i in range(len(array)):
        if height < array[i]:
            answer.append(array[i])
        else:
            continue
    return len(answer)