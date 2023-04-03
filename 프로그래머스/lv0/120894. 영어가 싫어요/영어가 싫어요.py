def solution(numbers):
    num_dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for char, idx in num_dic.items():
        numbers = numbers.replace(char, str(idx))
    return int(numbers)