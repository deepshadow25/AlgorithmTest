def solution(num_list):
    sorted(num_list)
    odd = []
    even = []
    answer = []
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even.append(num_list[i])
        else:
            odd.append(num_list[i])
    answer.append(len(even))
    answer.append(len(odd))
    return answer