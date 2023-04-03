def solution(s):
    result = 0
    for i in range(len(s.split())):
        if s.split()[i] != 'Z':
            result += int(s.split()[i])
        if s.split()[i] == 'Z':
            result -= int(s.split()[i-1])
    return result