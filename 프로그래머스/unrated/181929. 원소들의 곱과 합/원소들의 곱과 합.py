def solution(num_list):
    times = 1
    for i in num_list:
        times *= i
    return 1 if times < sum(num_list)**2 else 0