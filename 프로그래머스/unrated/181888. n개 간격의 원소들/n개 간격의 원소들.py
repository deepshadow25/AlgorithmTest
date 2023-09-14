def solution(num_list, n):
    return [num for idx, num in enumerate(num_list) if idx%n == 0]
    