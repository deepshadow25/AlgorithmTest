def solution(array, commands):
    answer = []
    for idx, com in enumerate(commands):
        arr = sorted(array[com[0]-1:com[1]])
        answer.append(arr[com[2]-1])
    return answer