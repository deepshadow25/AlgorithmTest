def solution(sizes):
    answer = [[],[]]
    for i, j in sizes:
        if i < j:
            i, j = j, i
        answer[0].append(i)
        answer[1].append(j)
    return max(answer[0]) * max(answer[1])