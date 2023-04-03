def one_in_binary(n):
    n_one = 0
    for i in bin(n)[2:]:
        if i == '1':
            n_one += 1
    return n_one

def solution(n):
    m = n+1
    while m:
        if one_in_binary(m) == one_in_binary(n):
            return m
        else:
            m += 1
            continue