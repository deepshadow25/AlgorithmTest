def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else times(num_list)
    
def times(num_list):
    answer = 1
    for i in num_list:
        answer *= i
        if i == 0:
            return 0
    return answer