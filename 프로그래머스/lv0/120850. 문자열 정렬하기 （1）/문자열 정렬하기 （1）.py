def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        for j in range(10):
            if list(my_string)[i] == list('1234567890')[j]:
                answer.append(int(list(my_string)[i]))
    return sorted(answer)